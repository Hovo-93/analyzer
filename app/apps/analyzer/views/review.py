from fastapi import APIRouter, Depends
from starlette import status

from app.apps.analyzer.schemas.models.review import ReviewResponseSchema
from app.apps.analyzer.schemas.request.review import SJBFilterInput, SJBReviewInput
from app.apps.analyzer.services.buisness_services.create_review import create_review
from app.apps.analyzer.services.buisness_services.get_review import get_review

router = APIRouter()


@router.post("/review",
             response_model=ReviewResponseSchema,
             status_code=status.HTTP_201_CREATED
)
async def create_review_view(
        data: SJBReviewInput
):
    response = await create_review(data=data)
    return response


@router.get(
    "/review",
    response_model=list[ReviewResponseSchema],
    status_code=status.HTTP_200_OK,
)
async def get_review_view(
    data: SJBFilterInput = Depends()
):
    response = await get_review(data=data)
    return response
