"""
Second Brain AI - Punto de Entrada Principal
=============================================

Este archivo es donde se crea y configura la aplicación FastAPI.
Es el PRIMER archivo que debes implementar.

📚 Aprenderás:
- Cómo crear una instancia de FastAPI
- Qué es CORS y por qué es necesario
- Cómo incluir routers
- Cómo crear un health check endpoint

🔗 Docs: https://fastapi.tiangolo.com/tutorial/first-steps/

=============================================================
PASO 1: Implementa este archivo siguiendo las instrucciones
=============================================================
"""

# TODO 1.1: Importar FastAPI
# from fastapi import FastAPI

# TODO 1.2: Importar CORSMiddleware para permitir peticiones del frontend
# from fastapi.middleware.cors import CORSMiddleware

# TODO 1.3: Importar la configuración (la crearás en core/config.py)
# from app.core.config import settings

# TODO 1.4: Importar el router principal (lo crearás en api/v1/router.py)
# from app.api.v1.router import api_router


# TODO 1.5: Crear la instancia de FastAPI
# Pista: app = FastAPI(title=..., version=..., description=...)
# Docs: https://fastapi.tiangolo.com/tutorial/metadata/


# TODO 1.6: Configurar CORS middleware
# Pista: app.add_middleware(CORSMiddleware, allow_origins=[...], ...)
# Docs: https://fastapi.tiangolo.com/tutorial/cors/


# TODO 1.7: Incluir el router de la API v1
# Pista: app.include_router(api_router, prefix="/api/v1")


# TODO 1.8: Crear un endpoint raíz de health check
# @app.get("/")
# async def root():
#     """Health check - verifica que la API está funcionando."""
#     return {"status": "ok", "app": "Second Brain AI"}


# TODO 1.9: (Opcional) Crear evento de startup
# @app.on_event("startup")
# async def startup_event():
#     """Se ejecuta cuando la app inicia. Útil para conectar a la DB."""
#     pass
