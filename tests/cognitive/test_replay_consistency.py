def test_replay_consistency():

    trace_id = run_system()

    replay1 = replay_engine.replay(trace_id)
    replay2 = replay_engine.replay(trace_id)

    assert replay1 == replay2