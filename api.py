import uvicorn
from app.api import api_app  # ✅ Importa correctamente la instancia de FastAPI

if __name__ == "__main__":
    #uvicorn.run(api_app, host="0.0.0.0", port=8000, reload=True)
    uvicorn.run("app_app:app", host="0.0.0.0", port=8000, reload=True)