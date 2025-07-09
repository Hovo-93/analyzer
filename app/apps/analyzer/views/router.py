from fastapi import APIRouter

from app.apps.analyzer.views.review import router as review_router

review_module_router = APIRouter(
    tags=["Review"],
)

review_module_router.include_router(
    review_router,
)

