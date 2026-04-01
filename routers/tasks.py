from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, selectinload
from sqlalchemy import select, func
from typing import Annotated
import uuid

from database import get_db
from models import User, Task
from schemas import TaskCreate, TaskResponse, Pagination, TaskResponseWithUser
from core import get_current_user

router = APIRouter(prefix="/tasks", tags=["tasks"])


# create task
@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Annotated[Session, Depends(get_db)], current_user: Annotated[User, Depends(get_current_user)]):
    new_task = Task(title=task.title, description=task.description, user_id=current_user.id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


# get tasks with pagination
@router.get("/", response_model=Pagination)
def get_tasks(db: Annotated[Session, Depends(get_db)],
              page: int = 1, limit: int = 10):
    offset = (page - 1) * limit
    res = db.execute(select(Task).options(selectinload(Task.user)).offset(offset).limit(limit))
    tasks = res.scalars().all()
    total = db.execute(select(func.count(Task.id))).scalar()
    return Pagination(items=tasks, total=total, page=page, size=limit)


# get only my tasks
@router.get("/me", response_model=list[TaskResponse])
def get_my_tasks(db: Annotated[Session, Depends(get_db)], current_user: Annotated[User, Depends(get_current_user)]):
    res = db.execute(select(Task).where(Task.user_id == current_user.id))
    return res.scalars().all()


# get a task with user info
@router.get("/{task_id}", response_model=TaskResponseWithUser)
def get_task(task_id: uuid.UUID, db: Annotated[Session, Depends(get_db)]):
    res = db.execute(select(Task).options(selectinload(Task.user)).where(Task.id == task_id))
    task = res.scalars().first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


# update task
@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: uuid.UUID, task: TaskCreate,
                db: Annotated[Session, Depends(get_db)], current_user: Annotated[User, Depends(get_current_user)]):
    res = db.execute(select(Task).where(Task.id == task_id))
    existing = res.scalars().first()
    if existing is None:
        raise HTTPException(status_code=404, detail="Task not found")
    if existing.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this task")
    existing.title = task.title
    existing.description = task.description
    existing.completed = task.completed
    db.commit()
    db.refresh(existing)
    return existing


# delete task
@router.delete("/{task_id}")
def delete_task(task_id: uuid.UUID, db: Annotated[Session, Depends(get_db)], current_user: Annotated[User, Depends(get_current_user)]):
    res = db.execute(select(Task).where(Task.id == task_id))
    existing = res.scalars().first()
    if existing is None:
        raise HTTPException(status_code=404, detail="Task not found")
    if existing.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this task")
    db.delete(existing)
    db.commit()
    return {"detail": "Task deleted successfully!"}