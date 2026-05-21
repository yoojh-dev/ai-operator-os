from fastapi import FastAPI
from apps.api.api.v1.chat import router as chat_router

from apps.api.planning.planner_v3 import PlannerV3
from apps.api.execution.runtime.execution_kernel import ExecutionKernel
from apps.api.tools.runtime.executor import ToolExecutor
from apps.api.observability.trace_logger import TraceLogger
from apps.api.observability.trace_store import TraceStore
from apps.api.memory.memory_system import MemorySystem

app = FastAPI()

# core dependencies
trace_store = TraceStore()
trace_logger = TraceLogger(trace_store)

tool_executor = ToolExecutor(
    registry=tool_registry,
    event_emitter=event_emitter
)

planner = PlannerV3(memory=None)

kernel = ExecutionKernel(
    tool_executor=tool_executor,
    event_emitter=event_emitter
)

memory_system = MemorySystem(
    vector_store=vector_store,
    embedding_service=embedding_service,
    retriever=retriever,
    memory_graph=memory_graph
)

chat_service = ChatService(
    planner=planner,
    kernel=kernel,
    memory_system=memory_system
)

app.state.chat_service = chat_service

app.include_router(chat_router)