from pydantic import BaseModel

# Model for financial record data returned to the client
class Finance(BaseModel):
    id: int
    amount: float
    category: str
    description: str

    class Config:
        orm_mode = True  # Enables ORM compatibility

# Model for finance creation (input data)
class FinanceCreate(BaseModel):
    amount: float
    category: str
    description: str
