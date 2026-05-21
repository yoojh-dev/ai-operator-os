def test_tenant_isolation():

    tenant_a = create_workspace("A")
    tenant_b = create_workspace("B")

    set_context(tenant_a)
    executor.execute(...)

    set_context(tenant_b)
    executor.execute(...)

    assert tenant_a.memory != tenant_b.memory