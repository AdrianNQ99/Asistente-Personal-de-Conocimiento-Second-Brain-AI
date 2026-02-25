"""
Endpoints de Tags
==================

Endpoints para gestionar etiquetas.

📚 Aprenderás:
- CRUD más sencillo (buena práctica antes de notas)
- Cómo manejar constraints unique (nombre duplicado)

=============================================================
PASO 7.5: Implementa después de los endpoints de notas
=============================================================

Endpoints a crear:
- POST /         → Crear un tag
- GET  /         → Listar todos los tags
- GET  /{tag_id} → Obtener un tag
- DELETE /{tag_id} → Eliminar un tag
"""

# TODO 7.19: Importar dependencias
# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.ext.asyncio import AsyncSession
# from app.db.session import get_db
# from app.schemas.tag import TagCreate, TagResponse
# from app.api.v1.dependencies import get_current_user

# router = APIRouter()


# TODO 7.20: Crear un tag
# @router.post("/", response_model=TagResponse, status_code=status.HTTP_201_CREATED)
# async def create_tag(tag_data: TagCreate, db: AsyncSession = Depends(get_db)):
#     """Crear un nuevo tag. Devuelve 409 si el nombre ya existe."""
#     pass


# TODO 7.21: Listar todos los tags
# @router.get("/", response_model=list[TagResponse])
# async def list_tags(db: AsyncSession = Depends(get_db)):
#     """Listar todos los tags disponibles."""
#     pass


# TODO 7.22: Obtener un tag por ID
# @router.get("/{tag_id}", response_model=TagResponse)
# async def get_tag(tag_id: int, db: AsyncSession = Depends(get_db)):
#     """Obtener un tag específico. Devuelve 404 si no existe."""
#     pass


# TODO 7.23: Eliminar un tag
# @router.delete("/{tag_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_tag(tag_id: int, db: AsyncSession = Depends(get_db)):
#     """Eliminar un tag. Devuelve 404 si no existe."""
#     pass
