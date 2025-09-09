from fastapi import FastAPI, Form
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from features import extract_features
from model import score_post

app = FastAPI()

# フロントを提供
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return FileResponse("static/index.html")

@app.post("/rate")
async def rate_post(text: str = Form(...), media_type: str = Form("none")):
    features = extract_features(text, media_type)
    score = score_post(features)

    explanation = []
    if features["media_video"]:
        explanation.append("動画付きは強く評価されます")
    if features["media_image"]:
        explanation.append("画像付きはプラス評価です")
    if features["sentiment"] > 0.2:
        explanation.append("ポジティブな感情が高評価です")
    if features["hashtags"] > 3:
        explanation.append("ハッシュタグが多すぎると逆効果です")

    return JSONResponse({
        "score": score,
        "comment": f"バズり度 {score}/100",
        "details": explanation
    })
