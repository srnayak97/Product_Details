from pydantic import BaseModel, Field
from typing import Optional


class ProductData(BaseModel):
    name: str
    price: int
    image: Optional[list] = Field(None)
    description: str

