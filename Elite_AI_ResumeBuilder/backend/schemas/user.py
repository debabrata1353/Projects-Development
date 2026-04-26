from pydantic import BaseModel, EmailStr
from typing import Optional, List

# ----- Users -----
class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True

# ----- Profiles -----
class UserProfileBase(BaseModel):
    full_name: Optional[str] = None
    extracted_skills: Optional[List[str]] = []
    experience_level: Optional[str] = None
    suggested_learning_paths: Optional[List[str]] = []

class UserProfileUpdate(UserProfileBase):
    pass

class UserProfileResponse(UserProfileBase):
    id: int
    user_id: int
    original_cv_path: Optional[str] = None

    class Config:
        from_attributes = True
