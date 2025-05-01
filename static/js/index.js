/* Scripts para la pagina de contacto */
document.addEventListener('DOMContentLoaded', function() {
    var enlaceContacto = document.querySelector('a[href="#contacto"]');
    enlaceContacto.addEventListener('click', function(event) {
        event.preventDefault();
        var tituloContacto = document.getElementById('titulo-contacto');
        tituloContacto.scrollIntoView({ behavior: 'smooth' });
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const carouselMotores = new bootstrap.Carousel('#carouselMotores', {
        interval: 3000,
        ride: 'carousel'
    });

    const carouselSeparacion = new bootstrap.Carousel('#carouselSeparacion', {
        interval: 3000,
        ride: 'carousel'
    });
});

document.getElementById('contactForm').addEventListener('submit', async function (event) {
    event.preventDefault();

    const formData = new FormData(this);
    const response = await fetch('/send_email', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    const messageBox = document.getElementById('messageBox');
    const messageContent = document.getElementById('messageContent');

    if (response.ok) {
        messageContent.textContent = result.message; // Mensaje de éxito
    } else {
        messageContent.textContent = result.message || 'Ocurrió un error al enviar el formulario.'; // Mensaje de error
    }

    messageBox.style.display = 'flex'; // Mostrar el cuadro de mensaje
});

function closeMessageBox() {
    document.getElementById('messageBox').style.display = 'none'; // Ocultar el cuadro de mensaje
}