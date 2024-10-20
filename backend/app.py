from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import subprocess
import os

app = Flask(__name__)
CORS(app)

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.get_json()
    base = float(data['base'])
    altura = float(data['altura'])
    area = (base * altura) / 2

    # Crear el archivo LaTeX
    with open('informe.tex', 'w') as f:
        f.write(f"""
        \\documentclass{{article}}
        \\begin{{document}}
        \\title{{Informe del Área de un Triángulo}}
        \\author{{Generado Automáticamente}}
        \\date{{\\today}}
        \\maketitle
        El área del triángulo con base {base} y altura {altura} es: {area}.
        \\end{{document}}
        """)

    # Generar el PDF desde el archivo LaTeX
    subprocess.run(['pdflatex', 'informe.tex'])

    return jsonify({'mensaje': f'Área: {area}, Informe generado como informe.pdf'})

@app.route('/informe', methods=['GET'])
def download_pdf():
    return send_file('informe.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
