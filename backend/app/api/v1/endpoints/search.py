"""
Endpoints de Búsqueda
======================

Endpoints para buscar notas por texto y, eventualmente, búsqueda semántica con IA.

📚 Aprenderás:
- Búsqueda por texto (LIKE en SQL)
- Parámetros de query para filtros
- (Avanzado) Búsqueda semántica con embeddings

=============================================================
PASO 9: Implementa cuando tengas el CRUD funcionando
=============================================================

Endpoints a crear:
- GET /text?q=...     → Búsqueda por texto en títulos y contenido
- GET /semantic?q=... → (Avanzado) Búsqueda semántica con IA
"""

# TODO 9.1: Importar dependencias
# from fastapi import APIRouter, Depends, Query
# from sqlalchemy.ext.asyncio import AsyncSession
# from app.db.session import get_db
# from app.schemas.note import NoteResponse
# from app.api.v1.dependencies import get_current_user
# from app.services.search_service import SearchService

# router = APIRouter()


# TODO 9.2: Búsqueda por texto
# @router.get("/text", response_model=list[NoteResponse])
# async def search_by_text(
#     q: str = Query(..., min_length=1, description="Texto a buscar"),
#     db: AsyncSession = Depends(get_db),
#     current_user = Depends(get_current_user),
# ):
#     """
#     Buscar notas por texto en título y contenido.
#     Usa ILIKE de PostgreSQL para búsqueda case-insensitive.
#     """
#     pass


# TODO 9.3: (Avanzado) Búsqueda semántica
# @router.get("/semantic", response_model=list[NoteResponse])
# async def search_semantic(
#     q: str = Query(..., min_length=1, description="Query semántica"),
#     limit: int = Query(10, ge=1, le=50),
#     db: AsyncSession = Depends(get_db),
#     current_user = Depends(get_current_user),
# ):
#     """
#     Búsqueda semántica usando embeddings e IA.
#     Encuentra notas relacionadas por SIGNIFICADO, no solo por palabras.
#     """
#     pass
