"""
Sesión de Base de Datos
========================

Aquí configuras la conexión a PostgreSQL usando SQLAlchemy async.
Esto crea el "engine" (motor) y la "session" (sesión) para interactuar con la DB.

📚 Aprenderás:
- Qué es un ORM (Object-Relational Mapper)
- Qué es un engine y una session en SQLAlchemy
- Cómo funciona el patrón async/await con bases de datos
- Qué es una dependency injection en FastAPI (get_db)

🔗 Docs:
- https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html
- https://fastapi.tiangolo.com/tutorial/sql-databases/

=============================================================
PASO 3: Implementa este archivo después de core/config.py
=============================================================
"""

# TODO 3.1: Importar componentes de SQLAlchemy async
# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
# from app.core.config import settings


# TODO 3.2: Crear el engine async
# El engine es la conexión principal a la base de datos.
# Pista: engine = create_async_engine(settings.DATABASE_URL, echo=settings.DEBUG)
# - echo=True imprime las queries SQL en la consola (útil para aprender)


# TODO 3.3: Crear el session maker
# La session es como una "conversación" con la DB. Cada request usa una session.
# Pista: async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


# TODO 3.4: Crear la función get_db (dependency injection)
# Esta función se usa en los endpoints para obtener una sesión de DB.
# FastAPI la inyecta automáticamente.
#
# async def get_db():
#     """
#     Dependency que proporciona una sesión de base de datos.
#     Se usa así en los endpoints:
#         async def mi_endpoint(db: AsyncSession = Depends(get_db)):
#     """
#     async with async_session() as session:
#         try:
#             yield session
#             await session.commit()
#         except Exception:
#             await session.rollback()
#             raise
#         finally:
#             await session.close()
