# Usar una imagen base de Python
FROM python:3.9

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del backend
COPY app.py ./
COPY requirements.txt ./

# Instalar las dependencias
RUN pip install -r requirements.txt
RUN pip install flask-cors
RUN pip install pdfkit

# Copiar el archivo LaTeX y otras dependencias
RUN apt-get update && apt-get install -y texlive-latex-base

# Exponer el puerto
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
