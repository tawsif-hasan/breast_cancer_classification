from flask import Flask, jsonify, request, render_template
app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hi'

if __name__ == '__main__':
    print("Server running...")
    app.run()

