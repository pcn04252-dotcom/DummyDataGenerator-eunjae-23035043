# CLAUDE.md

> 이 문서는 구현이 진행됨에 따라 갱신되는 living document입니다. 새 세션에서 이 repo를 열었을 때 아래 내용만으로 작업을 이어갈 수 있어야 합니다.

## 프로젝트 개요

테스트용 Dummy Data를 생성해 DB에 삽입하는 도구 PoC. 상세 계획은 `PLAN.md` 참고.

## 기술 스택

- Python 3.x + `sqlite3`, `random`, `argparse` (표준 라이브러리, 외부 의존성 없음)
- 테스트: `pytest` / 린트: `ruff` (설정은 `pyproject.toml`)
- CI: GitHub Actions (`.github/workflows/ci.yml`) — push/PR 시 `ruff check` + `pytest` 자동 실행

## 폴더 구조

```
src/db.py         # DB 연결/스키마 초기화
src/generator.py  # 더미 데이터 생성 (순수 함수, DB 비의존)
src/main.py       # CLI 진입점 (--count)
tests/
data/app.db       # 실제 데이터 (git 추적 제외)
```

## 실행 방법

```
python -m src.main --count 50
```

## 테스트 방법

```
pip install -r requirements-dev.txt
pytest
ruff check .
```

## 코드 컨벤션

- 더미 데이터 "생성" 로직(`generator.py`)과 "DB 삽입" 로직(`db.py`)을 분리한다 — 생성 함수는 DB 연결 없이 단독 테스트 가능해야 한다.
- `generate_items(count, rng=None)`처럼 `random.Random` 인스턴스를 파라미터로 주입받는다 — 테스트에서는 `rng=random.Random(seed)`로 재현 가능하게 호출한다.
- 타입 힌트를 사용한다.

## 주의사항

- 스키마는 `DataPersistence` repo와 동일한 설계 방향(Item: id/name/quantity)을 따르되, 코드/DB 파일을 직접 공유하지는 않는다.
- 실행할 때마다 기존 데이터에 누적 삽입되며, 삭제/초기화 기능은 이 PoC의 범위가 아니다.
- `main.py`에서 Windows 콘솔 기본 코드페이지(cp949) 한글 깨짐 방지를 위해 `sys.stdout.reconfigure(encoding="utf-8")` / `sys.stdin.reconfigure(encoding="utf-8")`를 적용한다 (`ConsoleMVC` PoC에서 확인된 이슈).
