"""
Seguridad y Autenticación
==========================

Aquí implementas la lógica de seguridad: hashing de contraseñas y JWT tokens.

📚 Aprenderás:
- Qué es un hash y por qué no se guardan contraseñas en texto plano
- Qué es un JWT (JSON Web Token) y cómo funciona
- Cómo crear y verificar tokens de acceso
- Qué es OAuth2 con Password Bearer

🔗 Docs: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/

=============================================================
PASO 6: Implementa este archivo después de los schemas
=============================================================
"""

# TODO 6.1: Importar dependencias de seguridad
# from datetime import datetime, timedelta, timezone
# from typing import Optional
# from jose import JWTError, jwt
# from passlib.context import CryptContext
# from fastapi.security import OAuth2PasswordBearer
# from app.core.config import settings


# TODO 6.2: Configurar el contexto de hashing de contraseñas
# Pista: pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# Docs: https://passlib.readthedocs.io/en/stable/


# TODO 6.3: Configurar el esquema OAuth2
# Pista: oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


# TODO 6.4: Función para hashear una contraseña
# def hash_password(password: str) -> str:
#     """
#     Toma una contraseña en texto plano y devuelve su hash.
#     NUNCA guardes contraseñas sin hashear.
#     """
#     pass  # Implementar: return pwd_context.hash(password)


# TODO 6.5: Función para verificar una contraseña
# def verify_password(plain_password: str, hashed_password: str) -> bool:
#     """
#     Compara una contraseña en texto plano con un hash.
#     Devuelve True si coinciden.
#     """
#     pass  # Implementar: return pwd_context.verify(plain_password, hashed_password)


# TODO 6.6: Función para crear un token JWT
# def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
#     """
#     Crea un token JWT con los datos proporcionados.
#     El token tiene un tiempo de expiración.
#
#     Args:
#         data: Datos a incluir en el token (ej: {"sub": user_id})
#         expires_delta: Tiempo de expiración personalizado
#
#     Returns:
#         Token JWT como string
#     """
#     pass  # Implementar: copiar data, agregar "exp", codificar con jwt.encode()


# TODO 6.7: Función para verificar/decodificar un token JWT
# def verify_token(token: str) -> dict:
#     """
#     Decodifica y valida un token JWT.
#     Lanza una excepción si el token es inválido o expirado.
#     """
#     pass  # Implementar: jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
