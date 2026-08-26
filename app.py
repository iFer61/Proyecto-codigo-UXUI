import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, session, flash
from config import Config
from models import db, Usuario, Doctor, Cita

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route("/")
def inicio():
    # Renderiza el Landing Page principal
    return render_template("index.html")

@app.route("/directorio")
def directorio():
    # Extrae todos los doctores activos de MySQL
    doctores = Doctor.query.filter_by(activo=True).all()
    return render_template("search-results.html", doctores=doctores)

# ==========================================
# RUTAS DE AUTENTICACIÓN Y SEGURIDAD
# ==========================================

@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        email = request.form["email"].strip().lower()

        # Verifica si el correo ya está registrado
        if Usuario.query.filter_by(email=email).first():
            flash("Ya existe una cuenta con ese correo.", "danger")
            return render_template("registro.html")

        # Crea un nuevo paciente
        nuevo_paciente = Usuario(
            nombre=request.form["nombre"],
            email=email,
            rol="paciente"
        )
        nuevo_paciente.set_password(request.form["password"])
        db.session.add(nuevo_paciente)
        db.session.commit()

        flash("Cuenta creada correctamente. Ya puedes iniciar sesión.", "success")
        return redirect(url_for("login"))

    return render_template("registro.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"].strip().lower()
        password = request.form["password"]

        usuario = Usuario.query.filter_by(email=email).first()

        # Verifica credenciales
        if usuario and usuario.check_password(password):
            session["usuario_id"] = usuario.id
            session["usuario_nombre"] = usuario.nombre
            session["usuario_rol"] = usuario.rol
            flash(f"¡Bienvenido a UMA Hospital, {usuario.nombre}!", "success")
            return redirect(url_for("inicio"))
        else:
            flash("Correo o contraseña incorrectos.", "danger")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    flash("Sesión cerrada correctamente.", "success")
    return redirect(url_for("inicio"))

if __name__ == "__main__":
    app.run(debug=True)