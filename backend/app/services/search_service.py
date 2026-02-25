"""
Servicio de Búsqueda
=====================

Lógica de búsqueda de notas: por texto y semántica.

📚 Aprenderás:
- Búsqueda con ILIKE en PostgreSQL (case-insensitive)
- (Avanzado) Búsqueda por similitud vectorial con FAISS
- Cómo combinar resultados de diferentes fuentes

=============================================================
PASO 9 (continuación): Implementa junto con los endpoints de search
=============================================================
"""

# TODO 9.4: Importar dependencias
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy import select, or_
# from app.models.note import Note
# from app.services.ai_service import AIService


# TODO 9.5: Crear la clase SearchService
# class SearchService:
#     """
#     Servicio de búsqueda de notas.
#     """
#
#     def __init__(self, db: AsyncSession):
#         self.db = db
#
#     async def search_by_text(self, query: str, owner_id: int) -> list[Note]:
#         """
#         Buscar notas por texto en título y contenido.
#
#         Usa ILIKE para búsqueda case-insensitive.
#         Pista: Note.title.ilike(f"%{query}%")
#         """
#         # stmt = select(Note).where(
#         #     Note.owner_id == owner_id,
#         #     or_(
#         #         Note.title.ilike(f"%{query}%"),
#         #         Note.content.ilike(f"%{query}%"),
#         #     )
#         # )
#         pass
#
#     async def search_semantic(self, query: str, owner_id: int, limit: int = 10):
#         """
#         Búsqueda semántica usando embeddings.
#
#         Pasos:
#         1. Generar embedding del query
#         2. Buscar los vectores más similares en FAISS
#         3. Obtener las notas correspondientes de la DB
#         """
#         pass
