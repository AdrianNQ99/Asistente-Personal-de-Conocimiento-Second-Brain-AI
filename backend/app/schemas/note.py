"""
Schemas de Nota
================

Schemas Pydantic para las operaciones CRUD de notas.

📚 Aprenderás:
- Cómo anidar schemas (NoteResponse incluye TagResponse)
- Validaciones personalizadas con Pydantic
- Schemas para paginación

🔗 Docs: https://docs.pydantic.dev/latest/concepts/models/

=============================================================
PASO 5 (continuación): Implementa junto con user.py
=============================================================
"""

# TODO 5.7: Importar dependencias
# from pydantic import BaseModel, ConfigDict, HttpUrl
# from datetime import datetime
# from typing import Optional
# from app.schemas.tag import TagResponse  # Lo crearás en tag.py


# TODO 5.8: Schema base de nota
# class NoteBase(BaseModel):
#     """Campos comunes de una nota."""
#     title: str
#     content: str
#     source_url: Optional[str] = None


# TODO 5.9: Schema para CREAR una nota
# class NoteCreate(NoteBase):
#     """
#     Datos para crear una nota.
#     Opcionalmente puede incluir tags.
#     """
#     tag_ids: list[int] = []  # IDs de tags existentes para asociar


# TODO 5.10: Schema para ACTUALIZAR una nota
# class NoteUpdate(BaseModel):
#     """Todos los campos son opcionales para actualización parcial."""
#     title: Optional[str] = None
#     content: Optional[str] = None
#     source_url: Optional[str] = None
#     tag_ids: Optional[list[int]] = None


# TODO 5.11: Schema de RESPUESTA de nota
# class NoteResponse(NoteBase):
#     """Datos que la API devuelve para una nota."""
#     id: int
#     summary: Optional[str] = None
#     owner_id: int
#     created_at: datetime
#     updated_at: datetime
#     # tags: list[TagResponse] = []  # Descomentar cuando tengas TagResponse
#
#     model_config = ConfigDict(from_attributes=True)


# TODO 5.12: (Opcional) Schema para respuesta paginada
# class NoteListResponse(BaseModel):
#     """Respuesta con lista de notas y metadata de paginación."""
#     items: list[NoteResponse]
#     total: int
#     page: int
#     per_page: int
