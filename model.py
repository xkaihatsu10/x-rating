def score_post(features: dict):
    score = 50  # ベーススコア

    # 長さ：短すぎ/長すぎはマイナス、中程度はプラス
    if 50 <= features["length"] <= 150:
        score += 10
    else:
        score -= 5

    # 感情
    score += int(features["sentiment"] * 20)

    # 絵文字
    score += features["emoji_count"] * 2

    # ハッシュタグ（2〜3がベスト）
    if features["hashtags"] == 0:
        score -= 5
    elif 1 <= features["hashtags"] <= 3:
        score += 5
    else:
        score -= 5

    # メンション（多いとスパム扱い）
    if features["mentions"] > 3:
        score -= 10

    # 感嘆符・疑問符
    score += min(features["punctuation"], 5)

    # メディア
    if features["media_image"]:
        score += 15
    if features["media_video"]:
        score += 25

    # スコア範囲を制限
    score = max(0, min(100, score))

    return score
