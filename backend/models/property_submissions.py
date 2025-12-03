from datetime import datetime
from typing import Optional, List
from sqlmodel import Field, SQLModel, Column
from sqlalchemy import Text, ARRAY

class PropertySubmission(SQLModel, table=True):
    __tablename__ = "property_submissions"
    
    property_submission_id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.user_id")
    reference_number: str = Field(unique=True, max_length=100)
    language: Optional[str] = Field(default=None, max_length=50)
    currency: Optional[str] = Field(default=None, max_length=10)
    country: Optional[str] = Field(default=None, max_length=100)
    city: Optional[str] = Field(default=None, max_length=150)
    town_area: Optional[str] = Field(default=None, max_length=150)
    community: Optional[str] = Field(default=None, max_length=150)
    category: Optional[List[str]] = Field(default=None, sa_column=Column(ARRAY(Text)))
    subcategory: Optional[str] = Field(default=None, max_length=150)
    minimum_investment: Optional[float] = None
    maximum_investment: Optional[float] = None
    minimum_investment_aed: Optional[float] = None
    maximum_investment_aed: Optional[float] = None
    investment_objective: Optional[str] = Field(default=None, max_length=100)
    additional_notes: Optional[str] = None
    status: Optional[str] = Field(default=None, max_length=100)
    submitted_by_user_id: Optional[int] = Field(default=None, foreign_key="users.user_id")
    submitted_by_user_name: Optional[str] = Field(default=None, max_length=150)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)