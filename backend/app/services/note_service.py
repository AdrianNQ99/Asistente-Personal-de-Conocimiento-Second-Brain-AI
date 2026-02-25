"""
Servicio de Notas
==================

Lógica de negocio para operaciones con notas.
Separa la lógica de los endpoints para mantener el código limpio.

📚 Aprenderás:
- Patrón Service Layer (capa de servicio)
- Queries async con SQLAlchemy
- Paginación en la base de datos
- Manejo de errores de negocio

🔗 Docs: https://docs.sqlalchemy.org/en/20/orm/queryguide/select.html

=============================================================
PASO 7.6: Implementa junto con los endpoints de notas
=============================================================
"""

# TODO 7.24: Importar dependencias
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy import select, func
# from app.models.note import Note
# from app.schemas.note import NoteCreate, NoteUpdate


# TODO 7.25: Crear la clase NoteService
# class NoteService:
#     """
#     Servicio para operaciones CRUD de notas.
#
#     Uso:
#         service = NoteService(db_session)
#         note = await service.create(note_data, user_id)
#     """
#
#     def __init__(self, db: AsyncSession):
#         self.db = db
#
#     async def create(self, note_data: NoteCreate, owner_id: int) -> Note:
#         """Crear una nueva nota."""
#         # 1. Crear instancia del modelo Note
#         # 2. Agregar a la sesión: self.db.add(note)
#         # 3. Flush para obtener el ID: await self.db.flush()
#         # 4. Refresh para cargar relaciones: await self.db.refresh(note)
#         # 5. Retornar la nota
#         pass
#
#     async def get_by_id(self, note_id: int, owner_id: int) -> Note | None:
#         """Obtener una nota por ID. Verifica que pertenece al usuario."""
#         # Pista: select(Note).where(Note.id == note_id, Note.owner_id == owner_id)
#         pass
#
#     async def list_by_owner(self, owner_id: int, page: int = 1, per_page: int = 20):
#         """Listar notas del usuario con paginación."""
#         # 1. Calcular offset: (page - 1) * per_page
#         # 2. Query con .offset().limit().order_by()
#         # 3. Query count para total
#         # 4. Retornar items, total, page, per_page
#         pass
#
#     async def update(self, note_id: int, note_data: NoteUpdate, owner_id: int) -> Note | None:
#         """Actualizar una nota existente."""
#         # 1. Buscar la nota
#         # 2. Actualizar solo los campos que vienen (exclude_unset=True)
#         # 3. Flush y refresh
#         pass
#
#     async def delete(self, note_id: int, owner_id: int) -> bool:
#         """Eliminar una nota. Retorna True si se eliminó."""
#         # 1. Buscar la nota
#         # 2. Si existe: await self.db.delete(note)
#         # 3. Retornar True/False
#         pass
