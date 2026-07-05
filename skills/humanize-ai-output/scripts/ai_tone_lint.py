#!/usr/bin/env python3
"""Flag common AI-ish language patterns in a text file or stdin."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


DEFAULT_THRESHOLD = 95


@dataclass(frozen=True)
class Pattern:
    code: str
    label: str
    regex: str
    suggestion: str
    weight: int


PATTERNS = [
    Pattern("CN01", "forced Chinese contrast", r"不是[^。；\n]{1,80}而是|是[^。；\n]{1,80}而不是|并非[^。；\n]{1,80}而(?:是|在)", "Keep only if it clarifies a real boundary.", 40),
    Pattern("CN02", "problem-not-in Chinese contrast", r"问题不在[^。；\n]{1,80}而在", "State the focus directly before adding context.", 40),
    Pattern("CN03", "negative-first Chinese advice", r"(^|[。！？\n])\s*(先别|不建议|不需要|不要)[^。！？\n]{1,80}", "Start from the affirmative action unless the rejected option is specific and necessary.", 25),
    Pattern("CN04", "abstract Chinese slogan", r"赋能|闭环|抓手|生态|底层逻辑|价值沉淀|提质增效|协同发力", "Replace with concrete actors, actions, and outcomes.", 15),
    Pattern("CN05", "mechanical Chinese transition", r"首先|其次|最后|综上所述|值得注意的是", "Use content-shaped transitions or remove.", 10),
    Pattern("EN01", "AI stock vocabulary", r"\b(delves?|tapestry|robust|seamless|leverage|unlock|transformative|game-changing)\b", "Use plainer verbs and domain nouns.", 15),
    Pattern("EN02", "generic opening", r"\bIn today's fast-paced world\b|\bAs technology continues to evolve\b", "Open with the specific situation or finding.", 25),
    Pattern("EN03", "overbalanced English contrast", r"\bnot only\b.{1,120}\bbut also\b|\bnot merely\b.{1,120}\bbut\b", "Use direct phrasing unless the contrast matters.", 35),
    Pattern("EN04", "broad English negative contrast", r"\bnot\b[^.\n]{1,100}\b(?:but|rather than)\b", "Start with the affirmative claim unless the contrast target is concrete.", 40),
    Pattern("EN05", "trailing not-frame", r",\s*not\s+[A-Za-z][^.\n]{1,100}", "Remove broad trailing negation and state the positive claim directly.", 35),
    Pattern("EN06", "not-alone contrast", r"\bnot\b[^.\n]{0,80}\balone\b", "Avoid vague 'not X alone' framing; name the useful advantage directly.", 35),
    Pattern("FMT01", "colon-led explanation", r"(?mi)^\s*(?:[-*]\s*)?(?:\*\*)?(?:标题|问题|指标|背景|挑战|策略|展望|痛点|方案|价值|负责人|decision needed|slide title|next question|question|metric|problem|strategy|value|background|challenge)\s*[:：]\s*[^:\n：]+", "Split into a normal sentence or use a dash only for a real field.", 20),
    Pattern("FMT02", "quoted framing label", r"[\"“][^\"”\n]{2,50}[\"”]", "Remove quote wrappers when the label is doing the explanation.", 10),
    Pattern("FMT03", "plus-stack shorthand", r"\S+\s*\+\s*\S+\s*\+\s*\S+", "Turn stacked labels into a sentence with priority.", 15),
    Pattern("FMT04", "negative-first title", r"(?mi)^\s*(?:#+\s*)?(?:\*\*)?(?:先别|不建议|不需要|不要|don't|do not)\b", "Use an affirmative title that names the action or focus.", 30),
    Pattern("IMG01", "image prompt quality tags", r"\b(8K|masterpiece|ultra[- ]detailed|hyper[- ]realistic|breathtaking|award[- ]winning)\b", "Replace quality tags with art direction.", 20),
    Pattern("LAY01", "generic design trope", r"\b(three cards|rounded cards|purple gradient|glassmorphism|floating orb|sparkles)\b", "Use layout hierarchy tied to content.", 15),
]


def read_text(path: str | None) -> str:
    if path:
        return Path(path).read_text(encoding="utf-8")
    return sys.stdin.read()


def lint(text: str) -> list[tuple[Pattern, int]]:
    findings: list[tuple[Pattern, int]] = []
    for pattern in PATTERNS:
        count = len(re.findall(pattern.regex, text, flags=re.IGNORECASE | re.DOTALL | re.MULTILINE))
        if count:
            findings.append((pattern, count))
    return findings


def score(text: str) -> tuple[int, list[dict[str, int | str]]]:
    findings = lint(text)
    payload: list[dict[str, int | str]] = []
    penalty = 0
    for pattern, count in findings:
        item_penalty = pattern.weight * count
        penalty += item_penalty
        payload.append(
            {
                "code": pattern.code,
                "label": pattern.label,
                "count": count,
                "weight": pattern.weight,
                "penalty": item_penalty,
                "suggestion": pattern.suggestion,
            }
        )
    return max(0, 100 - penalty), payload


def main() -> int:
    parser = argparse.ArgumentParser(description="Flag common AI-ish language patterns.")
    parser.add_argument("--score", action="store_true", help="Emit JSON score and fail below threshold.")
    parser.add_argument("--threshold", type=int, default=DEFAULT_THRESHOLD, help="Minimum passing score for --score.")
    parser.add_argument("path", nargs="?", help="Text file to scan. Reads stdin when omitted.")
    args = parser.parse_args()
    text = read_text(args.path)
    findings = lint(text)
    if args.score:
        value, score_findings = score(text)
        print(
            json.dumps(
                {
                    "score": value,
                    "threshold": args.threshold,
                    "passed": value >= args.threshold,
                    "findings": score_findings,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0 if value >= args.threshold else 1
    if not findings:
        print("No configured AI-ish patterns found.")
        return 0
    for pattern, count in findings:
        print(f"{pattern.code}\t{count}\t-{pattern.weight * count}\t{pattern.label}\t{pattern.suggestion}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
