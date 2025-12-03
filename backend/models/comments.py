from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel

class Comment(SQLModel, table=True):
    __tablename__ = "comments"
    
    comment_id: Optional[int] = Field(default=None, primary_key=True)
    property_search_request_id: int = Field(foreign_key="property_submissions.property_submission_id")
    commented_by_user_id: Optional[int] = Field(default=None, foreign_key="users.user_id")
    commented_by_user_name: Optional[str] = Field(default=None, max_length=150)
    comment_text: str
    created_at: datetime = Field(default_factory=datetime.now)