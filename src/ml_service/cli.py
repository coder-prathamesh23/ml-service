"""Stable CLI boundary for human use and automated jobs."""

import argparse
import json
import sys
from ml_service.domain import as_payload, classify


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Phase-0 deterministic risk scorer")
    parser.add_argument("--amount", type=float, required=True)
    parser.add_argument("--past-due", type=int, required=True, dest="past_due")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        result = classify(args.amount, args.past_due)
    except ValueError as exc:
        print(f"Input error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(as_payload(result), sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
