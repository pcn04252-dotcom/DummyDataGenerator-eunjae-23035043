import argparse
import sys

from src.db import get_connection, insert_items
from src.generator import generate_items


def parse_args(argv=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Dummy Item 데이터 생성기")
    parser.add_argument("--count", type=int, required=True, help="생성할 더미 데이터 개수")
    return parser.parse_args(argv)


def main(argv=None) -> None:
    sys.stdout.reconfigure(encoding="utf-8")

    args = parse_args(argv)
    items = generate_items(args.count)
    with get_connection() as conn:
        inserted = insert_items(conn, items)

    print(f"더미 데이터 {inserted}건을 삽입했습니다.")


if __name__ == "__main__":
    main()
