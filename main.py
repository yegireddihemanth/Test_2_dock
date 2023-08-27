from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def hello_world():
    # return ("<h1>mod gud</h1>")
    return render_template('index.html')
   

# Run the app if this script is executed
if __name__ == '__main__':
    app.run(debug=True, port=8006, host='0.0.0.0')
