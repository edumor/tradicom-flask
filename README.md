# Tradicom S.A. — Production Web Application

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.1-000000?style=flat&logo=flask)](https://flask.palletsprojects.com)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=flat&logo=bootstrap&logoColor=white)](https://getbootstrap.com)
[![Live](https://img.shields.io/badge/Live-tradicom.com.ar-28a745?style=flat&logo=firefox&logoColor=white)](https://www.tradicom.com.ar)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat)](LICENSE)

Production web application for Tradicom S.A. — an industrial equipment company specializing in separation, filtration, membrane systems, motors, and compressors for the Argentine market.

**Live site:** [https://www.tradicom.com.ar](https://www.tradicom.com.ar)

> **This is the production Flask version.** The original static HTML/CSS/JS prototype is at [edumor/tradicom](https://github.com/edumor/tradicom).

---

## Features

- Multi-section responsive website — Home, About, Clients, Representation, Motors & Compressors, Separation & Filtration, Membranes & Adsorption, Services, Contact
- Contact form with SMTP email sending (asynchronous via Python threading)
- Both client-side (JavaScript) and server-side (Python/regex) form validation
- Server and error logging to `server.log` and `error.log`
- Google Maps embed for office location
- WhatsApp direct contact button
- Video background and animated sections
- Image carousel and client gallery
- Mobile-first responsive design with custom CSS

---

## Tech stack

| Layer | Technology |
|---|---|
| Backend | Python 3.12 · Flask 3.1 · Jinja2 |
| Frontend | HTML5 · CSS3 · Bootstrap 5.3 · JavaScript ES6 |
| Email | SMTP · Python `threading` (async sending) |
| Maps | Google Maps Embed API |
| Icons | Font Awesome · Google Fonts |
| Config | python-dotenv · `.env` files |
| Deployment | WSGI-compatible server (Gunicorn/uWSGI) |

---

## Project structure

```
tradicom-flask/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not committed)
├── static/
│   ├── css/style.css
│   ├── js/index.js
│   └── img/                # Images, icons, videos
└── templates/
    ├── index.html
    ├── head.html
    ├── navbar.html
    ├── footer.html
    ├── contacto.html
    ├── galeria.html
    ├── inicio.html
    ├── membranas.html
    ├── motores.html
    ├── nosotros.html
    ├── representacion.html
    ├── separacion.html
    └── servicios.html
```

---

## Notable implementation details

- **Async email** — uses `threading.Thread` to send contact form emails without blocking the server
- **Dual validation** — client-side JavaScript + server-side Python/regex on all form inputs
- **Modular templates** — Jinja2 `include` for reusable navbar, footer, and section components
- **Logging** — all email activity and errors logged for traceability
- **Secure config** — SMTP credentials and sensitive paths managed via `.env` and `python-dotenv`

---

## Running locally

```bash
# 1. Clone the repository
git clone https://github.com/edumor/tradicom-flask.git
cd tradicom-flask

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Edit .env with your SMTP credentials

# 5. Run the application
python app.py
```

Open [http://localhost:5000](http://localhost:5000) in your browser.

---

## Dependencies

```
Flask
Jinja2
Werkzeug
python-dotenv
blinker
click
colorama
itsdangerous
MarkupSafe
```

---

## Related repository

| Repo | Description |
|---|---|
| [`tradicom`](https://github.com/edumor/tradicom) | Original static HTML/CSS/JS prototype |
| [`tradicom-flask`](https://github.com/edumor/tradicom-flask) | This repo — production Flask application |

---

## Author

**Eduardo Moreno** — Senior Software Developer · Full Stack & Backend Python

- GitHub: [@edumor](https://github.com/edumor)
- LinkedIn: [linkedin.com/in/eduardomoreno-15813b19b](https://linkedin.com/in/eduardomoreno-15813b19b)
- Email: [eduardomoreno2503@gmail.com](mailto:eduardomoreno2503@gmail.com)
- Live project: [https://www.tradicom.com.ar](https://www.tradicom.com.ar)
