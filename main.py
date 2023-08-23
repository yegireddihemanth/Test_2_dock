from flask import Flask, render_template


app = Flask(__name__)
# app = Flask(__name__, template_folder='templates')

# Define a route and its associated function
@app.route('/')
def hello_world():
    # return render_template('index.html')
    return ("hello CI-CD working successfully")

# Run the app if this script is executed
if __name__ == '__main__':
    app.run(debug=True, port=8006, host='0.0.0.0')
