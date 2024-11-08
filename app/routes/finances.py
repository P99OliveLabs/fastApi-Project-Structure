from fastapi import APIRouter, HTTPException, status, Query
from pydantic import BaseModel
from typing import List
from app.models.finance import Finance  # Import the Finance model from the models package
from app.services.finance_service import get_all_finances, get_all_finances_paginated, add_finance  # Service functions
from app.constants import NO_FINANCES_FOUND,FINANCE_CREATION_FAILED

from fastapi import APIRouter, HTTPException, status

router = APIRouter()

# Define a Pydantic model for input validation
class FinanceCreate(BaseModel):
    amount: float
    category: str
    description: str

@router.get("/all", response_model=List[Finance])
async def get_all_finances_route():
    """
    Fetch all financial records from the database without pagination.
    """
    finances = await get_all_finances()  # Function to return all financial records
    if not finances:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=NO_FINANCES_FOUND)
    return finances

@router.get("/paginated", response_model=List[Finance])
async def get_finances_paginated(page: int = Query(1, ge=1), size: int = Query(5, ge=1, le=100)):
    """
    Fetch a paginated list of financial records from the database.
    - `page`: The page number (1-based).
    - `size`: The number of records per page.
    """
    finances = await get_all_finances_paginated(page=page, size=size)
    if not finances:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=NO_FINANCES_FOUND)
    return finances

@router.post("/", response_model=Finance, status_code=status.HTTP_201_CREATED)
async def create_finance(finance: FinanceCreate):
    """Create a new financial record in the database."""
    created_finance = await add_finance(finance)
    if not created_finance:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=FINANCE_CREATION_FAILED)
    return created_finance
