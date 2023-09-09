from pydantic import BaseModel


class Status(BaseModel):
    """ Status class """
    status: str = "ok"
    