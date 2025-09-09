import re
import emoji
from textblob import TextBlob

def extract_features(text: str, media_type: str = "none"):
    features = {}

    # 長さ
    features["length"] = len(text)

    # 感情スコア（-1.0〜1.0）
    features["sentiment"] = TextBlob(text).sentiment.polarity

    # 絵文字数
    features["emoji_count"] = len([c for c in text if c in emoji.EMOJI_DATA])

    # ハッシュタグ数
    features["hashtags"] = len(re.findall(r"#\w+", text))

    # メンション数
    features["mentions"] = len(re.findall(r"@\w+", text))

    # 感嘆符・疑問符
    features["punctuation"] = text.count("!") + text.count("?")

    # メディアタイプ
    features["media_image"] = 1 if media_type == "image" else 0
    features["media_video"] = 1 if media_type == "video" else 0

    return features
