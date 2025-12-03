from datetime import datetime
from typing import Optional, List
from sqlmodel import Field, SQLModel, Column
from sqlalchemy import Text, ARRAY


class KnowledgeHub(SQLModel, table=True):
    __tablename__ = "knowledge_hub"
    
    knowledge_hub_id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(max_length=255)
    category: Optional[str] = None
    content: Optional[str] = None
    attachments: Optional[List[str]] = Field(default=None, sa_column=Column(ARRAY(Text)))
    links: Optional[List[str]] = Field(default=None, sa_column=Column(ARRAY(Text)))
    visibility: str = Field(default="Both", max_length=20)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
