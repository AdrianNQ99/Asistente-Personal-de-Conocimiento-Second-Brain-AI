"""
Modelo de Usuario
==================

Define la tabla "users" en la base de datos.
Un usuario tiene email, contraseña (hasheada) y puede tener muchas notas.

📚 Aprenderás:
- Cómo definir un modelo/tabla con SQLAlchemy 2.0
- Qué son los tipos Mapped y mapped_column
- Cómo definir relaciones entre tablas (1 usuario -> muchas notas)
- Qué son las constraints (unique, nullable, etc.)

🔗 Docs: https://docs.sqlalchemy.org/en/20/orm/quickstart.html

=============================================================
PASO 4: Implementa los modelos después de configurar la DB
=============================================================
"""

# TODO 4.1: Importar dependencias
# from sqlalchemy import String, Boolean
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from app.db.base import Base, TimestampMixin


# TODO 4.2: Definir el modelo User
# class User(TimestampMixin, Base):
#     """
#     Modelo de usuario.
#
#     Columnas:
#     - id: Identificador único (primary key)
#     - email: Email del usuario (único)
#     - hashed_password: Contraseña hasheada (NUNCA texto plano)
#     - full_name: Nombre completo (opcional)
#     - is_active: Si el usuario está activo
#
#     Relaciones:
#     - notes: Lista de notas del usuario
#     """
#     __tablename__ = "users"
#
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
#     hashed_password: Mapped[str] = mapped_column(String(255))
#     full_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
#     is_active: Mapped[bool] = mapped_column(Boolean, default=True)
#
#     # Relación: Un usuario tiene muchas notas
#     # notes: Mapped[list["Note"]] = relationship(back_populates="owner")
#
#     def __repr__(self) -> str:
#         return f"<User(id={self.id}, email={self.email})>"
