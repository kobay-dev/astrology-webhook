from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "ok"}

@app.post("/webhook")
async def webhook(request: Request):
    try:
        data = await request.json()
        # バリデーション（最低限のキー存在チェック）
        required_keys = ["timestamp", "name", "gender", "birthdate", "birthtime", "birthplace"]
        if not all(key in data for key in required_keys):
            return JSONResponse(
                status_code=400,
                content={"error": "Missing required fields", "received": data}
            )
        
        print("✅ Webhook受信:", data)
        return {"message": "Webhook received successfully"}
    except Exception as e:
        print("❌ Webhook受信エラー:", str(e))
        return JSONResponse(
            status_code=500,
            content={"error": "Internal server error", "detail": str(e)}
        )

# ローカルテスト用（Renderには不要）
# if __name__ == "__main__":
#     uvicorn.run("webhook_server:app", host="0.0.0.0", port=8000)
