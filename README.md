# Async Client Test

## Quick Start

```shell
# 의존성 설치
pip install -r requirements.txt
```

```shell
# 테스트 코드 수행
pytest -s
```

## 결론
동기냐 비동기냐 차이에 따라 성능 차이가 커진다.

재밌는 것은 코드 실행 순서에 따라, 성능에 차이를 보인다.

아래 결과 예시에선 1이 2보다 성능이 나쁜 것 처럼 보이지만, 순서를 바꾸면 결과도 달라진다.
클라이언트 인스턴스 숫자의 상관관계는 무시해도 될 정도라는 의미이다.
```text
test_async.py::test_ping1 PASSED                                         [ 25%]
test_ping1 - API 호출 시간: 6.1487250328063965

test_async.py::test_ping2 PASSED                                         [ 50%]
test_ping2 - API 호출 시간: 3.533263683319092

test_async.py::test_async_ping1 PASSED                                   [ 75%]
test_async_ping1 - API 호출 시간: 1.2908763885498047

test_async.py::test_async_ping2 PASSED                                   [100%]
test_async_ping2 - API 호출 시간: 1.0030231475830078
```