from flask import Flask

# Create a New Flask App Instance
app = Flask(__name__)

# Create Flask Routes
@app.route('/')
def Hello_world():
    return 'Hello World'

# Run a Flask App
