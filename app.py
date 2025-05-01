from flask import Flask, request, render_template, jsonify
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
from threading import Thread


# Cargar las variables de entorno
load_dotenv()

# Configuración del servidor SMTP
EMAIL_HOST = os.getenv('EMAIL_HOST', 'mail.tradicom.com.ar')  
EMAIL_HOST_USER = os.getenv('USER')
EMAIL_HOST_PASSWORD = os.getenv('PASSWORD')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))  # Cambiado a 587 para TLS
EMAIL_DESTINATARIO = os.getenv('DESTINATARIO')
EMAIL_DESTINATARIO_CC = os.getenv('DESTINATARIO_CC')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'true').lower() == 'true'
EMAIL_ASUNTO = os.getenv('ASUNTO')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def send_async_email(app, msg, remitente, destinatarios, password):
    with app.app_context():
        try:
            server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
            if EMAIL_USE_TLS:
                server.starttls()  # Inicia TLS
            server.login(remitente, password)
            server.send_message(msg)
            server.quit()
            print(f"Correo enviado a: {destinatarios}")
        except Exception as e:
            print(f"Error al enviar el correo: {str(e)}")
            raise  # Re-lanza el error para que se registre en los logs

@app.route('/send_email', methods=['POST'])
def send_email():
    nombre = request.form.get('nombre')
    empresa = request.form.get('empresa')
    cargo = request.form.get('cargo')
    email = request.form.get('email')
    telefono = request.form.get('telefono')
    mensaje = request.form.get('mensaje')

    # Validar campos obligatorios
    if not all([nombre, email, telefono, mensaje]):
        return jsonify({"message": "Campos Obligatorios no ingresados."}), 400

    # Configuración del remitente y destinatarios
    remitente = EMAIL_HOST_USER
    password = EMAIL_HOST_PASSWORD
    destinatario = EMAIL_DESTINATARIO
    destinatario_cc = EMAIL_DESTINATARIO_CC
    asunto = EMAIL_ASUNTO

    # Validar configuración SMTP
    if not remitente or not password:
        return jsonify({"message": "Error en la configuración del servidor SMTP."}), 500

    # Crear el mensaje
    msg = EmailMessage()
    msg['From'] = remitente
    msg['To'] = destinatario
    if destinatario_cc:
        msg['Cc'] = destinatario_cc
    msg['Subject'] = asunto

    body = f"""
    Nombre: {nombre}
    Empresa: {empresa}
    Cargo: {cargo}
    Email: {email}
    Teléfono: {telefono}
    Mensaje: {mensaje}
    """
    msg.set_content(body)

    # Crear lista de destinatarios sin duplicados
    destinatarios = list(set([destinatario] + ([destinatario_cc] if destinatario_cc else [])))

    # Enviar el correo de manera asíncrona
    Thread(target=send_async_email, args=(app, msg, remitente, destinatarios, password)).start()
    return jsonify({"message": "Gracias por ponerse en contacto con Tradicom S.A. nos comunicaremos con ud. a la brevedad"}), 200

if __name__ == '__main__':
    app.run(debug=True)