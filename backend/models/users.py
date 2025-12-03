from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    __tablename__ = "users"
    
    user_id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, max_length=255)
    full_name: str = Field(max_length=150)
    country_of_residence: Optional[str] = Field(default=None, max_length=100)
    city_of_residence: Optional[str] = Field(default=None, max_length=100)
    contact_number: Optional[str] = Field(default=None, max_length=20)
    contact_type: Optional[str] = Field(default=None, max_length=50)  # Mobile, WhatsApp
    company: Optional[str] = Field(default=None, max_length=255)
    website: Optional[str] = Field(default=None, max_length=255)
    created_by: Optional[int] = Field(
        default=None, 
        foreign_key="users.user_id",
        ondelete="SET NULL"
    )
    last_login: Optional[datetime] = None
    role: str = Field(max_length=50)
    is_approved: bool = Field(default=False)
    password: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
