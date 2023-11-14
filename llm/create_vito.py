from typing import Annotated

from dotenv import load_dotenv
from langchain.llms import OpenAI
from pydantic import BaseModel

load_dotenv()
llm = OpenAI()


class VitoRequest(BaseModel):
    linked_in_url: Annotated[str, "the LinkedIn profile URL"]
    company_url: Annotated[str, "the URL of the company"]


class CreateVito:
    def __self__(self):
        pass

    def create_vito(self, vito_request: VitoRequest):
        text = f"Send a message to {vito_request.linked_in_url} to ask for an introduction to {vito_request.company_url}"
        # return llm.invoke(text)
        return text
