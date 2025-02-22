from fastapi import FastAPI
from app.api.routes import auth, users

# Crear instancia de FastAPI
api_app = FastAPI(title="API REST con FastAPI & Flask")

# Registrar rutas
api_app.include_router(auth.router, prefix="/api", tags=["Auth"])
api_app.include_router(users.router, prefix="/api", tags=["Users"])

@api_app.get("/api/health", tags=["Health Check"])
async def health_check():
    return {"status": "ok", "message": "API funcionando correctamente"}
