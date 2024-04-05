from fastapi import APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends
from schemas.redemption_status import RedemptionStatusCreate,ShowStatus
from db.session import get_db
from typing import List
from db.repository.redemption_status import create_redemption_status

router = APIRouter()


@router.post("/redemption_status/", response_model=ShowStatus, status_code=status.HTTP_201_CREATED)
def add_redemption_status(status_data: RedemptionStatusCreate, db: Session = Depends(get_db)):
    """
    Создать новый статус выкупа.
    """
    try:
        new_status = create_redemption_status(status_data=status_data, db=db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ошибка при создании статуса выкупа: {e}")

    return new_status

