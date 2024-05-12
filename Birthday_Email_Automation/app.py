from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_birthday', methods=['POST'])
def add_birthday():
    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dob']
        email = request.form['email']

        # Append the data to the CSV file
        with open('birthday.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([name, dob, email])

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
