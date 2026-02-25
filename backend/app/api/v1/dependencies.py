"""
Dependencias de la API
=======================

Funciones reutilizables que se inyectan en los endpoints.
La más importante: obtener el usuario actual desde el token JWT.

📚 Aprenderás:
- Qué es Dependency Injection en FastAPI
- Cómo proteger endpoints requiriendo autenticación
- Cómo reutilizar lógica con Depends()

🔗 Docs: https://fastapi.tiangolo.com/tutorial/dependencies/

=============================================================
PASO 7.2: Implementa junto con el router
=============================================================
"""

# TODO 7.5: Importar dependencias
# from fastapi import Depends, HTTPException, status
# from sqlalchemy.ext.asyncio import AsyncSession
# from app.db.session import get_db
# from app.core.security import oauth2_scheme, verify_token
# from app.models.user import User


# TODO 7.6: Crear dependency para obtener el usuario actual
# async def get_current_user(
#     token: str = Depends(oauth2_scheme),
#     db: AsyncSession = Depends(get_db),
# ) -> User:
#     """
#     Dependency que extrae y valida el token JWT del header Authorization.
#     Devuelve el usuario correspondiente.
#
#     Uso en endpoints:
#         @router.get("/mis-notas")
#         async def mis_notas(current_user: User = Depends(get_current_user)):
#             ...
#
#     Si el token es inválido, lanza HTTP 401.
#     """
#     # 1. Verificar el token
#     # 2. Extraer el user_id del token
#     # 3. Buscar el usuario en la DB
#     # 4. Si no existe, lanzar HTTPException 401
#     # 5. Retornar el usuario
#     pass


# TODO 7.7: (Opcional) Dependency para requerir usuario activo
# async def get_current_active_user(
#     current_user: User = Depends(get_current_user),
# ) -> User:
#     """Verifica que el usuario esté activo."""
#     if not current_user.is_active:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Usuario inactivo"
#         )
#     return current_user
