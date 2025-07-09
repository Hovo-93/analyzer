from fastapi import APIRouter

from app.apps.analyzer.views.router import review_module_router

router = APIRouter()

router.include_router(review_module_router)
