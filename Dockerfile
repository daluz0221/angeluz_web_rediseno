FROM python:3.8-slim

# Establece la variable de entorno PYTHONUNBUFFERED para evitar que Python haga buffering de la salida a la consola
ENV PYTHONUNBUFFERED 1

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo requirements.txt al directorio de trabajo del contenedor
COPY requirements.txt /app/

RUN adduser pipe && su - pipe

# Instala las dependencias de la aplicación Django
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el contenido del directorio actual al directorio de trabajo del contenedor
COPY . /app/

# Exponer el puerto 8000 en el contenedor
EXPOSE 8000

# Define el comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]