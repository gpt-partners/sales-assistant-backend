from typing import Annotated

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class VitoRequest(BaseModel):
    linkedInUrl: Annotated[str, "the LinkedIn profile URL"]
    companyUrl: Annotated[str, "the URL of the company"]


@app.get("/")
def get_root():
    return {"status": "OK"}


@app.post("/vito")
def create_vito(vitoRequest: VitoRequest):
    return {"status": "OK"}
