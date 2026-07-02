#!/usr/bin/env python3
"""Generate a variation recipe for humanize-ai-output."""

from __future__ import annotations

import argparse
import json
import random
from datetime import datetime, timezone


VOICES = [
    "concise practical",
    "conversational professional",
    "editorial",
    "warm explanatory",
    "sharp executive",
    "loose draft",
    "visual director",
    "document editor",
]

TASK_VOICES = {
    "chinese": ["concise practical", "conversational professional", "editorial", "warm explanatory", "sharp executive"],
    "english": ["concise practical", "conversational professional", "editorial", "sharp executive"],
    "bilingual": ["conversational professional", "editorial", "sharp executive"],
    "ppt": ["sharp executive", "document editor"],
    "document": ["concise practical", "sharp executive", "document editor"],
    "image": ["visual director", "document editor"],
}

OPENINGS = [
    "direct finding",
    "scene detail",
    "problem tension",
    "decision first",
    "user pain",
    "concrete next step",
]

RHYTHMS = [
    "short lines",
    "mixed paragraph lengths",
    "one expanded paragraph",
    "memo bullets",
    "tight executive note",
]

MOVES = [
    "cut generic opening",
    "replace forced contrast",
    "turn abstractions into actions",
    "vary sentence length",
    "add grounded detail from source",
    "make the audience explicit",
    "name the deciding variable",
    "reduce decorative adjectives",
    "add layout hierarchy",
]

TASK_MOVES = {
    "chinese": [
        "replace forced contrast",
        "turn abstractions into actions",
        "vary sentence length",
        "add grounded detail from source",
        "make the audience explicit",
        "name the deciding variable",
    ],
    "english": [
        "cut generic opening",
        "turn abstractions into actions",
        "vary sentence length",
        "add grounded detail from source",
        "make the audience explicit",
        "name the deciding variable",
    ],
    "bilingual": [
        "smooth language mixing",
        "replace translationese",
        "make the audience explicit",
        "vary sentence length",
        "preserve domain terms",
        "turn abstractions into actions",
    ],
    "ppt": [
        "add layout hierarchy",
        "turn topic titles into claims",
        "make one takeaway dominant",
        "replace bullets with action rows",
        "add source and baseline to metrics",
        "cut decorative structure",
    ],
    "document": [
        "cut generic opening",
        "turn section titles into claims",
        "add owner/action/deadline details",
        "make the audience explicit",
        "vary paragraph weight",
        "preserve citations and terms",
    ],
    "image": [
        "replace quality tags with art direction",
        "make the use case explicit",
        "specify composition and text-safe space",
        "add concrete light and material constraints",
        "reduce decorative adjectives",
        "avoid readable generated text",
    ],
}


def build_recipe(seed: int | None = None, task: str | None = None) -> dict[str, object]:
    rng = random.Random(seed)
    voices = TASK_VOICES.get(task, VOICES)
    moves = TASK_MOVES.get(task, MOVES)
    return {
        "seed": seed,
        "task": task or "general",
        "voice": rng.choice(voices),
        "opening": rng.choice(OPENINGS),
        "rhythm": rng.choice(RHYTHMS),
        "intervention_strength": rng.choice(["light polish", "medium rewrite", "heavy restructure"]),
        "moves": rng.sample(moves, min(4, len(moves))),
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a style variation recipe.")
    parser.add_argument("--seed", type=int, help="Optional deterministic seed.")
    parser.add_argument(
        "--task",
        choices=sorted(TASK_VOICES),
        help="Optional task type for a better-matched style pool.",
    )
    parser.add_argument("--text", help="Optional source text. Accepted for workflow convenience; not analyzed.")
    args = parser.parse_args()
    print(json.dumps(build_recipe(args.seed, args.task), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
