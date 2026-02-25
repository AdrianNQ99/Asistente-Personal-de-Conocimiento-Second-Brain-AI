"""
Configuración de la Aplicación
================================

Aquí defines TODAS las configuraciones de la app usando Pydantic Settings.
Esto lee automáticamente el archivo .env y valida los valores.

📚 Aprenderás:
- Qué es el patrón de configuración centralizada
- Cómo usar pydantic-settings para leer variables de entorno
- Por qué NUNCA se hardcodean secretos en el código

🔗 Docs: https://docs.pydantic.dev/latest/concepts/pydantic_settings/

=============================================================
PASO 2: Implementa este archivo después de main.py
=============================================================
"""

# TODO 2.1: Importar BaseSettings de pydantic_settings
# from pydantic_settings import BaseSettings, SettingsConfigDict


# TODO 2.2: Crear la clase Settings que hereda de BaseSettings
# class Settings(BaseSettings):
#     """
#     Configuración de la aplicación.
#     Los valores se leen automáticamente del archivo .env
#     """
#
#     # --- Info de la App ---
#     APP_NAME: str = "Second Brain AI"
#     APP_VERSION: str = "0.1.0"
#     DEBUG: bool = True
#
#     # --- Base de Datos ---
#     DATABASE_URL: str
#
#     # --- JWT / Seguridad ---
#     SECRET_KEY: str
#     ALGORITHM: str = "HS256"
#     ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
#
#     # --- CORS ---
#     CORS_ORIGINS: str = "http://localhost:5173"
#
#     # TODO 2.3: Configurar la lectura del archivo .env
#     # model_config = SettingsConfigDict(
#     #     env_file=".env",
#     #     env_file_encoding="utf-8",
#     #     case_sensitive=True,
#     # )
#
#     # TODO 2.4: (Opcional) Propiedad para parsear CORS_ORIGINS como lista
#     # @property
#     # def cors_origins_list(self) -> list[str]:
#     #     return [origin.strip() for origin in self.CORS_ORIGINS.split(",")]


# TODO 2.5: Crear una instancia global de Settings
# Pista: settings = Settings()
# Esto se importará en otros archivos como: from app.core.config import settings
