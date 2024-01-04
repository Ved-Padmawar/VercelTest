from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
def attendance_tracker():
    attendance_data = []
    with open('attendence.csv', 'r') as file: 
        csv_reader = csv.reader(file)
        for row in csv_reader:
            attendance_data.append(row)

    return render_template('index.html', attendance_data=attendance_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


