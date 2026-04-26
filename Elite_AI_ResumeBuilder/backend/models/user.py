from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, JSON
from sqlalchemy.orm import relationship
from db.session import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(String, default=lambda: datetime.utcnow().isoformat())

    # Relationships
    profile = relationship("UserProfile", back_populates="user", uselist=False)

class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    full_name = Column(String)
    
    # AI Extracted Data
    extracted_skills = Column(JSON, default=list)
    experience_level = Column(String)
    suggested_learning_paths = Column(JSON, default=list)
    
    # Store the local path to the original CV PDF
    original_cv_path = Column(String)

    user = relationship("User", back_populates="profile")
