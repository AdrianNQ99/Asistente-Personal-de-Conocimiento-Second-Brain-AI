"""
Servicio de IA
===============

Integración con modelos de IA para generar resúmenes,
etiquetado automático y embeddings.

📚 Aprenderás:
- Cómo llamar a APIs externas (OpenAI) desde Python
- Qué son los embeddings y para qué sirven
- Cómo estructurar prompts para obtener buenos resultados
- Manejo de errores con APIs externas

🔗 Docs:
- https://platform.openai.com/docs/api-reference
- https://python.langchain.com/docs/get_started/introduction

=============================================================
PASO 8: Implementa cuando el CRUD esté funcionando
=============================================================
"""

# TODO 8.1: Importar dependencias
# from openai import AsyncOpenAI  # o la librería que elijas
# from app.core.config import settings


# TODO 8.2: Crear la clase AIService
# class AIService:
#     """
#     Servicio para interactuar con modelos de IA.
#     """
#
#     def __init__(self):
#         """Inicializar el cliente de IA."""
#         # self.client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
#         pass
#
#     async def generate_summary(self, content: str) -> str:
#         """
#         Generar un resumen automático del contenido de una nota.
#
#         Args:
#             content: Texto de la nota a resumir
#
#         Returns:
#             Resumen del contenido
#
#         Pista de prompt:
#             "Resume el siguiente texto en 2-3 oraciones manteniendo las ideas clave: {content}"
#         """
#         pass
#
#     async def suggest_tags(self, content: str) -> list[str]:
#         """
#         Sugerir tags/etiquetas relevantes para una nota.
#
#         Args:
#             content: Texto de la nota
#
#         Returns:
#             Lista de tags sugeridos
#
#         Pista de prompt:
#             "Sugiere 3-5 etiquetas relevantes para el siguiente texto. 
#              Devuelve solo las etiquetas separadas por comas: {content}"
#         """
#         pass
#
#     async def generate_embedding(self, text: str) -> list[float]:
#         """
#         Generar un vector embedding del texto para búsqueda semántica.
#
#         Args:
#             text: Texto a convertir en embedding
#
#         Returns:
#             Vector de floats (embedding)
#
#         Pista:
#             Usa el modelo "text-embedding-3-small" de OpenAI
#             o sentence-transformers para embeddings locales.
#         """
#         pass
