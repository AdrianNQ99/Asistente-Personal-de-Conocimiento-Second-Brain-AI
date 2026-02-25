"""
Router Principal de la API v1
==============================

Este archivo agrupa TODOS los routers de los endpoints de la API v1.
Es como un "índice" que conecta cada grupo de endpoints.

📚 Aprenderás:
- Qué es un APIRouter en FastAPI
- Cómo organizar endpoints en grupos (auth, notes, tags, search)
- Qué son los prefijos y tags en los routers

🔗 Docs: https://fastapi.tiangolo.com/tutorial/bigger-applications/

=============================================================
PASO 7.1: Implementa después de security.py
=============================================================
"""

# TODO 7.1: Importar APIRouter
# from fastapi import APIRouter

# TODO 7.2: Importar los routers de cada módulo de endpoints
# from app.api.v1.endpoints import auth, notes, tags, search

# TODO 7.3: Crear el router principal de v1
# api_router = APIRouter()

# TODO 7.4: Incluir cada router con su prefijo y tags
# Los tags agrupan los endpoints en la documentación automática (Swagger UI)
#
# api_router.include_router(
#     auth.router,
#     prefix="/auth",
#     tags=["Autenticación"]
# )
#
# api_router.include_router(
#     notes.router,
#     prefix="/notes",
#     tags=["Notas"]
# )
#
# api_router.include_router(
#     tags.router,
#     prefix="/tags",
#     tags=["Tags"]
# )
#
# api_router.include_router(
#     search.router,
#     prefix="/search",
#     tags=["Búsqueda"]
# )
