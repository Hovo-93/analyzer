from fastapi import HTTPException, status

from app.apps.analyzer.schemas.models.review import ReviewResponseSchema
from app.apps.analyzer.schemas.request.review import SJBReviewInput
from app.apps.analyzer.services.infrastructure_services.review_service import ReviewService


async def create_review(
        data:SJBReviewInput,
        review_service: ReviewService = ReviewService()

):
    try:
        review = await review_service.create_review(data)
        return ReviewResponseSchema(
            id=review.id,
            text=review.text,
            sentiment=review.sentiment,
            created_at=review.created_at,
        )

    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) from e

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Something went wrong") from e


