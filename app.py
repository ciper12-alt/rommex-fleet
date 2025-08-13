from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulación de base de datos en memoria
vehiculos = []

@app.route('/')
def home():
    return redirect(url_for('listado_vehiculos'))

@app.route('/vehiculos')
def listado_vehiculos():
    return render_template('listado.html', vehiculos=vehiculos)

@app.route('/vehiculos/nuevo', methods=['GET', 'POST'])
def agregar_vehiculo():
    if request.method == 'POST':
        nuevo = {
            'id': vehiculos[-1]['id'] + 1 if vehiculos else 1,
            'marca': request.form['marca'],
            'modelo': request.form['modelo'],
            'anio': request.form['anio']
        }
        vehiculos.append(nuevo)
        return redirect(url_for('listado_vehiculos'))
    return render_template('nuevo_vehiculo.html')

@app.route('/vehiculos/editar/<int:id>', methods=['GET', 'POST'])
def editar_vehiculo(id):
    vehiculo = next((v for v in vehiculos if v['id'] == id), None)
    if not vehiculo:
        return 'Vehículo no encontrado', 404
    if request.method == 'POST':
        vehiculo['marca'] = request.form['marca']
        vehiculo['modelo'] = request.form['modelo']
        vehiculo['anio'] = request.form['anio']
        return redirect(url_for('listado_vehiculos'))
    return render_template('editar_vehiculo.html', vehiculo=vehiculo)

@app.route('/vehiculos/eliminar/<int:id>', methods=['POST'])
def eliminar_vehiculo(id):
    global vehiculos
    vehiculos = [v for v in vehiculos if v['id'] != id]
    return redirect(url_for('listado_vehiculos'))

if __name__ == '__main__':
    app.run(debug=True)
