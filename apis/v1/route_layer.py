from fastapi import APIRouter, HTTPException, status, Depends
from typing import List, Optional
from sqlalchemy.orm import Session,joinedload

from db.models.layer import Layer

from schemas.layer import LayerShow,LayerCreate
from schemas.boundaries import BoundariesShow
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
        raise HTTPException(status_code=404, detail="Слой не найден")
    return layer


class LayerWithBoundaries(LayerShow):
    boundaries: List[BoundariesShow]

    class Config:
        orm_mode = True

@router.get("/layers-with-boundaries/", response_model=List[LayerWithBoundaries], status_code=status.HTTP_200_OK)
def read_layers_with_boundaries(layer_id: Optional[int] = None, db: Session = Depends(get_db)):
    """
    Получать слои с их границами.
    """
    query = db.query(Layer).options(joinedload(Layer.boundaries))
    if layer_id is not None:
        layer = query.filter(Layer.id == layer_id).first()
        if not layer:
            raise HTTPException(status_code=404, detail="Координаты не найдены")
        return [layer]
    else:
        layers = query.all()
        return layers