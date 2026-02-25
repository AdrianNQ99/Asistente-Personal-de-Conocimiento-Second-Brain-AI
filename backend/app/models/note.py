"""
Modelo de Nota
===============

Define la tabla "notes" en la base de datos.
Una nota pertenece a un usuario y puede tener múltiples tags.

📚 Aprenderás:
- Relaciones Many-to-One (muchas notas -> un usuario)
- Relaciones Many-to-Many (notas <-> tags) con tabla intermedia
- Qué es una Foreign Key (clave foránea)
- Tipos de datos en SQLAlchemy (Text, String, etc.)

🔗 Docs: https://docs.sqlalchemy.org/en/20/orm/relationships.html

=============================================================
PASO 4 (continuación): Implementa junto con user.py
=============================================================
"""

# TODO 4.3: Importar dependencias
# from sqlalchemy import String, Text, ForeignKey, Table, Column, Integer
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from app.db.base import Base, TimestampMixin


# TODO 4.4: (Opcional) Crear la tabla intermedia para la relación Note <-> Tag
# Esta tabla NO tiene modelo propio, es solo una tabla de asociación.
# note_tags = Table(
#     "note_tags",
#     Base.metadata,
#     Column("note_id", Integer, ForeignKey("notes.id"), primary_key=True),
#     Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True),
# )


# TODO 4.5: Definir el modelo Note
# class Note(TimestampMixin, Base):
#     """
#     Modelo de nota.
#
#     Columnas:
#     - id: Identificador único
#     - title: Título de la nota
#     - content: Contenido principal (texto largo)
#     - source_url: URL de origen (si la nota viene de un enlace)
#     - summary: Resumen generado por IA
#     - owner_id: ID del usuario dueño (Foreign Key)
#
#     Relaciones:
#     - owner: Usuario dueño de la nota
#     - tags: Lista de tags asociados
#     """
#     __tablename__ = "notes"
#
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     title: Mapped[str] = mapped_column(String(500))
#     content: Mapped[str] = mapped_column(Text)
#     source_url: Mapped[str | None] = mapped_column(String(2000), nullable=True)
#     summary: Mapped[str | None] = mapped_column(Text, nullable=True)
#     owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
#
#     # Relaciones
#     # owner: Mapped["User"] = relationship(back_populates="notes")
#     # tags: Mapped[list["Tag"]] = relationship(secondary=note_tags, back_populates="notes")
#
#     def __repr__(self) -> str:
#         return f"<Note(id={self.id}, title={self.title[:30]})>"
