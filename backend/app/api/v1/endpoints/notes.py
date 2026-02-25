"""
Endpoints de Notas (CRUD)
==========================

Endpoints para crear, leer, actualizar y eliminar notas.
Este es el CORE de la aplicación.

📚 Aprenderás:
- Operaciones CRUD completas (Create, Read, Update, Delete)
- Parámetros de ruta (path parameters): /notes/{note_id}
- Parámetros de query para filtrado y paginación: ?page=1&per_page=10
- Cómo proteger endpoints y filtrar datos por usuario
- Response models para controlar qué datos se devuelven

🔗 Docs: https://fastapi.tiangolo.com/tutorial/path-params/

=============================================================
PASO 7.4: Implementa los endpoints CRUD de notas
=============================================================

Endpoints a crear:
- POST   /           → Crear una nota
- GET    /           → Listar notas del usuario (con paginación)
- GET    /{note_id}  → Obtener una nota específica
- PUT    /{note_id}  → Actualizar una nota
- DELETE /{note_id}  → Eliminar una nota
"""

# TODO 7.13: Importar dependencias
# from fastapi import APIRouter, Depends, HTTPException, status, Query
# from sqlalchemy.ext.asyncio import AsyncSession
# from app.db.session import get_db
# from app.schemas.note import NoteCreate, NoteUpdate, NoteResponse, NoteListResponse
# from app.api.v1.dependencies import get_current_user
# from app.services.note_service import NoteService

# router = APIRouter()


# TODO 7.14: Crear una nota
# @router.post("/", response_model=NoteResponse, status_code=status.HTTP_201_CREATED)
# async def create_note(
#     note_data: NoteCreate,
#     db: AsyncSession = Depends(get_db),
#     current_user = Depends(get_current_user),
# ):
#     """
#     Crear una nueva nota para el usuario autenticado.
#
#     El campo owner_id se asigna automáticamente desde el token.
#     """
#     pass


# TODO 7.15: Listar notas con paginación
# @router.get("/", response_model=NoteListResponse)
# async def list_notes(
#     page: int = Query(1, ge=1, description="Número de página"),
#     per_page: int = Query(20, ge=1, le=100, description="Items por página"),
#     db: AsyncSession = Depends(get_db),
#     current_user = Depends(get_current_user),
# ):
#     """
#     Listar las notas del usuario con paginación.
#     Solo devuelve las notas del usuario autenticado.
#     """
#     pass


# TODO 7.16: Obtener una nota por ID
# @router.get("/{note_id}", response_model=NoteResponse)
# async def get_note(
#     note_id: int,
#     db: AsyncSession = Depends(get_db),
#     current_user = Depends(get_current_user),
# ):
#     """
#     Obtener una nota específica.
#     Verifica que la nota pertenece al usuario.
#     """
#     pass


# TODO 7.17: Actualizar una nota
# @router.put("/{note_id}", response_model=NoteResponse)
# async def update_note(
#     note_id: int,
#     note_data: NoteUpdate,
#     db: AsyncSession = Depends(get_db),
#     current_user = Depends(get_current_user),
# ):
#     """
#     Actualizar una nota existente.
#     Solo el dueño puede actualizarla.
#     """
#     pass


# TODO 7.18: Eliminar una nota
# @router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_note(
#     note_id: int,
#     db: AsyncSession = Depends(get_db),
#     current_user = Depends(get_current_user),
# ):
#     """
#     Eliminar una nota.
#     Solo el dueño puede eliminarla.
#     Devuelve 204 No Content si se eliminó correctamente.
#     """
#     pass
