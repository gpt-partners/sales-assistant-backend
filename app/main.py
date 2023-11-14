from fastapi import FastAPI

from llm.create_vito import CreateVito, VitoRequest

app = FastAPI()
client = CreateVito()


@app.get("/")
def get_root():
    return {"status": "OK"}


@app.post("/vito")
def create_vito(vitoRequest: VitoRequest):
    client.create_vito(vitoRequest)
    return {"status": "OK"}
