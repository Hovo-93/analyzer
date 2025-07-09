POSITIVE_WORDS = ["хорош", "люблю", "отлично"]
NEGATIVE_WORDS = ["плохо", "ненавижу"]


async def analyze_sentiment(text: str) -> str:
    """
    Analyze the sentiment of the given text.
    :param text:
    :return:
    """
    text_lower = text.lower()
    if any(word in text_lower for word in POSITIVE_WORDS):
        return "positive"
    if any(word in text_lower for word in NEGATIVE_WORDS):
        return "negative"
    return "neutral"
