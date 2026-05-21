import time
import uuid


class ExecutionSession:

    def __init__(self, tenant_id: str):

        self.session_id = str(uuid.uuid4())
        self.tenant_id = tenant_id

        self.created_at = time.time()
        self.trace_id = str(uuid.uuid4())

        self.metadata = {}

    def attach(self, key, value):

        self.metadata[key] = value