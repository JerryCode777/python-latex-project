# Generación Automática de Informe en PDF con variables usando Python, Latex y JavaScript

Este proyecto es una aplicación que permite calcular el área de un triángulo dado su base y altura. Además del cálculo, la aplicación se distingue por generar un informe PDF automatizado usando LaTeX, combinando Python y JavaScript dentro de un entorno Docker. Este enfoque es ideal para generar memorias de cálculo técnicas con variables dinámicas.

## Tabla de Contenidos
- [Descripción](#descripción)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Instalación y Ejecución](#instalación-y-ejecución)
- [Uso](#uso)
- [Detalles Técnicos](#detalles-técnicos)
  - [Combinación de Python, LaTeX y JavaScript](#combinación-de-python-latex-y-javascript)

## Descripción

Esta aplicación web permite ingresar la base y la altura de un triángulo para calcular su área. Además de mostrar el resultado en pantalla, se genera un informe en formato PDF con LaTeX que puede ser descargado desde la interfaz web. El proyecto se ejecuta completamente en un entorno Docker, lo que garantiza que todas las dependencias necesarias se gestionen automáticamente y evita la instalación manual en tu sistema local.

Este enfoque es ideal para generar memorias de cálculo o informes técnicos que requieran variables modificables según los datos de entrada del usuario.

## Tecnologías Utilizadas

- **Frontend**:
  - HTML5, CSS3, JavaScript
- **Backend**:
  - Python (Flask)
  - LaTeX
- **Infraestructura**:
  - Docker y Docker Compose

## Instalación y Ejecución

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tu_usuario/mi_proyecto.git
    cd mi_proyecto
    ```

2. Asegúrate de tener Docker y Docker Compose instalados en tu máquina. Si no los tienes, sigue las instrucciones de instalación en [la página oficial de Docker](https://docs.docker.com/get-docker/).

3. Levanta los servicios de Docker usando `docker-compose`:

    ```bash
    docker-compose up --build
    ```

    Este comando construirá la imagen Docker y levantará los contenedores necesarios para la aplicación.

4. Abre tu navegador en `http://localhost:5000` para acceder a la aplicación.

## Uso

1. Ingresa la **base** y la **altura** del triángulo en el formulario.
2. Haz clic en **Calcular Área**.
3. El área del triángulo se mostrará en la página.
4. Haz clic en **Descargar Informe** para generar y descargar el informe en formato PDF con el área calculada.

## Detalles Técnicos

### Combinación de Python, LaTeX y JavaScript

Este proyecto destaca por la integración de tecnologías clave para la generación automatizada de documentos técnicos:

1. **JavaScript**: El frontend captura los valores de la base y la altura del triángulo mediante un formulario, y los envía al backend usando una petición `fetch` con el método POST.

2. **Python (Flask)**: En el backend, Flask recibe los datos y realiza el cálculo del área. Luego, genera un archivo `.tex` (LaTeX) que incluye el cálculo con variables modificables, como la base y la altura.

3. **LaTeX**: Usando LaTeX, Python genera el informe técnico con el resultado del cálculo. Un proceso en Python ejecuta `pdflatex` para compilar el archivo `.tex` y producir el informe en formato PDF.

4. **Docker**: Todo el proceso se ejecuta dentro de un contenedor Docker, lo que garantiza que las dependencias como Flask, LaTeX, y `pdflatex` estén correctamente configuradas sin intervención manual. Esto simplifica la ejecución y el despliegue del proyecto en cualquier sistema.

### Ejemplo de Informe en LaTeX

El archivo `.tex` generado automáticamente tiene un formato como el siguiente:

```latex
\documentclass{article}
\begin{document}
\title{Informe del Área de un Triángulo}
\author{Generado Automáticamente}
\date{\today}
\maketitle
El área del triángulo con base 10 y altura 5 es: 25.
\end{document}
