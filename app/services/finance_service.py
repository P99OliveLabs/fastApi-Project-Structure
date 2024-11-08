from app.models.finance import FinanceCreate, Finance

# Sample in-memory database for demonstration
FAKE_DB = [
    Finance(id=1, amount=100.0, category="Groceries", description="Weekly grocery shopping"),
    Finance(id=2, amount=50.0, category="Transport", description="Bus pass"),
    Finance(id=3, amount=150.0, category="Utilities", description="Monthly electricity bill"),
    Finance(id=4, amount=200.0, category="Rent", description="Monthly rent payment"),
    Finance(id=5, amount=120.0, category="Dining", description="Dinner at a restaurant"),
    Finance(id=6, amount=30.0, category="Entertainment", description="Movie ticket"),
    Finance(id=7, amount=75.0, category="Gas", description="Fuel for the car"),
    Finance(id=8, amount=45.0, category="Subscriptions", description="Streaming service"),
    Finance(id=9, amount=60.0, category="Clothing", description="New shirt and pants"),
    Finance(id=10, amount=25.0, category="Snacks", description="Snacks for the week"),
    Finance(id=11, amount=180.0, category="Insurance", description="Monthly insurance payment"),
    Finance(id=12, amount=300.0, category="Travel", description="Weekend trip expenses"),
]

async def get_all_finances():
    """
    Return all financial records.
    """
    return FAKE_DB

async def get_all_finances_paginated(page: int, size: int):
    skip = (page - 1) * size
    limit = size
    finances = FAKE_DB[skip: skip + limit]  # Simulating pagination with list slicing
    if not finances:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No financial records found")
    return finances

async def add_finance(finance: FinanceCreate):
    # Simulate creating a financial record in the database
    new_id = len(FAKE_DB) + 1
    new_finance = Finance(id=new_id, amount=finance.amount, category=finance.category, description=finance.description)
    FAKE_DB.append(new_finance)
    return new_finance
