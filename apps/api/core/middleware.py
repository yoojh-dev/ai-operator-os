import time
import uuid

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request


class TraceMiddleware(BaseHTTPMiddleware):
    """
    Request tracing middleware

    역할:
    - request_id 생성
    - total request latency 측정
    - tracing context 저장
    - response header 추가
    """

    async def dispatch(self, request: Request, call_next):
        # 고유 request id 생성
        request_id = str(uuid.uuid4())

        # request 시작 시간
        start = time.time()

        # request context 저장
        request.state.request_id = request_id
        request.state.start_time = start

        # downstream 호출
        response = await call_next(request)

        # 전체 처리 시간 계산
        process_time = time.time() - start

        # response header 삽입
        response.headers["X-Request-ID"] = request_id
        response.headers["X-Response-Time"] = str(process_time)

        return response