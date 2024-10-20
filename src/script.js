document.getElementById('triangulo-form').addEventListener('submit', function (event) {
    event.preventDefault();

    const base = document.getElementById('base').value;
    const altura = document.getElementById('altura').value;

    fetch('http://localhost:5000/calcular', {  // Cambiado aquí
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ base, altura }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('resultado').innerText = data.mensaje;
    })
    .catch(error => console.error('Error:', error));
});

// Añade este código para descargar el informe
document.getElementById('descargar').addEventListener('click', function () {
    window.open('http://localhost:5000/informe', '_blank');
});
