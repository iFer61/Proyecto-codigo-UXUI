from app import app 
from models import db, Usuario, Doctor

with app.app_context():
    print("Conectando a MySQL y creando tablas...")
    db.drop_all()   # Limpia la base de datos (solo para desarrollo)
    db.create_all()
    print("Tablas creadas exitosamente.")

    # ── 1. Usuarios de Prueba (Administrador y Paciente) ──
    admin = Usuario(nombre="Admin Hospital", email="admin@umahospital.com", rol="admin")
    admin.set_password("admin123")

    paciente = Usuario(nombre="Paciente Demo", email="paciente@correo.com", rol="paciente")
    paciente.set_password("paciente123")

    db.session.add_all([admin, paciente])

    # ── 2. Doctores del Directorio Médico ──
    doc1 = Doctor(
        nombre="Dr. Emilio Córdova", 
        especialidad="Medicina General", 
        imagen="doctor-1.svg"
    )
    doc2 = Doctor(
        nombre="Dr. Fernando Lema", 
        especialidad="Medicina General", 
        imagen="doctor-2.svg"
    )
    doc3 = Doctor(
        nombre="Dr. Carlos Ruíz Luna", 
        especialidad="Neumología", 
        imagen="doctor-3.svg"
    )

    db.session.add_all([doc1, doc2, doc3])
    db.session.commit()

    print("✅ Base de datos poblada con éxito.")
    print("Pacientes y Doctores listos para recibir citas.")