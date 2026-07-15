# PLAN: DummyDataGenerator

> 이 문서는 구현이 진행됨에 따라 갱신되는 living document입니다. 실제 구현 중 발견된 이슈나 구조 변경 사항을 반영해 계속 업데이트합니다.

## 1. 목적

테스트를 위한 Dummy Data를 생성하여 연결된 DB에 추가하는 도구를 검증하는 PoC.

## 2. 영속성 연동 방식

- `DataPersistence` PoC와 동일한 방식인 SQLite에 삽입한다. 이 repo는 독립 실행 가능해야 하므로 자체 스키마 초기화 로직을 포함한다.
- DB 파일 경로: `data/app.db`.

## 3. 데모 도메인: Item(품목)

`DataPersistence`/`DataMonitor`와 동일한 스키마(`id`, `name`, `quantity`)를 사용한다.

## 4. 폴더 구조

```
src/
  db.py        # DB 연결 및 스키마 초기화
  generator.py # 더미 데이터 생성 로직 (random 모듈 사용)
  main.py      # CLI 진입점 (--count 인자로 생성 개수 지정)
tests/
  test_generator.py
```

## 5. 구현 단계

- [ ] 1단계 - `db.py`: SQLite 연결 함수, 테이블 없을 시 자동 생성.
- [ ] 2단계 - `generator.py`: 랜덤 이름/수량을 가진 Item 더미 데이터 N개 생성하는 순수 함수 (DB 접근과 분리, 테스트 용이성 확보).
- [ ] 3단계 - `main.py`: `argparse`로 `--count` 인자를 받아 생성된 더미 데이터를 DB에 삽입, 삽입 건수 요약 출력.
- [ ] 4단계 - `tests/test_generator.py`: 생성 함수의 개수/필드 유효성 단위 테스트 (DB 접근 없이 순수 로직만 검증).

## 6. 완료 기준 (Definition of Done)

- `python -m src.main --count 50` 실행 시 50건이 `data/app.db`에 삽입된다.
- 반복 실행 시 기존 데이터에 **누적 삽입**된다 (덮어쓰지 않음).
- 생성 로직(순수 함수)과 DB 삽입 로직이 분리되어 있어 생성 로직만 단독 테스트 가능하다.
- `pytest` 전체 통과.

## 7. 미결정/추후 논의 사항

- (없음, 발견 시 추가)
