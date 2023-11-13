from typing import Annotated

from pydantic import BaseModel


class VitoRequest(BaseModel):
    linked_in_url: Annotated[str, "the LinkedIn profile URL"]
    company_url: Annotated[str, "the URL of the company"]


class CreateVito:
    def __self__(self):
        pass

    def create_vito(self, vito_request: VitoRequest):
        return vito_request
