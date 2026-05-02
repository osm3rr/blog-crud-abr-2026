# Newspaper Lechería 📄

[![Django](https://img.shields.io/badge/Django-6.0.4-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Una aplicación web basada en Django para la gestión de artículos de periódico con autenticación de usuarios. Permite crear, leer, actualizar y eliminar artículos de manera sencilla y segura.

## ✨ Características

- 📝 **Gestión completa de artículos**: Crear, leer, actualizar y eliminar artículos
- 🔐 **Autenticación de usuarios**: Registro y inicio de sesión seguro
- 👤 **Atribución de autor**: Cada artículo está vinculado a su autor
- 📅 **Timestamps automáticos**: Fechas de creación y actualización
- 🎨 **Interfaz limpia y responsiva**: Diseño moderno con CSS personalizado
- 🛡️ **Permisos de acceso**: Solo usuarios autenticados pueden crear/editar/eliminar artículos
- 📱 **Responsive Design**: Funciona en dispositivos móviles y de escritorio

## 🚀 Instalación

### Prerrequisitos

- Python 3.8 o superior
- Git

### Pasos de instalación

1. **Clona el repositorio:**
   ```bash
   git clone <url-del-repositorio>
   cd crud_abr2026
   ```

2. **Crea un entorno virtual:**
   ```bash
   python -m venv .venv
   # En Windows:
   .venv\Scripts\activate
   # En macOS/Linux:
   source .venv/bin/activate
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecuta las migraciones de la base de datos:**
   ```bash
   python manage.py migrate
   ```

5. **Crea un superusuario (opcional, para acceder al admin de Django):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Ejecuta el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

7. **Abre tu navegador y visita:**
   ```
   http://127.0.0.1:8000/
   ```

## 📖 Uso

### Para usuarios no registrados:
- Ver la lista de artículos publicados
- Ver detalles de artículos individuales
- Registrarse como nuevo usuario

### Para usuarios registrados:
- Todo lo anterior, más:
- Crear nuevos artículos
- Editar artículos propios
- Eliminar artículos propios

### Navegación:
- **Inicio**: Lista de todos los artículos
- **Crear artículo**: Formulario para nuevos artículos (requiere login)
- **Iniciar sesión**: Acceso a la cuenta
- **Crear cuenta**: Registro de nuevo usuario
- **Cerrar sesión**: Salir de la cuenta

## 🏗️ Arquitectura del Proyecto

```
crud_abr2026/
├── base_project/          # Configuración principal del proyecto Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py       # Configuraciones de Django
│   ├── urls.py           # URLs principales
│   └── wsgi.py
├── newspaper/            # Aplicación de gestión de artículos
│   ├── __init__.py
│   ├── admin.py          # Configuración del admin
│   ├── apps.py
│   ├── models.py         # Modelo Article
│   ├── tests.py
│   ├── urls.py           # URLs de la app newspaper
│   └── views.py          # Vistas basadas en clases
├── signup/               # Aplicación de registro de usuarios
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py         # (Usa modelo User de Django)
│   ├── tests.py
│   ├── urls.py           # URLs de registro
│   └── views.py          # Vista SignUpView
├── static/               # Archivos estáticos
│   └── css/
│       └── style.css     # Estilos CSS
├── templates/            # Plantillas HTML
│   ├── _base.html        # Plantilla base
│   ├── article-create.html
│   ├── article-delete.html
│   ├── article-detail.html
│   ├── article-update.html
│   ├── articles-list.html
│   └── registration/
│       ├── login.html
│       └── signup.html
├── db.sqlite3            # Base de datos SQLite
├── manage.py             # Script de gestión de Django
└── requirements.txt      # Dependencias Python
```

## 📊 Modelos de Datos

### Article
```python
class Article(models.Model):
    title = models.CharField(max_length=200)          # Título del artículo
    content = models.TextField()                      # Contenido completo
    author = models.ForeignKey('auth.User',           # Autor (usuario de Django)
                               on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)  # Fecha de creación
    updated_at = models.DateTimeField(auto_now=True)  # Fecha de última actualización
```

## 🎯 Vistas y URLs

### Vistas principales:
- `ArticleListView`: Lista todos los artículos
- `ArticleDetailView`: Muestra un artículo específico
- `ArticleCreateView`: Formulario para crear artículos (requiere autenticación)
- `ArticleUpdateView`: Formulario para editar artículos (requiere autenticación y ser autor)
- `ArticleDeleteView`: Confirma eliminación de artículo (requiere autenticación y ser autor)
- `SignUpView`: Formulario de registro de usuarios

### URLs disponibles:
- `/` → Lista de artículos
- `/articulo/<id>/` → Detalle de artículo
- `/articulo/crear/` → Crear nuevo artículo
- `/articulo/<id>/editar/` → Editar artículo
- `/articulo/<id>/eliminar/` → Eliminar artículo
- `/accounts/signup/` → Registro de usuario
- `/accounts/login/` → Inicio de sesión
- `/accounts/logout/` → Cierre de sesión
- `/admin/` → Panel de administración de Django

## 🔧 Configuración

### Base de datos
Por defecto, utiliza SQLite3 (`db.sqlite3`). Para cambiar a otra base de datos, modifica `base_project/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # o mysql, etc.
        'NAME': 'nombre_db',
        'USER': 'usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Variables de entorno
Para producción, configura estas variables:
- `SECRET_KEY`: Clave secreta de Django
- `DEBUG`: False en producción
- `ALLOWED_HOSTS`: Lista de hosts permitidos

## 🧪 Pruebas

Ejecuta las pruebas con:
```bash
python manage.py test
```

## 🤝 Contribución

1. Haz fork del proyecto
2. Crea una rama para tu feature: `git checkout -b feature/nueva-funcionalidad`
3. Realiza tus cambios y haz commit: `git commit -am 'Agrega nueva funcionalidad'`
4. Push a la rama: `git push origin feature/nueva-funcionalidad`
5. Abre un Pull Request

### Guías de contribución:
- Sigue las convenciones de código de Django
- Agrega tests para nuevas funcionalidades
- Actualiza la documentación según sea necesario
- Usa commits descriptivos

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🙋‍♂️ Soporte

Si encuentras algún problema o tienes preguntas:
1. Revisa la documentación de Django: https://docs.djangoproject.com/
2. Abre un issue en el repositorio
3. Contacta al equipo de desarrollo

---

**Desarrollado con ❤️ usando Django**</content>
<parameter name="filePath">c:\Users\Ada-Amarillo\Documents\crud_abr2026\README.md