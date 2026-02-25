"""
Modelo de Tag (Etiqueta)
=========================

Define la tabla "tags" en la base de datos.
Un tag puede estar asociado a múltiples notas (relación Many-to-Many).

📚 Aprenderás:
- Cómo funciona una relación Many-to-Many
- Cómo reutilizar la tabla de asociación (note_tags)

🔗 Docs: https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#many-to-many

=============================================================
PASO 4 (continuación): Implementa junto con note.py
=============================================================
"""

# TODO 4.6: Importar dependencias
# from sqlalchemy import String
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from app.db.base import Base, TimestampMixin
# from app.models.note import note_tags  # Tabla de asociación


# TODO 4.7: Definir el modelo Tag
# class Tag(TimestampMixin, Base):
#     """
#     Modelo de etiqueta.
#
#     Columnas:
#     - id: Identificador único
#     - name: Nombre del tag (único)
#     - color: Color hex para UI (opcional)
#
#     Relaciones:
#     - notes: Lista de notas que tienen este tag
#     """
#     __tablename__ = "tags"
#
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     name: Mapped[str] = mapped_column(String(100), unique=True, index=True)
#     color: Mapped[str | None] = mapped_column(String(7), nullable=True)  # ej: "#FF5733"
#
#     # Relación Many-to-Many con Note
#     # notes: Mapped[list["Note"]] = relationship(secondary=note_tags, back_populates="tags")
#
#     def __repr__(self) -> str:
#         return f"<Tag(id={self.id}, name={self.name})>"
