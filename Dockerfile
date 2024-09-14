# Usa una imagen base de Python 3.12
FROM python:3.12-slim

# Establece el directorio de trabajo en /code
WORKDIR /code

# Instala las dependencias del sistema necesarias para compilar ciertas bibliotecas
RUN apt-get update && apt-get install -y \
    build-essential \
    libfreetype6-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copia el archivo de requisitos a /code
COPY requirements.txt /code/

# Actualiza pip y luego instala las dependencias del proyecto
RUN pip install --upgrade pip
RUN pip install pybind11>=2.12
RUN pip install -r requirements.txt

# Copia todo el código al directorio de trabajo
COPY . /code/

# Exponer el puerto que utiliza Django
EXPOSE 8000

# Comando por defecto para iniciar la aplicación Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
