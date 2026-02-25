# Second Brain AI

## Descripción
Second Brain AI es un asistente personal de conocimiento impulsado por IA que ayuda a los usuarios a organizar notas, enlaces y documentos. La app utiliza inteligencia artificial para generar resúmenes automáticos, encontrar conexiones entre ideas y sugerir acciones proactivas basadas en patrones detectados. Inspirado en el concepto de "second brain", este proyecto está diseñado para mejorar la productividad y la gestión de información personal.

### Funcionalidades Principales (MVP)
- Carga y almacenamiento de notas, enlaces y archivos (PDF, imágenes).
- Resúmenes automáticos y etiquetado inteligente con IA.
- Búsqueda semántica y visualización de conexiones entre ideas.
- Sugerencias proactivas y recordatorios.

## Tecnologías Utilizadas
- **Frontend**: React.js (o Next.js) para la interfaz de usuario.
- **Backend**: Python con FastAPI (o Flask) para la API.
- **IA**: LangChain o LlamaIndex con modelos como Llama 3 (open-source) o OpenAI API.
- **Base de Datos**: PostgreSQL o MongoDB para almacenamiento; Pinecone o FAISS para búsqueda vectorial.
- **Otras**: Docker para contenedores, Vercel/Heroku para despliegue.

## Instalación
1. Clona el repositorio:
   ```
   git clone https://github.com/AdrianNQ99/Asistente-Personal-de-Conocimiento-Second-Brain-AI
   cd second-brain-ai
   ```

2. Instala dependencias del backend (requiere Python 3.10+):
   ```
   pip install -r requirements.txt
   ```

3. Instala dependencias del frontend:
   ```
   cd frontend
   npm install
   ```

4. Configura variables de entorno (crea un `.env` basado en `.env.example`):
   - API keys para IA (ej. OPENAI_API_KEY si usas OpenAI).
   - Conexión a DB.

5. Ejecuta el backend:
   ```
   uvicorn main:app --reload
   ```

6. Ejecuta el frontend:
   ```
   npm run dev
   ```

La app estará disponible en `http://localhost:3000` (frontend) y `http://localhost:8000` (backend).

## Uso
- Accede a la app en el navegador.
- Regístrate/inicia sesión (si implementado).
- Sube notas o enlaces y explora las features de IA.

## Contribuyendo
¡Contribuciones bienvenidas! Forkea el repo, crea una branch y envía un pull request. Sigue el código de conducta.

## Licencia
MIT License. Ver [LICENSE](LICENSE) para detalles.

## Roadmap
- [ ] Implementar MVP básico.
- [ ] Agregar autenticación.
- [ ] Integrar visualizaciones de grafos.
- [ ] Desplegar en producción.

Proyecto en desarrollo inicial. ¡Feedback apreciado!
