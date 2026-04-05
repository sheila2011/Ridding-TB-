from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        age_group = request.form['age_group']
        reasons = request.form.getlist('reasons')
        location = request.form['location']
        health_awareness = request.form['health_awareness']
        solutions = request.form['solutions']
        with open('responses.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, age_group, ', '.join(reasons), location, health_awareness, solutions])
        return 'Thank you for your response!'
    return render_template('questionnaire.html')

if __name__ == '__main__':
    app.run(debug=True)