from flask import Flask
app = Flask( __name__ )
from flask_cors  import CORS
cors = CORS(app, ressources= {r"/todo/api/v1.0/*" : {"origin": "*"}})
