from sqlalchemy import select

from app.apps.analyzer.schemas.request.review import SJBFilterInput, SJBReviewInput
from app.apps.analyzer.services.buisness_services.sentiment import analyze_sentiment
from app.core.settings import logger
from app.database import sync_session
from app.models.reviews import Reviews


class ReviewService:
    @classmethod
    async def create_review(cls, data: SJBReviewInput):
        """
        Create a review
        :param data: SJBReviewInput
        :return:
        """
        with sync_session() as session:
            sentiment = await analyze_sentiment(data.text)

            review = Reviews(
                text=data.text,
                sentiment=sentiment,
            )
            session.add(review)
            session.commit()
            logger.info(f"Review created: id={review.id}, sentiment={review.sentiment}")

            return review

    @classmethod
    async def get_reviews(cls, data: SJBFilterInput):
        """
        Get reviews
        :param data:
        :return:
        """
        with sync_session() as session:
            stmt = select(Reviews).where(Reviews.sentiment == data.sentiment)
            result = session.execute(stmt)
            return result.scalars().all()
