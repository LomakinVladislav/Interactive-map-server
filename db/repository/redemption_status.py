from sqlalchemy.orm import Session
from db.models.redemption_status import Redemption_status
from schemas.redemption_status import RedemptionStatusCreate

def create_redemption_status(status_data: RedemptionStatusCreate, db: Session):
    new_status = Redemption_status(**status_data.dict())
    db.add(new_status)
    db.commit()
    db.refresh(new_status)
    return new_status
