from fastapi import APIRouter
from apis.v1 import route_redemption_status
from apis.v1 import route_object
from apis.v1 import route_boundaries
from apis.v1 import route_layer
from apis.v1 import route_city_and_project
from apis.v1 import  route_object_type


api_router = APIRouter()
api_router.include_router(route_city_and_project.router,prefix="",tags=["city_and_project"])
api_router.include_router(route_object_type.router,prefix="",tags=["object_type"])
api_router.include_router(route_redemption_status.router, prefix = "", tags = ["redemption_status"])
api_router.include_router(route_object.router,prefix="",tags=["object"])
api_router.include_router(route_layer.router,prefix="",tags=["layer"])
api_router.include_router(route_boundaries.router,prefix="",tags=["boundaries"])


