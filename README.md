# DummyDataGenerator

테스트용 Dummy Data를 생성하여 연결된 DB에 추가하는 도구 PoC 프로젝트입니다.

- 언어: Python (`sqlite3`, `random`, `argparse` 표준 라이브러리)
- 상태: 구현 완료
- 상세 계획: [`PLAN.md`](./PLAN.md), 세션 참고 문서: [`CLAUDE.md`](./CLAUDE.md)

## 실행 방법

```
python -m src.main --count 50
```

`data/app.db`에 더미 Item 데이터가 삽입되며, 반복 실행 시 기존 데이터에 누적됩니다.

## 테스트 방법

```
pip install -r requirements-dev.txt
pytest
```

## 검증한 것

- 더미 데이터 생성(순수 함수)과 DB 삽입 로직 분리, 생성 로직만 단독 테스트 가능
- `pytest` 5개 테스트 통과 (개수/필드 유효성/재현성/경계값)
- CLI로 5건 실행 후 3건 재실행 → 총 8건으로 누적 삽입되는 것 수동 검증 완료
