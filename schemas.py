from pydantic import BaseModel, Field, ConfigDict
import uuid



class UserBase(BaseModel):
    username: str = Field(min_length=1, max_length=50)
    
    model_config = ConfigDict(from_attributes=True)

class UserCreate(UserBase):
    password: str = Field(min_length=8)
    
class UserResponse(UserBase):
    id: uuid.UUID
    
    
class UserSimple(UserBase):
    id: uuid.UUID
    



class TaskBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str | None = None
    completed: bool = False
    
    model_config = ConfigDict(from_attributes=True)

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: uuid.UUID
    user_id: uuid.UUID
    
class TaskResponseWithUser(TaskResponse):
    id: uuid.UUID
    user: UserSimple




class Pagination(BaseModel):
    items: list["TaskResponseWithUser"]
    total: int
    page: int = Field(1, ge=1)
    size: int = Field(10, ge=1, le=100)
    
    model_config = ConfigDict(from_attributes=True)