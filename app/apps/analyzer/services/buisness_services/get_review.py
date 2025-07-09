from fastapi import HTTPException, status

from app.apps.analyzer.schemas.models.review import ReviewResponseSchema
from app.apps.analyzer.schemas.request.review import SJBFilterInput
from app.apps.analyzer.services.infrastructure_services.review_service import ReviewService


async def get_review(
        data:SJBFilterInput,
        review_service: ReviewService = ReviewService()
):
    try:
        reviews = await review_service.get_reviews(data)
        print(reviews)
        return [
            ReviewResponseSchema(
                id=r.id,
                text=r.text,
                sentiment=r.sentiment,
                created_at=r.created_at,
            )
            for r in reviews
        ]

    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) from e

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Something went wrong") from e
