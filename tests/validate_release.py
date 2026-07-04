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
PENALTY_THRESHOLD = 95

PENALTY_PATTERNS = [
    (
        "CN_FORCED_CONTRAST",
        "Chinese forced contrast",
        r"不是[^。；\n]{1,80}而是|是[^。；\n]{1,80}而不是|问题不在[^。；\n]{1,80}而在",
        40,
    ),
    (
        "CN_NEGATIVE_FIRST",
        "Chinese negative-first advice",
        r"(^|[。！？\n])\s*(先别|不建议|不需要|不要)[^。！？\n]{1,80}",
        25,
    ),
    (
        "EN_BROAD_NEGATIVE_CONTRAST",
        "English broad negative contrast",
        r"\bnot\b[^.\n]{1,100}\b(?:but|rather than)\b",
        40,
    ),
    (
        "EN_TRAILING_NOT_FRAME",
        "English trailing not-frame",
        r",\s*not\s+[A-Za-z][^.\n]{1,100}",
        35,
    ),
    (
        "EN_NOT_ALONE",
        "English not-alone contrast",
        r"\bnot\b[^.\n]{0,80}\balone\b",
        35,
    ),
    (
        "COLON_LED_EXPLANATION",
        "Colon-led explanation",
        r"(?mi)^\s*(?:[-*]\s*)?(?:\*\*)?(?:标题|问题|指标|背景|挑战|策略|展望|痛点|方案|价值|负责人|decision needed|slide title|next question|question|metric|problem|strategy|value|background|challenge)\s*[:：]\s*[^:\n：]+",
        20,
    ),
    (
        "QUOTED_LABEL",
        "Quoted framing label",
        r"[\"“][^\"”\n]{2,50}[\"”]",
        10,
    ),
    (
        "PLUS_STACK",
        "Plus-stack shorthand",
        r"\S+\s*\+\s*\S+\s*\+\s*\S+",
        15,
    ),
    (
        "NEGATIVE_TITLE",
        "Negative-first title",
        r"(?mi)^\s*(?:#+\s*)?(?:\*\*)?(?:先别|不建议|不需要|不要|don't|do not)\b",
        30,
    ),
]


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


def extract_humanized_blocks(text: str, label: str) -> list[str]:
    blocks = [
        match.group("body").strip()
        for match in re.finditer(
            r"\*\*Humanized output\*\*\s*\n\n(?P<body>.*?)(?=\n\n\*\*(?:Score|What changed|Notes)\*\*|\n### Case|\n## Case|\Z)",
            text,
            flags=re.DOTALL,
        )
    ]
    if not blocks:
        raise AssertionError(f"No humanized output blocks found in {label}")
    return blocks


def penalty_score(text: str) -> tuple[int, list[str]]:
    penalty = 0
    details: list[str] = []
    for code, label, pattern, weight in PENALTY_PATTERNS:
        count = len(re.findall(pattern, text, flags=re.IGNORECASE | re.DOTALL | re.MULTILINE))
        if count:
            penalty += count * weight
            details.append(f"{code}={count} ({label}, -{count * weight})")
    return max(0, 100 - penalty), details


def require_humanized_penalty_gate(text: str, label: str) -> None:
    for index, block in enumerate(extract_humanized_blocks(text, label), start=1):
        score, details = penalty_score(block)
        if score < PENALTY_THRESHOLD:
            joined = "; ".join(details)
            preview = block.replace("\n", " ")[:180]
            raise AssertionError(
                f"{label} humanized block {index} penalty score {score} is below "
                f"{PENALTY_THRESHOLD}: {joined}. Preview: {preview}"
            )


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
        "Penalty gate",
        "95",
        "revise and rerun",
    ]:
        require(body, phrase, "AI-ish pattern coverage")


def check_references() -> None:
    references = {
        "chinese-style-patterns.md": ["不是", "而是", "口语", "连接", "口语颗粒感"],
        "english-bilingual-patterns.md": ["bilingual", "translationese", "rhythm", "editor-like"],
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

    clean_lint = subprocess.run(
        [sys.executable, str(SKILL / "scripts" / "ai_tone_lint.py"), "--score"],
        input="Customer workflow depth is the current advantage.",
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if clean_lint.returncode != 0:
        raise AssertionError(f"ai_tone_lint.py --score must pass clean text: {clean_lint.stderr or clean_lint.stdout}")
    clean_payload = json.loads(clean_lint.stdout)
    if clean_payload.get("score") != 100 or clean_payload.get("passed") is not True:
        raise AssertionError(f"ai_tone_lint.py --score must return a passing score for clean text: {clean_payload}")

    bad_lint = subprocess.run(
        [sys.executable, str(SKILL / "scripts" / "ai_tone_lint.py"), "--score"],
        input="Our current advantage is customer workflow depth, not model capability alone.",
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if bad_lint.returncode == 0:
        raise AssertionError("ai_tone_lint.py --score must fail broad trailing not-frames")
    bad_payload = json.loads(bad_lint.stdout)
    if bad_payload.get("score", 100) >= PENALTY_THRESHOLD:
        raise AssertionError(f"ai_tone_lint.py --score must penalize broad trailing not-frames: {bad_payload}")

    bad_cn_lint = subprocess.run(
        [sys.executable, str(SKILL / "scripts" / "ai_tone_lint.py"), "--score"],
        input="问题不在获客，而在客户试用后的第一周。",
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if bad_cn_lint.returncode == 0:
        raise AssertionError("ai_tone_lint.py --score must fail Chinese problem-not-in frames")
    bad_cn_payload = json.loads(bad_cn_lint.stdout)
    if bad_cn_payload.get("score", 100) >= PENALTY_THRESHOLD:
        raise AssertionError(f"ai_tone_lint.py --score must penalize Chinese problem-not-in frames: {bad_cn_payload}")


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
    review = read(ROOT / "evals" / "review-feedback-2026-07-04.md")

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
    require(report, "Iteration 3", "iteration log")
    require(report, "Iteration 4", "iteration log")
    require(report, "Iteration 5", "iteration log")
    require(report, "Iteration 6", "iteration log")
    for phrase in [
        "Penalty Gate Result",
        "Threshold: 95",
        "Forced Chinese contrast: 0",
        "Problem-not-in frame: 0",
        "Trailing not-frame: 0",
        "Colon-led label explanation: 0",
        "All accepted humanized outputs scored at least 95",
    ]:
        require(report, phrase, "penalty gate report")
    for phrase in [
        "本周主要我们推进有三件事",
        "支付回调现在卡在风控规则上",
        "测试包可能就要顺延一天",
        "我今天会把待确认项列给财务和风控",
        "现在呢我只保留一个动作",
        "总之自律呢，一来不要只追求热血，重复、坚持才是最重要的",
        "这次耽误的时间我们会来承担，以免让您再来回沟通",
        "行业 beta现在可能不合适了，要看看这些订单能否从试点进入批量交付",
        "那么估值上就很难继续给溢价",
        "Retention features should lead the next segment plan",
        "Customer workflow depth is the current advantage.",
        "过去三个月，销售线索保持稳定，但从试用到付费的转化明显变慢",
        "客户试用后的第一周需要重点梳理",
        "后续分工也先这样定",
        "The useful signal now is whether those 12 design partners keep using the review workflow",
        "I work on AI product workflows for teams trying to cut manual review",
        "Even if the date is still moving",
        "Operations teams get one place to track approvals, files, and status updates",
        "New feature work can wait.",
        "actually adopted",
        "instead of chasing context across tools",
    ]:
        require(report, phrase, "preferred humanized phrasing")

    for phrase in [
        "# Review Feedback Cases - 2026-07-04",
        "## Forbidden Structures",
        "Do not open with a negative contrast before the positive claim.",
        "Avoid quoted framing labels as the main explanation.",
        "Avoid colon-led explanation sentences when a direct sentence works.",
        "寻找进度卡壳点",
        "构建持续重复工作流程",
        "30天重点关注指标—交接消耗时间",
        "该指标应是重点优先关注对象，或许比一昧接入AI工具更能提升效率",
        "Next step we should focus on whether teams come back to the workflow after the first try",
        "Operations teams get one place to track approvals, files, and status updates",
    ]:
        require(review, phrase, "review feedback eval coverage")

    for forbidden in [
        "does not need the",
        "The old AI product innovation line is doing too much work",
        "The beta headline probably is not the useful framing anymore",
        "标题：先别",
        "第一阶段不建议",
        "30 天内只看一个指标：",
        "Our current advantage is customer workflow depth, not model capability alone",
        "Decision needed:",
        "问题不在获客，而在客户试用后的第一周：",
    ]:
        if forbidden.lower() in review.lower() or forbidden.lower() in report.lower():
            raise AssertionError(f"Forbidden reviewed structure remains: {forbidden}")
    require_humanized_penalty_gate(report, "evals/test-report.md")
    require_humanized_penalty_gate(review, "evals/review-feedback-2026-07-04.md")
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
