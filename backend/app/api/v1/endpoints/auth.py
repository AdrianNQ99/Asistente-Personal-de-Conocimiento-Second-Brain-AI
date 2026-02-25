"""
Endpoints de Autenticación
===========================

Endpoints para registro, login y gestión de sesión.

📚 Aprenderás:
- Cómo crear endpoints POST para registro y login
- Cómo usar OAuth2PasswordRequestForm para recibir credenciales
- Cómo devolver un JWT token después del login
- Cómo proteger un endpoint con Depends(get_current_user)

🔗 Docs: https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/

=============================================================
PASO 7.3: Implementa los endpoints de autenticación
=============================================================

Endpoints a crear:
- POST /register  → Registrar nuevo usuario
- POST /login     → Iniciar sesión (devuelve JWT)
- GET  /me        → Obtener perfil del usuario actual
"""

# TODO 7.8: Importar dependencias
# from fastapi import APIRouter, Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordRequestForm
# from sqlalchemy.ext.asyncio import AsyncSession
# from app.db.session import get_db
# from app.schemas.user import UserCreate, UserResponse, Token
# from app.core.security import hash_password, verify_password, create_access_token
# from app.api.v1.dependencies import get_current_user

# TODO 7.9: Crear el router
# router = APIRouter()


# TODO 7.10: Endpoint de registro
# @router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
# async def register(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
#     """
#     Registrar un nuevo usuario.
#
#     Pasos:
#     1. Verificar que el email no existe ya
#     2. Hashear la contraseña
#     3. Crear el usuario en la DB
#     4. Devolver los datos del usuario (sin password)
#     """
#     pass


# TODO 7.11: Endpoint de login
# @router.post("/login", response_model=Token)
# async def login(
#     form_data: OAuth2PasswordRequestForm = Depends(),
#     db: AsyncSession = Depends(get_db),
# ):
#     """
#     Iniciar sesión.
#
#     Pasos:
#     1. Buscar usuario por email (form_data.username)
#     2. Verificar contraseña
#     3. Si es válido, crear token JWT
#     4. Devolver el token
#     """
#     pass


# TODO 7.12: Endpoint para obtener perfil actual
# @router.get("/me", response_model=UserResponse)
# async def get_me(current_user = Depends(get_current_user)):
#     """
#     Obtener el perfil del usuario autenticado.
#     Este endpoint está PROTEGIDO: requiere un token JWT válido.
#     """
#     pass  # return current_user
