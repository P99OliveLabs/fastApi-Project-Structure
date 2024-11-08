from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import List, Optional
from app.models.user import User, UserCreate, UserUpdate
from app.database.database import UserDatabaseAdapter
from config.settings import settings

# SQLAlchemy Base model (imported if needed elsewhere)
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Create the database URL dynamically using the configuration from `settings.py`
DATABASE_URL = (
    f"mysql+pymysql://{settings.DB_USER}:{settings.DB_PASSWORD}"
    f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
)

# Create the database engine
engine = create_engine(DATABASE_URL, echo=True)

# SessionLocal is a factory for creating new SQLAlchemy session objects
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get a database session
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# RealUserDBAdapter implementation
class RealUserDBAdapter(UserDatabaseAdapter):
    def __init__(self, db: Session):
        self.db = db

    async def get_all_users(self) -> List[User]:
        """Fetch all users from the database."""
        return self.db.query(User).all()

    async def get_user_by_id(self, user_id: int) -> Optional[User]:
        """Fetch a single user by their ID."""
        return self.db.query(User).filter(User.id == user_id).first()

    async def add_user(self, user: UserCreate) -> User:
        """Add a new user to the database."""
        new_user = User(**user.dict())
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    async def update_user(self, user_id: int, user: UserUpdate) -> Optional[User]:
        """Update an existing user in the database."""
        existing_user = self.db.query(User).filter(User.id == user_id).first()
        if existing_user:
            for key, value in user.dict().items():
                setattr(existing_user, key, value)
            self.db.commit()
            self.db.refresh(existing_user)
            return existing_user
        return None

    async def delete_user(self, user_id: int) -> bool:
        """Delete a user from the database by their ID."""
        existing_user = self.db.query(User).filter(User.id == user_id).first()
        if existing_user:
            self.db.delet
