from .create_vito import CreateVito, VitoRequest

client = CreateVito()

vr = VitoRequest(linked_in_url="", company_url="")


def test_create_vito():
    vito = client.create_vito(vr)
    assert vito == vr
