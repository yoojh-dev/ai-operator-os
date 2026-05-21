from apps.api.core.logging import log_event
from apps.api.core.exceptions import FallbackExhausted

from apps.api.providers.litellm_provider import ProviderRegistry
from apps.api.execution.agent_loop import AgentLoop
from apps.api.execution.stream_agent_loop import StreamAgentLoop

from apps.api.safety.sandbox import Sandbox
from apps.api.safety.policy_engine import PolicyEngine
from apps.api.safety.tool_guard import ToolGuard

from apps.api.tenancy.tenant_context import TenantContext
from apps.api.tenancy.quota_manager import QuotaManager

from apps.api.deployment.traffic_splitter import TrafficSplitter

from apps.api.schemas.llm_contract import LLMContract


class ModelExecutor:

    def __init__(self):

        self.provider_registry = ProviderRegistry()

        self.sandbox = Sandbox()
        self.policy = PolicyEngine()
        self.tool_guard = ToolGuard()

        self.quota = QuotaManager()
        self.traffic = TrafficSplitter(rollout_rate=0.3)

    def execute(
        self,
        request_id: str,
        selected_model: str,
        fallbacks: list[str],
        messages: list,
        stream: bool = False,
        tools=None,
        user_id: str | None = None,
    ) -> LLMContract:

        workspace = TenantContext.get()
        candidate_models = [selected_model] + fallbacks
        last_error = None

        if user_id and not self.traffic.allow():
            raise Exception("Traffic limit")

        self.quota.check(workspace.workspace_id)

        self.sandbox.validate({
            "step_count": len(messages),
            "tool_calls": len(tools or []),
        })

        if not self.policy.check({
            "messages": messages,
            "tools": tools,
        }):
            raise Exception("Policy violation")

        for model in candidate_models:

            try:

                provider = self.provider_registry.get_provider(model)

                if stream:

                    contract: LLMContract = StreamAgentLoop(provider).run(
                        model=model,
                        messages=messages,
                        tools=tools,
                    )

                    return contract

                contract: LLMContract = AgentLoop(provider).run(
                    model=model,
                    messages=messages,
                    tools=tools,
                )

                self.quota.record(
                    workspace.workspace_id,
                    tokens=contract.usage.get("total_tokens", 0),
                )

                return contract

            except Exception as e:

                last_error = e
                log_event("execution_failed", error=str(e))

        raise FallbackExhausted(str(last_error))