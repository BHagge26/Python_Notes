from flask import Flask, render_template
from python_table import StudentTable
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', students = StudentTable)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5001)