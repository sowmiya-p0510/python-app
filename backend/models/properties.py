from datetime import date, datetime
from typing import Optional, List
from sqlmodel import Field, SQLModel, Column
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import Text, ARRAY

class Property(SQLModel, table=True):
    __tablename__ = "properties"
    
    property_id: Optional[int] = Field(default=None, primary_key=True)
    property_submission_id: int = Field(foreign_key="property_submissions.property_submission_id")
    external_property_id: Optional[str] = Field(default=None, max_length=100)
    is_available: bool = Field(default=True)
    
    # Property details
    title: Optional[str] = Field(default=None, max_length=100)
    property_name: Optional[str] = Field(default=None, max_length=300)
    building_name: Optional[str] = Field(default=None, max_length=255)
    category: Optional[str] = Field(default=None, max_length=255)
    property_type: Optional[str] = Field(default=None, max_length=255)
    purpose: Optional[str] = Field(default=None, max_length=255)
    bedrooms: Optional[int] = None
    bathrooms: Optional[int] = None
    property_description: Optional[str] = None
    amenities: Optional[List[str]] = Field(default=None, sa_column=Column(ARRAY(Text)))
    dld_number: Optional[str] = Field(default=None, max_length=255)
    
    # Location
    city: Optional[str] = Field(default=None, max_length=100)
    community: Optional[str] = Field(default=None, max_length=150)
    subcommunity: Optional[str] = Field(default=None, max_length=150)
    tower: Optional[str] = Field(default=None, max_length=150)
    display_address: Optional[str] = None
    
    # Coordinates
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    
    # Size
    size: Optional[float] = None
    size_unit: Optional[str] = Field(default=None, max_length=20)
    
    # Pricing
    price_aed: Optional[float] = None
    price_currency: Optional[str] = Field(default="AED", max_length=10)
    preferred_currency: Optional[str] = Field(default=None, max_length=10)
    preferred_price: Optional[float] = None
    
    # Sales agent
    agent_name: Optional[str] = Field(default=None, max_length=150)
    agent_email: Optional[str] = Field(default=None, max_length=255)
    agent_contact_number: Optional[str] = Field(default=None, max_length=20)
    agent_address: Optional[str] = None
    
    # Developer details
    developer_name: Optional[str] = Field(default=None, max_length=150)
    developer_brand: Optional[str] = Field(default=None, max_length=255)
    development_location: Optional[str] = Field(default=None, max_length=255)
    development_category: Optional[str] = Field(default=None, max_length=255)
    
    # Status
    completion_status: Optional[str] = Field(default=None, max_length=50)
    is_furnished: Optional[str] = Field(default=None, max_length=50)
    
    # Additional info
    rental_availability_date: Optional[date] = None
    listing_level: Optional[str] = Field(default=None, max_length=100)
    is_new_insert: bool = Field(default=False)
    
    # Market data (JSONB fields)
    similar_transactions: Optional[dict] = Field(default=None, sa_column=Column(JSONB))
    payment_plans: Optional[dict] = Field(default=None, sa_column=Column(JSONB))
    immigration_eligibility: Optional[dict] = Field(default=None, sa_column=Column(JSONB))

    # Market Trend analysis
    price_analysis: Optional[dict] = Field(default=None, sa_column=Column(JSONB))
    projected_yearly_prices: Optional[dict] = Field(default=None, sa_column=Column(JSONB))
    rental_income: Optional[dict] = Field(default=None, sa_column=Column(JSONB))
    rental_yearly_analysis: Optional[dict] = Field(default=None, sa_column=Column(JSONB))
    neighbourhood_data: Optional[dict] = Field(default=None, sa_column=Column(JSONB))
    
    risk_rating: Optional[str] = Field(default=None, max_length=20)
    recommendation: Optional[str] = Field(default=None, max_length=20)
    ai_forecast_3year: Optional[str] = None
    ai_forecast_5year: Optional[str] = None

    # Map details
    map_language: str = Field(max_length=10)
    map_path: str

    # Images
    image_list: Optional[List[str]] = Field(default=None, sa_column=Column(ARRAY(Text)))
    
    # Timestamps
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)