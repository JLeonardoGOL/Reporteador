# Reporteador

Proyecto en blanco de **Django** (v6.1.2) con Python 3.12, listo para desarrollar.

## 📁 Estructura del proyecto

```
.
├── manage.py            # CLI de administración de Django
├── requirements.txt     # Dependencias (Django==6.1.2)
├── db.sqlite3           # Base de datos SQLite (migraciones aplicadas)
├── .gitignore
├── mysite/              # Configuración del proyecto
│   ├── settings.py      # Ajustes (INSTALLED_APPS incluye 'core')
│   ├── urls.py          # Enrutado raíz + /admin/
│   ├── asgi.py
│   └── wsgi.py
└── core/                # App principal
    ├── views.py         # Vista home ("¡Hola, Django!")
    ├── urls.py          # Ruta raíz: GET /
    ├── models.py
    ├── admin.py
    ├── apps.py
    ├── tests.py
    └── migrations/
```

## 🚀 Instalación y ejecución

1. **Crear y activar un entorno virtual** (recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate        # Linux/macOS
   # venv\Scripts\activate        # Windows
   ```

2. **Instalar dependencias**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Aplicar migraciones** (ya aplicadas en `db.sqlite3`, ejecútalo si usas una BD nueva):

   ```bash
   python manage.py migrate
   ```

4. **Arrancar el servidor de desarrollo**:

   ```bash
   python manage.py runserver
   ```

   Abre http://127.0.0.1:8000/ — verás la página de inicio *"¡Hola, Django!"*.

## 🔑 Panel de administración

Crea un superusuario y accede a http://127.0.0.1:8000/admin/:

```bash
python manage.py createsuperuser
```

## 🛠️ Comandos útiles

| Comando | Descripción |
|---|---|
| `python manage.py check` | Verifica que no hay problemas en el proyecto |
| `python manage.py makemigrations` | Genera migraciones de `core` |
| `python manage.py migrate` | Aplica las migraciones |
| `python manage.py test` | Ejecuta las pruebas |
| `python manage.py shell` | Consola interactiva de Django |

## ⚙️ Notas de configuración

- **Base de datos**: SQLite por defecto (`db.sqlite3`). Para PostgreSQL u otro motor, edita `DATABASES` en `mysite/settings.py`.
- **DEBUG**: Activado (`True`) para desarrollo. Recuerda desactivarlo y configurar `SECRET_KEY` / `ALLOWED_HOSTS` de forma segura antes de producción.
- **Idioma**: `LANGUAGE_CODE = 'en-us'` y `TIME_ZONE = 'UTC'` (cámbialos a `'es-es'` / `'UTC'` local si lo necesitas en `settings.py`).

## 📄 Licencia

Proyecto interno — sin licencia pública definida.