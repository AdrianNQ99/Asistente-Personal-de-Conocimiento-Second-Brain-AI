"""
Schemas de Tag
===============

Schemas Pydantic para operaciones con tags/etiquetas.

📚 Aprenderás:
- Schemas simples con pocos campos
- Validaciones de formato (ej: color hex)

=============================================================
PASO 5 (continuación): Implementa junto con los otros schemas
=============================================================
"""

# TODO 5.13: Importar dependencias
# from pydantic import BaseModel, ConfigDict, field_validator
# from datetime import datetime
# from typing import Optional


# TODO 5.14: Schema base de tag
# class TagBase(BaseModel):
#     """Campos comunes de un tag."""
#     name: str
#     color: Optional[str] = None  # Formato hex: "#FF5733"


# TODO 5.15: Schema para CREAR un tag
# class TagCreate(TagBase):
#     """Datos para crear un tag."""
#     pass  # Hereda todo de TagBase
#
#     # (Opcional) Validación del formato de color
#     # @field_validator("color")
#     # @classmethod
#     # def validate_color(cls, v):
#     #     if v and not v.startswith("#"):
#     #         raise ValueError("El color debe estar en formato hex (ej: #FF5733)")
#     #     return v


# TODO 5.16: Schema de RESPUESTA de tag
# class TagResponse(TagBase):
#     """Datos que la API devuelve para un tag."""
#     id: int
#     created_at: datetime
#
#     model_config = ConfigDict(from_attributes=True)
