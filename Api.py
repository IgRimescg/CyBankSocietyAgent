from dotenv import load_dotenv
load_dotenv()

from flask import Flask, jsonify
from services import AboutService, CognitoService
import Scheduler as Sched




app = Flask(__name__)

@app.route('/date', methods=['GET'])
def get_date():
    return jsonify({'date': 'ok'})

@app.route('/cal', methods=['GET'])
def get_cal():
    return jsonify({'cal': 'ok'})

@app.route('/docker', methods=['GET'])
def get_docker():
    return jsonify({'docker': 'ok'})

@app.route('/cls', methods=['GET'])
def get_cls():
    return jsonify({'cls': 'ok'})

if __name__ == '__main__':
    AboutService.startAbout()
    Sched.start()
    app.run()