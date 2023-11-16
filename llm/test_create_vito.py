from .create_vito import CreateVito, VitoRequest

client = CreateVito()

vr = VitoRequest(linked_in_url="", company_url="")


class MockOpenAI:
    def invoke(_text):
        return vr


def test_create_vito(mocker):
    mocker.patch("llm.create_vito.llm", MockOpenAI)
    vito = client.create_vito(vr)
    assert vito == vr
