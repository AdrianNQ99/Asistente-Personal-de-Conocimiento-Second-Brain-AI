"""
Base Model de SQLAlchemy
=========================

Aquí defines la clase Base de la que heredarán TODOS tus modelos.
También puedes definir columnas comunes (como id, created_at, updated_at).

📚 Aprenderás:
- Qué es una clase Base en un ORM
- Cómo crear una clase mixin para columnas comunes
- Qué es DeclarativeBase en SQLAlchemy 2.0

🔗 Docs: https://docs.sqlalchemy.org/en/20/orm/mapping_api.html

=============================================================
PASO 3 (continuación): Implementa junto con session.py
=============================================================
"""

# TODO 3.5: Importar componentes de SQLAlchemy
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
# from sqlalchemy import DateTime, func
# from datetime import datetime


# TODO 3.6: Crear la clase Base
# class Base(DeclarativeBase):
#     """
#     Clase base para todos los modelos de SQLAlchemy.
#     Todos los modelos (User, Note, Tag) heredarán de esta clase.
#     """
#     pass


# TODO 3.7: (Opcional) Crear un mixin con columnas comunes
# class TimestampMixin:
#     """
#     Mixin que agrega columnas created_at y updated_at a cualquier modelo.
#     Uso: class MiModelo(TimestampMixin, Base): ...
#     """
#     created_at: Mapped[datetime] = mapped_column(
#         DateTime(timezone=True),
#         server_default=func.now(),
#     )
#     updated_at: Mapped[datetime] = mapped_column(
#         DateTime(timezone=True),
#         server_default=func.now(),
#         onupdate=func.now(),
#     )
