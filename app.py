from flask import Flask, render_template, url_for, jsonify

app = Flask(__name__, template_folder='template', static_folder='static')

@app.route('/static/particlesjs-config.json')
def particles_config():
    with open('static/particlesjs-config.json') as f:
        config = f.read()
    return jsonify(config)

@app.route("/")
def home():
   return render_template('home.html')

if __name__ == '__main__':
   app.run(host='localhost', port=8080, debug=True)