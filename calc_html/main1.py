from flask import Flask, render_template, request

app = Flask(__name__)

def mostrar_tarifas_bondi():
    return '''
    <h2>Tarifas de Bondi:</h2>
    <ul>
        <li>1 - $300</li>
        <li>2 - $325</li>
    </ul>
    '''

def guardar_gastos(dia, gastos):
    with open('registro_gastos.txt', 'a') as archivo:
        archivo.write(f'Día {dia}: ${gastos}\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_gastos', methods=['POST'])
def calcular_gastos():
    medio_transporte = int(request.form['medio_transporte'])
    total_gastos = 0

    if medio_transporte == 1:
        return mostrar_tarifas_bondi()
        # Aquí puedes mostrar las tarifas de bondi en una página diferente
    # Resto del código para calcular gastos según el medio de transporte seleccionado

if __name__ == '__main__':
    app.run(debug=True)
