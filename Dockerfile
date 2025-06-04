# Usar una imagen base oficial de Python 
FROM python:3.10-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY ./django_proyect /app

# Copiar el archivo requirements.txt (desde la raíz del proyecto al contenedor)
COPY requirements.txt /app/

# Instalar dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exponer el puerto de Django
EXPOSE 8000

# Comando para ejecutar Gunicorn (en lugar de Django runserver)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "django_proyect.wsgi:application"]
