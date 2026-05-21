def test_e2e_cognitive_flow():

    validator = CognitiveValidator(executor, planner, trace_store)

    output = validator.run_e2e("hello world")

    assert output["plan"] is not None
    assert output["result"] is not None
    assert len(output["trace"]) > 0