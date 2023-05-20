from flask import Flask, render_template, request
import pandas as pd
import csv

app = Flask(__name__)

@app.route('/')
def index():
    # Leer el archivo CSV
    df = pd.read_csv('preguntas.csv')

    # Convertir los datos del DataFrame a una lista de diccionarios
    questions = df.to_dict('records')

    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    answers = {}
    for key, value in request.form.items():
        if key.startswith('answer_'):
            question_id = key.split('_')[1]
            answers[question_id] = value

    # Guardar las respuestas en un archivo CSV
    with open('respuestas.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(answers.values())

    return '¡Respuestas enviadas y almacenadas correctamente!'

if __name__ == '__main__':
    app.run()
