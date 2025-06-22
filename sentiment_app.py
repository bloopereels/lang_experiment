import re

POSITIVE_WORDS = {
    'good', 'great', 'excellent', 'awesome', 'happy', 'love', 'fantastic', 'wonderful', 'amazing', 'nice', 'positive', 'fortunate', 'correct', 'superior'
}
NEGATIVE_WORDS = {
    'bad', 'terrible', 'awful', 'hate', 'sad', 'poor', 'wrong', 'horrible', 'negative', 'unfortunate', 'inferior', 'worst', 'disappointing', 'annoying'
}

def sentiment_score(text: str) -> float:
    words = re.findall(r"\b\w+\b", text.lower())
    pos_count = sum(1 for word in words if word in POSITIVE_WORDS)
    neg_count = sum(1 for word in words if word in NEGATIVE_WORDS)
    total = pos_count + neg_count
    if total == 0:
        return 0.0
    score = (pos_count - neg_count) / total
    # Ensure score is within [-1, 1]
    return max(min(score, 1.0), -1.0)


def main():
    print("Enter text (empty line to quit):")
    while True:
        try:
            text = input('> ').strip()
        except EOFError:
            break
        if not text:
            break
        score = sentiment_score(text)
        print(f"Sentiment score: {score:.2f}")

if __name__ == '__main__':
    main()
