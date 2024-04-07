from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from schemas.layer import LayerCreate, LayerShow
from db.repository.layer import create_new_layer,get_layer
from db.session import get_db

router = APIRouter()

@router.post("/layers/", response_model=LayerShow, status_code=status.HTTP_201_CREATED)
def add_layer(layer_data: LayerCreate, db: Session = Depends(get_db)):
    """
    Добавить новый слой.
    """
    try:
        new_layer = create_new_layer(layer_data=layer_data, db=db)
        return new_layer
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ошибка при создании слоя: {e}")


@router.get("/layer/{layer_id}", response_model=LayerShow, status_code=status.HTTP_200_OK)
def read_layer(layer_id: int, db: Session = Depends(get_db)):
    """
       Получить слой.
       """
    layer = get_layer(db=db, layer_id=layer_id)
    if not layer:
        raise HTTPException(status_code=404, detail="Layer not found")
    return layer