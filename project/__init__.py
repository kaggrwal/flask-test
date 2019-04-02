import os,sys
from flask import Flask, jsonify


# instantiate the app
app = Flask(__name__)


#app.config.from_object('project.config.DevelopmentConfig')
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)


print(app.config, file=sys.stderr)
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
