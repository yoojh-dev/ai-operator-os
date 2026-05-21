from apps.api.schemas.llm_contract import LLMContract


class ContractAdapter:

    @staticmethod
    def from_response(response, model: str) -> LLMContract:

        if isinstance(response, dict):

            content = (
                response.get("choices", [{}])[0]
                .get("message", "")
            )

            return LLMContract(
                content=str(content),
                model=model,
                usage=response.get("usage", {}),
                raw=response,
            )

        return LLMContract(
            content=str(response),
            model=model,
            usage={},
            raw=response,
        )