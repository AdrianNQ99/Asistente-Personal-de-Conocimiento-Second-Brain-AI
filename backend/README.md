# 🧠 Second Brain AI - Guía de Desarrollo del Backend

## 📖 Índice

1. [Vista General](#-vista-general)
2. [Arquitectura del Proyecto](#-arquitectura-del-proyecto)
3. [Prerrequisitos](#-prerrequisitos)
4. [Paso 0: Setup Inicial](#paso-0-setup-inicial)
5. [Paso 1: Crear la App FastAPI](#paso-1-crear-la-app-fastapi-appmainpy)
6. [Paso 2: Configuración con Pydantic](#paso-2-configuración-appcoreconfig)
7. [Paso 3: Conexión a la Base de Datos](#paso-3-conexión-a-la-base-de-datos-appdb)
8. [Paso 4: Modelos de Datos](#paso-4-modelos-de-datos-appmodels)
9. [Paso 5: Schemas Pydantic](#paso-5-schemas-pydantic-appschemas)
10. [Paso 6: Seguridad y JWT](#paso-6-seguridad-y-jwt-appcoresecuritypy)
11. [Paso 7: Endpoints de la API](#paso-7-endpoints-de-la-api-appapiservices)
12. [Paso 8: Integración con IA](#paso-8-integración-con-ia-appservicesai_servicepy)
13. [Paso 9: Búsqueda](#paso-9-búsqueda-appservicessearch_servicepy)
14. [Paso 10: Testing](#paso-10-testing)
15. [Comandos Útiles](#-comandos-útiles)
16. [Recursos de Aprendizaje](#-recursos-de-aprendizaje)

---

## 🔭 Vista General

Este backend usa **FastAPI** (Python) con la siguiente stack:

| Componente | Tecnología | Para qué sirve |
|---|---|---|
| **Framework Web** | FastAPI | Crear la API REST |
| **ORM** | SQLAlchemy 2.0 (async) | Interactuar con la DB sin escribir SQL puro |
| **Base de Datos** | PostgreSQL | Almacenar datos persistentes |
| **Migraciones** | Alembic | Versionar cambios en la estructura de la DB |
| **Validación** | Pydantic v2 | Validar datos de entrada/salida automáticamente |
| **Autenticación** | JWT (python-jose) | Tokens de sesión seguros |
| **IA** | OpenAI / LangChain | Resúmenes, tags automáticos, búsqueda semántica |

---

## 🏗 Arquitectura del Proyecto

```
backend/
├── .env.example          ← Variables de entorno (template)
├── .gitignore            ← Archivos ignorados por git
├── requirements.txt      ← Dependencias de Python
├── README.md             ← Esta guía
│
└── app/                  ← Código fuente principal
    ├── __init__.py       ← Marca app/ como paquete Python
    ├── main.py           ← 🟢 PASO 1: Punto de entrada de FastAPI
    │
    ├── core/             ← Configuración y utilidades centrales
    │   ├── config.py     ← 🟡 PASO 2: Settings desde .env
    │   └── security.py   ← 🔴 PASO 6: Hashing + JWT
    │
    ├── db/               ← Capa de base de datos
    │   ├── base.py       ← 🟡 PASO 3: Clase Base de SQLAlchemy
    │   └── session.py    ← 🟡 PASO 3: Conexión y sesión de DB
    │
    ├── models/           ← Modelos = Tablas de la DB
    │   ├── user.py       ← 🟠 PASO 4: Tabla users
    │   ├── note.py       ← 🟠 PASO 4: Tabla notes
    │   └── tag.py        ← 🟠 PASO 4: Tabla tags
    │
    ├── schemas/          ← Schemas = Forma de los datos de la API
    │   ├── user.py       ← 🔵 PASO 5: Schemas de usuario
    │   ├── note.py       ← 🔵 PASO 5: Schemas de nota
    │   └── tag.py        ← 🔵 PASO 5: Schemas de tag
    │
    ├── api/
    │   └── v1/
    │       ├── router.py       ← 🟣 PASO 7.1: Router principal
    │       ├── dependencies.py ← 🟣 PASO 7.2: Inyección de dependencias
    │       └── endpoints/
    │           ├── auth.py     ← 🟣 PASO 7.3: Login/Register
    │           ├── notes.py    ← 🟣 PASO 7.4: CRUD de notas
    │           ├── tags.py     ← 🟣 PASO 7.5: CRUD de tags
    │           └── search.py   ← ⚪ PASO 9: Búsqueda
    │
    └── services/         ← Lógica de negocio
        ├── note_service.py   ← 🟣 PASO 7.6: Lógica de notas
        ├── ai_service.py     ← ⚪ PASO 8: Integración IA
        └── search_service.py ← ⚪ PASO 9: Lógica de búsqueda
```

### 🧩 Flujo de una petición

```
Cliente (Frontend)
    │
    ▼
  main.py (FastAPI app)
    │
    ▼
  router.py (enruta a /notes, /auth, etc.)
    │
    ▼
  endpoints/notes.py (recibe request, valida con schema)
    │
    ▼
  services/note_service.py (lógica de negocio)
    │
    ▼
  models/note.py (interactúa con la DB via SQLAlchemy)
    │
    ▼
  PostgreSQL (base de datos)
```

---

## 📋 Prerrequisitos

Antes de empezar, asegúrate de tener instalado:

- [ ] **Python 3.10+** → [Descargar](https://www.python.org/downloads/)
- [ ] **PostgreSQL** → [Descargar](https://www.postgresql.org/download/) o usar Docker
- [ ] **Git** → [Descargar](https://git-scm.com/)
- [ ] **VS Code** con la extensión de Python

### Verifica tu instalación:
```bash
python --version    # Debe ser 3.10 o superior
psql --version      # Verifica PostgreSQL
git --version
```

---

## PASO 0: Setup Inicial

> **Objetivo:** Preparar el entorno de desarrollo.

### 0.1 Crear y activar el entorno virtual

```bash
# Navega a la carpeta backend
cd backend

# Crear entorno virtual
python -m venv venv

# Activar (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Activar (Windows CMD)
.\venv\Scripts\activate.bat

# Activar (Linux/Mac)
source venv/bin/activate
```

> 💡 **¿Qué es un venv?** Un entorno virtual aísla las dependencias de tu proyecto. Cada proyecto tiene sus propias librerías sin afectar al sistema.

### 0.2 Instalar dependencias

```bash
pip install -r requirements.txt
```

### 0.3 Configurar variables de entorno

```bash
# Windows
copy .env.example .env

# Linux/Mac
cp .env.example .env
```

Edita `.env` y configura:
- `DATABASE_URL`: Tu conexión a PostgreSQL
- `SECRET_KEY`: Genera una con `python -c "import secrets; print(secrets.token_hex(32))"`

### 0.4 Crear la base de datos en PostgreSQL

```bash
# Entra a PostgreSQL
psql -U postgres

# Crea la base de datos
CREATE DATABASE secondbrain_db;

# Sal de psql
\q
```

### ✅ Checkpoint: Tu entorno está listo cuando:
- [ ] `pip list` muestra fastapi, sqlalchemy, uvicorn instalados
- [ ] El archivo `.env` existe con tus valores
- [ ] La base de datos `secondbrain_db` existe en PostgreSQL

---

## PASO 1: Crear la App FastAPI (`app/main.py`)

> **Objetivo:** Crear la aplicación FastAPI y que responda en `http://localhost:8000`.
>
> **Archivo:** `app/main.py`
>
> **Conceptos:** FastAPI, CORS, routers, health check

### Qué hacer:
1. Abre `app/main.py` y sigue los TODOs numerados (1.1 a 1.9)
2. Descomenta y completa cada sección
3. Para esta primera versión, puedes omitir los TODOs de router e importar config (los harás después)

### Versión mínima para probar:
```python
from fastapi import FastAPI

app = FastAPI(title="Second Brain AI", version="0.1.0")

@app.get("/")
async def root():
    return {"status": "ok", "app": "Second Brain AI"}
```

### Probar:
```bash
# Desde la carpeta backend/
uvicorn app.main:app --reload
```

Abre tu navegador en:
- `http://localhost:8000` → Debería mostrar `{"status": "ok", ...}`
- `http://localhost:8000/docs` → Documentación automática (Swagger UI) 🎉

### ✅ Checkpoint:
- [ ] El servidor inicia sin errores
- [ ] `http://localhost:8000` devuelve JSON
- [ ] `http://localhost:8000/docs` muestra la documentación interactiva

### 📚 Lee sobre:
- [FastAPI - Primeros Pasos](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [CORS explicado](https://developer.mozilla.org/es/docs/Web/HTTP/CORS)

---

## PASO 2: Configuración (`app/core/config`)

> **Objetivo:** Centralizar la configuración usando variables de entorno.
>
> **Archivo:** `app/core/config.py`
>
> **Conceptos:** Pydantic Settings, .env, configuración centralizada

### Qué hacer:
1. Abre `app/core/config.py` y sigue los TODOs 2.1 a 2.5
2. Crea la clase `Settings` que lee del `.env`
3. Crea la instancia `settings` al final del archivo

### Cómo probarlo:
```python
# Prueba rápida en terminal (desde backend/)
python -c "from app.core.config import settings; print(settings.APP_NAME)"
```

### Luego actualiza main.py:
```python
from app.core.config import settings

app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)
```

### ✅ Checkpoint:
- [ ] `settings.APP_NAME` devuelve "Second Brain AI"
- [ ] `settings.DATABASE_URL` devuelve tu URL de PostgreSQL
- [ ] No hay secretos hardcodeados en el código

### 📚 Lee sobre:
- [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
- [12-Factor App - Config](https://12factor.net/config)

---

## PASO 3: Conexión a la Base de Datos (`app/db/`)

> **Objetivo:** Conectar la app a PostgreSQL con SQLAlchemy async.
>
> **Archivos:** `app/db/session.py`, `app/db/base.py`
>
> **Conceptos:** ORM, Engine, Session, Dependency Injection

### Qué hacer:
1. **`base.py`**: Crea la clase `Base` y el `TimestampMixin` (TODOs 3.5-3.7)
2. **`session.py`**: Crea el engine, session maker y `get_db` (TODOs 3.1-3.4)

### Concepto clave - ¿Qué es un ORM?

| Sin ORM (SQL puro) | Con ORM (SQLAlchemy) |
|---|---|
| `INSERT INTO users (email) VALUES ('a@b.com')` | `db.add(User(email="a@b.com"))` |
| `SELECT * FROM users WHERE id=1` | `db.get(User, 1)` |

El ORM te permite trabajar con **objetos Python** en vez de escribir SQL directamente.

### ✅ Checkpoint:
- [ ] `Base` está definida en `base.py`
- [ ] `get_db()` es un generador async que yield una sesión
- [ ] No hay errores de importación

### 📚 Lee sobre:
- [SQLAlchemy 2.0 Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/)
- [FastAPI + SQLAlchemy](https://fastapi.tiangolo.com/tutorial/sql-databases/)

---

## PASO 4: Modelos de Datos (`app/models/`)

> **Objetivo:** Definir las tablas de la base de datos como clases Python.
>
> **Archivos:** `user.py`, `note.py`, `tag.py`
>
> **Conceptos:** Modelos, Relaciones (1-N, N-M), Foreign Keys, Constraints

### Qué hacer:
1. **`user.py`**: Modelo User (TODOs 4.1-4.2)
2. **`note.py`**: Modelo Note + tabla note_tags (TODOs 4.3-4.5)
3. **`tag.py`**: Modelo Tag (TODOs 4.6-4.7)
4. **`__init__.py`**: Importa todos los modelos

### Diagrama de relaciones:

```
┌──────────┐       ┌──────────┐       ┌──────────┐
│  users   │ 1───N │  notes   │ N───M │   tags   │
├──────────┤       ├──────────┤       ├──────────┤
│ id (PK)  │       │ id (PK)  │       │ id (PK)  │
│ email    │       │ title    │       │ name     │
│ hashed_  │       │ content  │       │ color    │
│ password │       │ summary  │       └──────────┘
│ full_name│       │ owner_id │            │
│ is_active│       │ (FK→user)│            │
└──────────┘       └──────────┘            │
                        │                  │
                   ┌────┴──────────────────┘
                   │   note_tags (tabla intermedia)
                   ├──────────────┐
                   │ note_id (FK) │
                   │ tag_id  (FK) │
                   └──────────────┘
```

### Crear las tablas con Alembic (migraciones):

```bash
# Inicializar Alembic (solo la primera vez)
alembic init alembic

# Editar alembic/env.py para agregar tus modelos y el DATABASE_URL
# (Te explico abajo qué cambiar)

# Generar una migración automática
alembic revision --autogenerate -m "crear tablas iniciales"

# Aplicar la migración (crear las tablas en la DB)
alembic upgrade head
```

> 💡 **Configurar Alembic (alembic/env.py):** Necesitas:
> 1. Importar `Base` de `app.db.base` y todos los modelos de `app.models`
> 2. Setear `target_metadata = Base.metadata`
> 3. Configurar la URL de la DB desde tu settings

### ✅ Checkpoint:
- [ ] Los 3 modelos (User, Note, Tag) están definidos
- [ ] Las relaciones están configuradas
- [ ] `alembic upgrade head` crea las tablas en PostgreSQL
- [ ] Puedes ver las tablas con `\dt` en psql

### 📚 Lee sobre:
- [SQLAlchemy Relationships](https://docs.sqlalchemy.org/en/20/orm/relationships.html)
- [Alembic Tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)

---

## PASO 5: Schemas Pydantic (`app/schemas/`)

> **Objetivo:** Definir la forma de los datos que entran y salen de la API.
>
> **Archivos:** `user.py`, `note.py`, `tag.py`
>
> **Conceptos:** DTOs, Validación automática, Serialización

### Concepto clave - Model vs Schema:

| Concepto | Model (SQLAlchemy) | Schema (Pydantic) |
|---|---|---|
| **Propósito** | Representar una tabla en la DB | Validar datos de la API |
| **Ubicación** | `app/models/` | `app/schemas/` |
| **Ejemplo** | `User` tiene `hashed_password` | `UserResponse` NO tiene password |

### Patrón de schemas por entidad:

```
UserBase          ← Campos comunes (email, name)
  ├── UserCreate  ← Para registro (incluye password)
  ├── UserUpdate  ← Para actualizar (todo opcional)  
  └── UserResponse ← Lo que devuelve la API (sin password, con id y fechas)
```

### Qué hacer:
1. **`user.py`**: Schemas de usuario + Token (TODOs 5.1-5.6)
2. **`note.py`**: Schemas de nota + paginación (TODOs 5.7-5.12)
3. **`tag.py`**: Schemas de tag (TODOs 5.13-5.16)

### Cómo probar los schemas:
```python
# Prueba rápida
python -c "
from app.schemas.user import UserCreate
user = UserCreate(email='test@test.com', password='123456')
print(user.model_dump())
"
```

### ✅ Checkpoint:
- [ ] Los schemas validan datos correctamente
- [ ] `UserCreate` requiere email y password
- [ ] `UserResponse` NO incluye password
- [ ] Los schemas con `from_attributes=True` pueden crearse desde objetos SQLAlchemy

### 📚 Lee sobre:
- [Pydantic Models](https://docs.pydantic.dev/latest/concepts/models/)
- [FastAPI Request Body](https://fastapi.tiangolo.com/tutorial/body/)

---

## PASO 6: Seguridad y JWT (`app/core/security.py`)

> **Objetivo:** Implementar hashing de contraseñas y tokens JWT.
>
> **Archivo:** `app/core/security.py`
>
> **Conceptos:** Hashing, JWT, OAuth2, Bearer tokens

### Concepto clave - ¿Cómo funciona la autenticación?

```
1. REGISTRO:
   Usuario envía email + password
   → Backend hashea el password → Guarda en DB

2. LOGIN:
   Usuario envía email + password
   → Backend verifica password vs hash
   → Si es válido, crea un JWT token
   → Devuelve el token al usuario

3. PETICIONES AUTENTICADAS:
   Usuario envía petición + token en header "Authorization: Bearer xxx"
   → Backend decodifica el token
   → Extrae el user_id
   → Busca el usuario en la DB
   → Permite o deniega la petición
```

### Qué hacer:
Sigue los TODOs 6.1 a 6.7 en `app/core/security.py`

### Cómo probar:
```python
python -c "
from app.core.security import hash_password, verify_password, create_access_token

# Test hashing
hashed = hash_password('mi_password')
print(f'Hash: {hashed}')
print(f'Verificar: {verify_password(\"mi_password\", hashed)}')

# Test JWT
token = create_access_token({'sub': '1'})
print(f'Token: {token}')
"
```

### ✅ Checkpoint:
- [ ] `hash_password()` devuelve un hash diferente al password original
- [ ] `verify_password()` retorna `True` con el password correcto
- [ ] `create_access_token()` genera un token JWT válido
- [ ] `verify_token()` decodifica el token correctamente

### 📚 Lee sobre:
- [JWT.io - Cómo funciona JWT](https://jwt.io/introduction)
- [FastAPI Security Tutorial](https://fastapi.tiangolo.com/tutorial/security/)
- [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

---

## PASO 7: Endpoints de la API (`app/api/`, `services/`)

> **Objetivo:** Crear todos los endpoints REST de la API.
>
> **Este es el paso más largo. Se divide en sub-pasos.**

### 7.1 Router Principal (`api/v1/router.py`)
Conecta todos los endpoints. Sigue los TODOs 7.1-7.4.

### 7.2 Dependencies (`api/v1/dependencies.py`)
Crea `get_current_user` para proteger endpoints. TODOs 7.5-7.7.

### 7.3 Endpoints de Auth (`api/v1/endpoints/auth.py`)
Registro y Login. TODOs 7.8-7.12.

**Prueba con Swagger UI:**
1. Ve a `http://localhost:8000/docs`
2. Usa `POST /api/v1/auth/register` para crear un usuario
3. Usa `POST /api/v1/auth/login` para obtener un token
4. Haz clic en "Authorize" 🔒 y pega el token
5. Prueba `GET /api/v1/auth/me`

### 7.4 Endpoints de Notes (`api/v1/endpoints/notes.py`)
CRUD completo de notas. TODOs 7.13-7.18.

### 7.5 Endpoints de Tags (`api/v1/endpoints/tags.py`)
CRUD de tags. TODOs 7.19-7.23.

### 7.6 Note Service (`services/note_service.py`)
Lógica de negocio separada. TODOs 7.24-7.25.

### Orden recomendado de implementación:
1. `note_service.py` → La lógica
2. `dependencies.py` → get_current_user
3. `auth.py` → Registro y login
4. `tags.py` → CRUD simple (practica)
5. `notes.py` → CRUD completo con relaciones
6. `router.py` → Conectar todo

### ✅ Checkpoint:
- [ ] Puedes registrar un usuario via Swagger UI
- [ ] Puedes hacer login y recibir un token
- [ ] Puedes crear, leer, actualizar y eliminar notas
- [ ] Los endpoints protegidos rechazan peticiones sin token (401)
- [ ] Un usuario solo puede ver sus propias notas

### 📚 Lee sobre:
- [FastAPI Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/)
- [FastAPI Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/)
- [HTTP Status Codes](https://developer.mozilla.org/es/docs/Web/HTTP/Status)

---

## PASO 8: Integración con IA (`app/services/ai_service.py`)

> **Objetivo:** Conectar con un modelo de IA para generar resúmenes y tags automáticos.
>
> **Archivo:** `app/services/ai_service.py`
>
> **Conceptos:** APIs de IA, Prompts, Embeddings

### Qué hacer:
1. Descomenta `openai` en `requirements.txt` e instala: `pip install openai`
2. Agrega tu `OPENAI_API_KEY` al `.env`
3. Implementa `AIService` (TODOs 8.1-8.2)

### Ideas de integración:
- Al crear una nota → Generar resumen automáticamente
- Al crear una nota → Sugerir tags automáticamente
- Generar embeddings para búsqueda semántica

### ✅ Checkpoint:
- [ ] `generate_summary()` devuelve un resumen del texto dado
- [ ] `suggest_tags()` devuelve una lista de tags relevantes
- [ ] Los errores de la API se manejan graciosamente (try/except)

### 📚 Lee sobre:
- [OpenAI API Docs](https://platform.openai.com/docs/quickstart)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

---

## PASO 9: Búsqueda (`app/services/search_service.py`)

> **Objetivo:** Permitir buscar notas por texto y semánticamente.
>
> **Archivos:** `services/search_service.py`, `api/v1/endpoints/search.py`

### Enfoque gradual:
1. **Primero:** Búsqueda por texto con `ILIKE` de PostgreSQL (sencillo)
2. **Después:** Búsqueda semántica con embeddings + FAISS (avanzado)

### ✅ Checkpoint:
- [ ] Puedes buscar notas por título o contenido
- [ ] La búsqueda es case-insensitive
- [ ] (Avanzado) La búsqueda semántica encuentra notas por significado

---

## PASO 10: Testing

> **Objetivo:** Escribir tests automatizados para verificar que todo funciona.

### Setup:
```bash
pip install pytest pytest-asyncio httpx
```

### Estructura sugerida:
```
backend/
└── tests/
    ├── __init__.py
    ├── conftest.py        ← Fixtures compartidos (test DB, test client)
    ├── test_auth.py       ← Tests de autenticación
    ├── test_notes.py      ← Tests de CRUD de notas
    └── test_tags.py       ← Tests de tags
```

### Ejemplo de test:
```python
# tests/test_auth.py
import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_register():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.post("/api/v1/auth/register", json={
            "email": "test@test.com",
            "password": "password123",
        })
        assert response.status_code == 201
        assert response.json()["email"] == "test@test.com"
        assert "password" not in response.json()  # ¡Nunca devolver password!
```

### Ejecutar tests:
```bash
pytest -v
```

### ✅ Checkpoint:
- [ ] Tienes al menos 1 test por cada endpoint
- [ ] Los tests pasan con `pytest`
- [ ] Usas una DB de prueba separada

---

## 🛠 Comandos Útiles

```bash
# --- Servidor ---
uvicorn app.main:app --reload              # Iniciar servidor con auto-reload
uvicorn app.main:app --host 0.0.0.0        # Accesible desde la red local

# --- Base de datos ---
alembic init alembic                        # Inicializar Alembic
alembic revision --autogenerate -m "msg"    # Crear migración
alembic upgrade head                        # Aplicar migraciones
alembic downgrade -1                        # Revertir última migración
alembic history                             # Ver historial de migraciones

# --- Dependencias ---
pip install -r requirements.txt             # Instalar dependencias
pip freeze > requirements.txt               # Guardar dependencias actuales

# --- Testing ---
pytest -v                                   # Correr tests (verbose)
pytest --cov=app                            # Tests con cobertura

# --- Utilidades ---
python -c "import secrets; print(secrets.token_hex(32))"  # Generar SECRET_KEY
```

---

## 📚 Recursos de Aprendizaje

### FastAPI (Framework)
- 📖 [Tutorial Oficial de FastAPI](https://fastapi.tiangolo.com/tutorial/) - **Empieza aquí**
- 🎥 [FastAPI Full Course (YouTube)](https://www.youtube.com/results?search_query=fastapi+full+course+español)
- 📖 [FastAPI Best Practices](https://github.com/zhanymkanov/fastapi-best-practices)

### SQLAlchemy (Base de Datos)
- 📖 [SQLAlchemy 2.0 Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/)
- 📖 [Async SQLAlchemy](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)

### Python Async
- 📖 [Async/Await en Python](https://docs.python.org/3/library/asyncio.html)
- 🎥 [Python Async explicado](https://www.youtube.com/results?search_query=python+asyncio+español)

### Seguridad
- 📖 [JWT.io](https://jwt.io/) - Entiende los tokens
- 📖 [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Vulnerabilidades comunes

### IA / NLP
- 📖 [OpenAI Cookbook](https://cookbook.openai.com/)
- 📖 [LangChain Docs](https://python.langchain.com/)

---

## 🗺 Roadmap Visual

```
PASO 0: Setup          ██████████ ← Estás aquí
PASO 1: main.py        ░░░░░░░░░░
PASO 2: config.py      ░░░░░░░░░░
PASO 3: DB             ░░░░░░░░░░
PASO 4: Models         ░░░░░░░░░░
PASO 5: Schemas        ░░░░░░░░░░
PASO 6: Security       ░░░░░░░░░░
PASO 7: API Endpoints  ░░░░░░░░░░ ← MVP listo aquí 🎉
PASO 8: IA             ░░░░░░░░░░
PASO 9: Search         ░░░░░░░░░░
PASO 10: Testing       ░░░░░░░░░░
```

> 💡 **Tip final:** Cada archivo tiene TODOs numerados que coinciden con los pasos de esta guía. Ábrelos en orden y sigue las instrucciones. ¡Buena suerte! 🚀
