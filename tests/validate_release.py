#!/usr/bin/env python3
"""Release checks for the humanize-ai-output skill package."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "humanize-ai-output"


def read(path: Path) -> str:
    if not path.exists():
        raise AssertionError(f"Missing required file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def require(text: str, needle: str, label: str) -> None:
    if needle.lower() not in text.lower():
        raise AssertionError(f"Missing {label}: {needle}")


def require_count(text: str, pattern: str, minimum: int, label: str) -> None:
    count = len(re.findall(pattern, text, flags=re.IGNORECASE | re.MULTILINE))
    if count < minimum:
        raise AssertionError(f"Expected at least {minimum} {label}, found {count}")


def check_skill_metadata() -> None:
    body = read(SKILL / "SKILL.md")
    require(body, "name: humanize-ai-output", "skill name")
    require(body, "description:", "frontmatter description")
    for phrase in [
        "Chinese",
        "English",
        "bilingual",
        "presentation",
        "document",
        "image prompt",
        "variation",
        "style_seed.py",
        "Preserve facts",
        "Do not claim to bypass AI detection",
    ]:
        require(body, phrase, "SKILL.md coverage")

    for phrase in [
        "不是",
        "而是",
        "templated",
        "generic",
        "sentence length",
        "layout",
        "composition",
    ]:
        require(body, phrase, "AI-ish pattern coverage")


def check_references() -> None:
    references = {
        "chinese-style-patterns.md": ["不是", "而是", "口语", "连接"],
        "english-bilingual-patterns.md": ["bilingual", "translationese", "rhythm"],
        "design-and-ppt-patterns.md": ["PPT", "layout", "hierarchy"],
        "image-prompt-patterns.md": ["image prompt", "composition", "lighting"],
        "variation-recipes.md": ["variation", "seed", "recipe"],
        "examples.md": ["Before", "After", "What changed"],
    }
    for filename, phrases in references.items():
        body = read(SKILL / "references" / filename)
        for phrase in phrases:
            require(body, phrase, filename)


def check_scripts() -> None:
    for script in ["style_seed.py", "ai_tone_lint.py"]:
        path = SKILL / "scripts" / script
        read(path)
        result = subprocess.run(
            [sys.executable, str(path), "--help"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        if result.returncode != 0:
            raise AssertionError(f"{script} --help failed: {result.stderr or result.stdout}")

    seed_result = subprocess.run(
        [sys.executable, str(SKILL / "scripts" / "style_seed.py"), "--seed", "7"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if seed_result.returncode != 0 or seed_result.stderr:
        raise AssertionError(f"style_seed.py must emit clean JSON without stderr: {seed_result.stderr}")
    recipe = json.loads(seed_result.stdout)
    if not recipe.get("generated_at", "").endswith("Z"):
        raise AssertionError("style_seed.py generated_at must be UTC-like and end with Z")

    image_result = subprocess.run(
        [sys.executable, str(SKILL / "scripts" / "style_seed.py"), "--task", "image", "--seed", "7"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if image_result.returncode != 0 or image_result.stderr:
        raise AssertionError(f"style_seed.py --task image must emit clean JSON: {image_result.stderr}")
    image_recipe = json.loads(image_result.stdout)
    if image_recipe.get("task") != "image":
        raise AssertionError("style_seed.py --task image must include task=image in output")
    if image_recipe.get("voice") not in {"visual director", "document editor"}:
        raise AssertionError("style_seed.py --task image must avoid unrelated writing voices")
    image_moves = set(image_recipe.get("moves", []))
    allowed_image_moves = {
        "replace quality tags with art direction",
        "make the use case explicit",
        "specify composition and text-safe space",
        "add concrete light and material constraints",
        "reduce decorative adjectives",
        "avoid readable generated text",
    }
    if not image_moves.issubset(allowed_image_moves):
        raise AssertionError(f"style_seed.py --task image emitted unrelated moves: {sorted(image_moves - allowed_image_moves)}")


def check_readme() -> None:
    body = read(ROOT / "README.md")
    for phrase in [
        "# Humanize AI Output Skill",
        "中文",
        "English",
        "Install",
        "Before / After",
        "Ethics",
        "Evaluation",
        "humanize-ai-output",
    ]:
        require(body, phrase, "README coverage")
    for placeholder in ["<owner>", "<your", "YOUR_GITHUB_USERNAME"]:
        if placeholder.lower() in body.lower():
            raise AssertionError(f"README still contains publication placeholder: {placeholder}")


def check_evals() -> None:
    prompts = read(ROOT / "evals" / "prompts.md")
    report = read(ROOT / "evals" / "test-report.md")
    rubric = read(ROOT / "evals" / "rubric.md")

    for category in [
        "Chinese writing naturalization",
        "English and bilingual polish",
        "PPT and document de-templating",
        "Image prompt de-AI-styling",
    ]:
        require(prompts, category, "prompt category")
        require(report, category, "report category")

    require_count(report, r"^### Case \d+", 10, "evaluation cases")
    require_count(report, r"\*\*Baseline AI-ish output\*\*", 10, "baseline outputs")
    require_count(report, r"\*\*Humanized output\*\*", 10, "humanized outputs")
    require(report, "Iteration 1", "iteration log")
    require(report, "Iteration 2", "iteration log")
    require(rubric, "Meaning preservation", "rubric criterion")
    require(rubric, "Template reduction", "rubric criterion")


def check_openai_yaml() -> None:
    body = read(SKILL / "agents" / "openai.yaml")
    for phrase in [
        'display_name: "Humanize AI Output"',
        "short_description:",
        "$humanize-ai-output",
    ]:
        require(body, phrase, "agents/openai.yaml")


def check_publication_metadata() -> None:
    license_body = read(ROOT / "LICENSE")
    require(license_body, "Copyright (c) 2026 zhaoyun", "license holder")


def main() -> int:
    checks = [
        check_skill_metadata,
        check_references,
        check_scripts,
        check_readme,
        check_evals,
        check_openai_yaml,
        check_publication_metadata,
    ]
    for check in checks:
        check()
    print("Release checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
