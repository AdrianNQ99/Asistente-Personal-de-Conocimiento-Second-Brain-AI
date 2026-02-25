"""
Schemas de Usuario
===================

Los Schemas (también llamados DTOs) definen la estructura de los datos
que la API recibe y devuelve. Usan Pydantic para validación automática.

📚 Aprenderás:
- Diferencia entre Model (DB) y Schema (API)
- Cómo Pydantic valida datos automáticamente
- Patrón Create/Update/Response para separar datos de entrada y salida
- Qué es model_config y por qué usar from_attributes=True

🔗 Docs: https://fastapi.tiangolo.com/tutorial/schema-extra-example/

=============================================================
PASO 5: Implementa los schemas después de los modelos
=============================================================

💡 CONCEPTO CLAVE:
- UserCreate: Lo que el usuario ENVÍA para registrarse (incluye password)
- UserResponse: Lo que la API DEVUELVE (NUNCA incluye password)
- UserUpdate: Lo que el usuario ENVÍA para actualizar su perfil
"""

# TODO 5.1: Importar Pydantic
# from pydantic import BaseModel, EmailStr, ConfigDict
# from datetime import datetime
# from typing import Optional


# TODO 5.2: Schema base con campos comunes
# class UserBase(BaseModel):
#     """Campos comunes entre crear y responder."""
#     email: EmailStr
#     full_name: Optional[str] = None


# TODO 5.3: Schema para CREAR un usuario (input)
# class UserCreate(UserBase):
#     """
#     Datos requeridos para registrar un usuario.
#     Nota: incluye 'password' porque el usuario lo envía al registrarse.
#     """
#     password: str  # Texto plano, se hasheará antes de guardar


# TODO 5.4: Schema para ACTUALIZAR un usuario (input)
# class UserUpdate(BaseModel):
#     """
#     Datos opcionales para actualizar perfil.
#     Todos los campos son opcionales.
#     """
#     full_name: Optional[str] = None
#     password: Optional[str] = None


# TODO 5.5: Schema de RESPUESTA (output)
# class UserResponse(UserBase):
#     """
#     Datos que la API devuelve. NUNCA incluye la contraseña.
#     """
#     id: int
#     is_active: bool
#     created_at: datetime
#
#     # Permite crear el schema desde un objeto SQLAlchemy
#     model_config = ConfigDict(from_attributes=True)


# TODO 5.6: Schema para el token de autenticación
# class Token(BaseModel):
#     """Respuesta del endpoint de login."""
#     access_token: str
#     token_type: str = "bearer"
#
# class TokenData(BaseModel):
#     """Datos extraídos del token JWT."""
#     user_id: Optional[int] = None
