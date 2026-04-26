from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.session import get_db
from models.user import User, UserProfile
from schemas.user import UserCreate, UserResponse
from core.security import get_password_hash

router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if user exists
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
        
    # Create new user
    hashed_password = get_password_hash(user.password)
    new_user = User(email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    # Initialize empty profile
    profile = UserProfile(user_id=new_user.id)
    db.add(profile)
    db.commit()
    
    return new_user

# Note: In a complete implementation, add POST /login to return JWT tokens
