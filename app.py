from flask import Flask, request, render_template, jsonify
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
from threading import Thread
import uuid
import re

# Cargar las variables de entorno
load_dotenv()

# Configuración del servidor SMTP
EMAIL_HOST = os.getenv('EMAIL_HOST', 'mail.tradicom.com.ar')
EMAIL_HOST_USER = os.getenv('EMAIL_USER')  # Cambiado de 'USER' a 'EMAIL_USER'
EMAIL_HOST_PASSWORD = os.getenv('PASSWORD')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 465))
EMAIL_DESTINATARIO = os.getenv('DESTINATARIO')
EMAIL_ASUNTO = os.getenv('ASUNTO', 'Formulario de contacto')

# Ruta para los archivos de registro
log_file_path = os.getenv('LOG_FILE_PATH', '/home/tradicom/tradicom-flask')
os.makedirs(log_file_path, exist_ok=True)

# Validar configuración SMTP
if not all([EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_DESTINATARIO]):
    raise ValueError("Faltan variables de entorno necesarias para la configuración SMTP.")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def send_async_email(app, msg, remitente, password):
    with app.app_context():
        server = None
        try:
            server = smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT)
            server.login(remitente, password)
            server.send_message(msg)

            # Registrar conexión exitosa
            with open(os.path.join(log_file_path, 'server.log'), 'a') as server_log:
                server_log.write(f"[INFO] Conexión SSL exitosa al servidor SMTP {EMAIL_HOST} en el puerto {EMAIL_PORT}\n")
                server_log.write(f"[INFO] Correo enviado a: {msg['To']}\n")
        except smtplib.SMTPException as e:
            # Registrar errores específicos de SMTP
            with open(os.path.join(log_file_path, 'error.log'), 'a') as error_log:
                error_log.write(f"[ERROR] Error SMTP (SSL): {str(e)}\n")
        except Exception as e:
            # Registrar errores generales
            with open(os.path.join(log_file_path, 'error.log'), 'a') as error_log:
                error_log.write(f"[ERROR] Error al enviar el correo (SSL): {str(e)}\n")
        finally:
            if server:
                server.quit()

@app.route('/send_email', methods=['POST'])
def send_email():
    # Obtener datos del formulario
    nombre = request.form.get('nombre', '').strip()
    empresa = request.form.get('empresa', '').strip()
    cargo = request.form.get('cargo', '').strip()
    email = request.form.get('email', '').strip()
    telefono = request.form.get('telefono', '').strip()
    mensaje = request.form.get('mensaje', '').strip()

    # Validar campos obligatorios
    if not all([nombre, email, telefono, mensaje]):
        return jsonify({"message": "Campos obligatorios no ingresados."}), 400

    # Validar formato de correo electrónico
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        return jsonify({"message": "El correo electrónico no es válido."}), 400

    remitente = EMAIL_HOST_USER
    password = EMAIL_HOST_PASSWORD
    destinatario = EMAIL_DESTINATARIO
    asunto = EMAIL_ASUNTO

    if not remitente or not password:
        return jsonify({"message": "Error en la configuración del servidor SMTP."}), 500

    # Crear el mensaje de correo
    msg = EmailMessage()
    msg['From'] = remitente
    msg['To'] = destinatario
    msg['Reply-To'] = email
    msg['Subject'] = asunto
    msg['Message-ID'] = f"<{uuid.uuid4()}@{EMAIL_HOST}>"

    # Cuerpo del correo
    body = f"""
    Nombre: {nombre}
    Empresa: {empresa}
    Cargo: {cargo}
    Email: {email}
    Teléfono: {telefono}
    Mensaje: {mensaje}
    """
    msg.set_content(body)
    msg.add_alternative(f"""
    <html>
        <body>
            <p><strong>Nombre:</strong> {nombre}</p>
            <p><strong>Empresa:</strong> {empresa}</p>
            <p><strong>Cargo:</strong> {cargo}</p>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>Teléfono:</strong> {telefono}</p>
            <p><strong>Mensaje:</strong> {mensaje}</p>
        </body>
    </html>
    """, subtype='html')

    # Enviar el correo de forma asíncrona
    Thread(target=send_async_email, args=(app, msg, remitente, password)).start()
    return jsonify({"message": "Gracias por ponerse en contacto con Tradicom S.A. Nos comunicaremos con usted a la brevedad."}), 200

    
if __name__ == '__main__':
    app.run(debug=False)
