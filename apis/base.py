from fastapi import APIRouter
from apis.v1 import route_redemption_status
from apis.v1 import route_object
from apis.v1 import route_boundaries
from apis.v1 import route_layer

api_router = APIRouter()
api_router.include_router(route_redemption_status.router, prefix = "", tags = ["redemption_status"])
api_router.include_router(route_object.router,prefix="",tags=["object"])
api_router.include_router(route_layer.router,prefix="",tags=["layer"])
api_router.include_router(route_boundaries.router,prefix="",tags=["boundaries"])


