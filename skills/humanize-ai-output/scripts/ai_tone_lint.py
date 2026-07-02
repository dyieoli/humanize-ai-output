#!/usr/bin/env python3
"""Flag common AI-ish language patterns in a text file or stdin."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Pattern:
    code: str
    label: str
    regex: str
    suggestion: str


PATTERNS = [
    Pattern("CN01", "forced Chinese contrast", r"不是[^。；\n]{1,80}而是|是[^。；\n]{1,80}而不是", "Keep only if it clarifies a real boundary."),
    Pattern("CN02", "abstract Chinese slogan", r"赋能|闭环|抓手|生态|底层逻辑|价值沉淀|提质增效|协同发力", "Replace with concrete actors, actions, and outcomes."),
    Pattern("CN03", "mechanical Chinese transition", r"首先|其次|最后|综上所述|值得注意的是", "Use content-shaped transitions or remove."),
    Pattern("EN01", "AI stock vocabulary", r"\b(delves?|tapestry|robust|seamless|leverage|unlock|transformative|game-changing)\b", "Use plainer verbs and domain nouns."),
    Pattern("EN02", "generic opening", r"\bIn today's fast-paced world\b|\bAs technology continues to evolve\b", "Open with the specific situation or finding."),
    Pattern("EN03", "overbalanced English contrast", r"\bnot only\b.{1,120}\bbut also\b|\bnot merely\b.{1,120}\bbut\b", "Use direct phrasing unless the contrast matters."),
    Pattern("IMG01", "image prompt quality tags", r"\b(8K|masterpiece|ultra[- ]detailed|hyper[- ]realistic|breathtaking|award[- ]winning)\b", "Replace quality tags with art direction."),
    Pattern("LAY01", "generic design trope", r"\b(three cards|rounded cards|purple gradient|glassmorphism|floating orb|sparkles)\b", "Use layout hierarchy tied to content."),
]


def read_text(path: str | None) -> str:
    if path:
        return Path(path).read_text(encoding="utf-8")
    return sys.stdin.read()


def lint(text: str) -> list[tuple[Pattern, int]]:
    findings: list[tuple[Pattern, int]] = []
    for pattern in PATTERNS:
        count = len(re.findall(pattern.regex, text, flags=re.IGNORECASE | re.DOTALL))
        if count:
            findings.append((pattern, count))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Flag common AI-ish language patterns.")
    parser.add_argument("path", nargs="?", help="Text file to scan. Reads stdin when omitted.")
    args = parser.parse_args()
    text = read_text(args.path)
    findings = lint(text)
    if not findings:
        print("No configured AI-ish patterns found.")
        return 0
    for pattern, count in findings:
        print(f"{pattern.code}\t{count}\t{pattern.label}\t{pattern.suggestion}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
