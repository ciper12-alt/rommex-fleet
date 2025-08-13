from flask_sqlalchemy import SQLAlchemy
from app import db

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(20), unique=True, nullable=False)
    km_actual = db.Column(db.Integer, nullable=False)
    km_prox_mantencion = db.Column(db.Integer, nullable=True)
    # Agrega más campos según los requerimientos

    def __repr__(self):
        return f'<Vehicle {self.placa}>'
