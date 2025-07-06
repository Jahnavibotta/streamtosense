from textblob import TextBlob

def detect_emotions(text):
    polarity = TextBlob(text).sentiment.polarity

    if polarity <= -0.7:
        return "😭 Grief"
    elif polarity <= -0.4:
        return "😢 Sadness"
    elif polarity <= -0.2:
        return "😟 Anxiety"
    elif polarity < 0:
        return "😕 Discomfort"
    elif polarity == 0:
        return "😐 Neutral"
    elif polarity <= 0.2:
        return "🙂 Content"
    elif polarity <= 0.4:
        return "😊 Calm"
    elif polarity <= 0.6:
        return "😄 Happy"
    elif polarity <= 0.8:
        return "🤩 Excited"
    else:
        return "🥳 Joyful"
