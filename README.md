# Programación Back-End: Sistema de Tickets de Soporte

El proyecto consiste en un sistema backend utilizando Django 6.1 y Django REST Framework (DRF) para digitalizar y centralizar la gestión de incidencias de soporte de una Mesa de Ayuda. Esta versión implementa una API REST funcional que permite realizar operaciones CRUD sobre el modelo de datos asignado.

## Descripción del Proyecto

El proyecto se compone de:
- DRF: El núcleo del proyecto donde se alojan las configuraciones principales, el enrutamiento global hacia la API y la lectura de variables de entorno.
- Sistema de Tickets de Soporte: La aplicación principal que gestiona la lógica de negocio, incluyendo modelos relacionales, serializadores y vistas basadas en         ModelViewSet.
- Base de Datos: Persistencia en base de datos MySQL mediante el ORM de Django, SQLAlchemy y mysqlclient.
- Endpoints REST: Enrutamiento automatizado mediante DefaultRouter para operaciones HTTP (GET, POST, PUT, PATCH, DELETE).

---

## Instrucciones de Instalación y Ejecución

Pasos para preparar y ejecutar el proyecto en entorno local:

### 1. Clonar el repositorio

Abra su terminal y ejecute el siguiente comando para descargar el proyecto:
git clone https://github.com/xepoiis/Proyecto-BackEnd.git
cd Proyecto-BackEnd

### 2. Crear y activar el ambiente virtual
Es estrictamente necesario crear un ambiente virtual para aislar las dependencias del proyecto.

En Windows:
python -m venv venv
venv\Scripts\activate

En macOS o Linux:
python3 -m venv venv
source venv/bin/activate

### 3. Instalar dependencias
Con el ambiente virtual activado, instale los paquetes necesarios especificados en el archivo requirements.txt:
pip install -r requirements.txt

### 4. Configuracion de Base de Datos y Entorno
Ejecute el script SQL provisto en la raiz del proyecto (scripts_db.sql) en su gestor MySQL para crear la base de datos y asignar los privilegios al usuario.

Asegurese de contar con el archivo .env en la raiz del proyecto para evitar la exposicion de credenciales.

### 5. Migraciones y Usuario Administrador
Genere las tablas en la base de datos e ingrese sus credenciales de administrador:
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

### 6. Ejecutar el proyecto
Finalmente, levante el servidor de desarrollo local utilizando el archivo manage.py:
python manage.py runserver

Una vez que el servidor este en ejecucion, podra acceder a la interfaz navegable de la API REST en las siguientes rutas:
- http://127.0.0.1:8000/api/categorias/
- http://127.0.0.1:8000/api/perfiles/
- http://127.0.0.1:8000/api/tickets/
- http://127.0.0.1:8000/api/auditoria/

---
Desarrollado por Jose Francisco Galdamez Borquez
