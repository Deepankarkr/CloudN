from flask import Flask
from apis import api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api.init_app(app)

app.config['SECRET_KEY'] = '(*$&%^$^#@**($(@&@&$(^('

#app.run(debug=True)
if __name__ == '__main__':
    app.run(port='4000',debug=True)
