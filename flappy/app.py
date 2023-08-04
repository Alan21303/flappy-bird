from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script')
def run_script():
    try:
        subprocess.run(['python', 'flappy.py'], check=True)
        return 'Python script executed successfully!'
    except subprocess.CalledProcessError as e:
        return f'Error: {e}'

if __name__ == '__main__':
    app.run(debug=True)
