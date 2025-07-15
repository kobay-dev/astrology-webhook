from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

REQUIRED_FIELDS = ["name", "birthdate", "birthtime", "birthplace", "gender", "timestamp"]

@app.post("/webhook")
async def receive_webhook(request: Request):
    try:
        data = await request.json()

        missing = [key for key in REQUIRED_FIELDS if key not in data]
        if missing:
            raise HTTPException(status_code=400, detail=f"Missing fields: {', '.join(missing)}")

        print("✅ 受信成功:", data)
        return JSONResponse(status_code=200, content={"message": "受信完了", "data": data})

    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"error": e.detail})

    except Exception as e:
        print(f"[エラー] {e}")
        return JSONResponse(status_code=500, content={"error": "サーバーエラー"})
