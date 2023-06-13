from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='template', static_folder='static')

@app.route("/")
def home():
   return render_template('home.html')

if __name__ == '__main__':
   app.run(host='localhost', port=8080, debug=True)