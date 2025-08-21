


# Pagina Web Tradicom S.A.

## Project Structure

```
tradicom-flask/
│   app.py
│   requirements.txt
│   README.md
│   server.log
│   .env
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── index.js
│   └── img/
│       ├── [various images, icons, and videos]
│       └── iconos/
│           ├── [favicon and app icons]
│
├── templates/
│   ├── index.html
│   ├── head.html
│   ├── navbar.html
│   ├── footer.html
│   ├── contacto.html
│   ├── galeria.html
│   ├── inicio.html
│   ├── membranas.html
│   ├── motores.html
│   ├── nosotros.html
│   ├── representacion.html
│   ├── separacion.html
│   └── servicios.html
│
├── .venv/           # Python virtual environment (not included in repo)
└── __pycache__/     # Python cache files
```


## Overview

This project is a modern, responsive web application for Tradicom S.A., designed to showcase the company's services, products, and contact information. The application is built using Python and Flask, with a strong focus on user experience, visual appeal, and robust backend functionality.

## Features

- Responsive multi-section website (Home, About Us, Clients, Representation, Motors & Compressors, Separation & Filtration, Membranes & Adsorption, Services, Contact)
- Video background and animated sections for a modern look
- Contact form with email sending (SMTP, asynchronous, with validation and logging)
- Google Maps integration for office locations
- WhatsApp direct contact button
- Dynamic navigation bar and footer
- Carousel and gallery for client and product images
- Custom CSS for branding and mobile optimization
- Error and server logging for traceability
- Deployed as a web application ([see deployment](#deployment))

## Tools & Technologies

- 🐍 **Python 3.12**
- ⚗️ **Flask 3.1**: Web framework for routing, templating, and backend logic
- 🧩 **Jinja2**: HTML templating engine
- 🎨 **Bootstrap 5.3**: Responsive design and UI components
- ⭐ **Font Awesome**: Iconography
- 📜 **JavaScript (ES6)**: Frontend interactivity (carousel, smooth scroll, AJAX form submission)
- 🖥️ **HTML5 & CSS3**: Custom styles and layout
- 🔤 **Google Fonts**: Typography
- 🗺️ **Google Maps Embed**: Location display
- 🔄 **Threading**: Asynchronous email sending
- �️ **dotenv**: Environment variable management

## Python Libraries Used

All dependencies are listed in `requirements.txt`:

```
🔔 blinker
🖱️ click
🎨 colorama
⚗️ Flask
🛡️ itsdangerous
🧩 Jinja2
🛡️ MarkupSafe
�️ python-dotenv
🛠️ Werkzeug
```

## Notable Implementation Details

- 🔄 **Asynchronous Email Sending**: Uses Python's `threading.Thread` to send emails without blocking the main server process.
- ✅ **Robust Form Validation**: Both client-side (JavaScript) and server-side (Python, regex) validation for contact forms.
- 📝 **Logging**: All email activity and errors are logged to `server.log` and `error.log` for traceability.
- 🔐 **Environment Variables**: Sensitive configuration (SMTP credentials, log paths) is managed via `.env` files and `python-dotenv`.
- 🧩 **Modular Templates**: Uses Jinja2 includes for reusable HTML components (navbar, footer, sections).
- 📱 **Mobile-First Design**: Extensive CSS media queries for optimal display on all devices.
- 🎬 **Rich Media**: Video backgrounds, image carousels, and icon sets for a professional appearance.

## Deployment

> 🚀 **The web application is deployed and accessible online at [https://www.tradicom.com.ar](https://www.tradicom.com.ar).**

Deployment is performed using Flask's production-ready configuration. The app is ready for deployment on any WSGI-compatible server (e.g., Gunicorn, uWSGI) or cloud platform. Static assets are served efficiently, and all environment variables are managed securely.

## How to Run Locally

1. 📥 Clone the repository.
2. 🐍 Create a virtual environment and activate it.
3. 📦 Install dependencies:
	```
	pip install -r requirements.txt
	```
4. ⚙️ Set up a `.env` file with the required SMTP and configuration variables.
5. ▶️ Run the application:
	```
	python app.py
	```
6. 🌍 Open your browser at `http://localhost:5000` (or visit the production site at https://www.tradicom.com.ar)

## Contact

For more information, visit [Tradicom S.A.](https://www.tradicom.com.ar) or contact Lic. Eduardo Moreno  +54 1168560011. mail: eduardomoreno2503@gmail.com


