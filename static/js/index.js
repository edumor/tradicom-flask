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
    if (response.ok && result.redirect) {
        window.location.href = result.redirect; // Redirige con el mensaje
    } else {
        alert(result.message); // Muestra el error si ocurre
    }
});
