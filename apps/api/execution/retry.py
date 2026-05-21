import random
import time


RETRYABLE_ERRORS = (
    TimeoutError,
    ConnectionError,
)


class RetryExecutor:

    def __init__(
        self,
        executor,
        max_retries: int = 3,
        base_delay: float = 1.0,
    ):

        self.executor = executor
        self.max_retries = max_retries
        self.base_delay = base_delay

    def execute(self, fn, *args, **kwargs):

        last_error = None

        for attempt in range(self.max_retries):

            try:
                return fn(*args, **kwargs)

            except RETRYABLE_ERRORS as e:

                last_error = e

                if attempt == self.max_retries - 1:
                    break

                delay = (
                    self.base_delay
                    * (2 ** attempt)
                    + random.uniform(0, 0.5)
                )

                time.sleep(delay)

        raise last_error