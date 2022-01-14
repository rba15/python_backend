import flask

app = flask.Flask(__name__) 

''' import the APIs '''
from apis import script_apis

''' register the APIs '''
app.register_blueprint(script_apis)

if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug=True)