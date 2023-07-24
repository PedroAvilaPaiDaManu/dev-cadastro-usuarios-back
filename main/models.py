from pydantic import BaseModel


class User(BaseModel):
    email: str
    name: str
    last_name: str
    phone: str
    uf: str
    cep: str
    city: str
    age: int
