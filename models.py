from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

# 1. TABLA DE USUARIOS (Pacientes y Administradores)
class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    
    # Roles: "paciente", "admin", "medico"
    rol = db.Column(db.String(20), nullable=False, default="paciente") 
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)

    # Relación: Un paciente puede tener muchas citas
    citas = db.relationship('Cita', backref='paciente', lazy=True)

    def set_password(self, password_plano):
        self.password_hash = generate_password_hash(password_plano)

    def check_password(self, password_plano):
        return check_password_hash(self.password_hash, password_plano)

    def es_admin(self):
        return self.rol == "admin"

    def __repr__(self):
        return f"<Usuario {self.email} ({self.rol})>"


# 2. TABLA DE DOCTORES
class Doctor(db.Model):
    __tablename__ = "doctores"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    especialidad = db.Column(db.String(100), nullable=False)
    
    # Para guardar el nombre del archivo SVG o JPG
    imagen = db.Column(db.String(255), nullable=True, default="default-doctor.svg")
    activo = db.Column(db.Boolean, default=True)

    # Relación: Un doctor tiene muchas citas programadas
    citas = db.relationship('Cita', backref='doctor', lazy=True)

    def __repr__(self):
        return f"<Doctor {self.nombre} - {self.especialidad}>"


# 3. TABLA DE CITAS (El "Motor de Reservas")
class Cita(db.Model):
    __tablename__ = "citas"

    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctores.id'), nullable=False)
    paciente_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    
    fecha = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    
    # Estados: "disponible", "reservada", "cancelada"
    estado = db.Column(db.String(20), default="reservada")
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Cita {self.fecha} {self.hora} - Dr. {self.doctor_id}>"