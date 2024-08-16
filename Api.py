from dotenv import load_dotenv
load_dotenv()
from flask import Flask, jsonify
from services import about_service, users_service
import Scheduler as Sched


app = Flask(__name__)

@app.route('/about', methods=['GET'])
def get_about():
    return jsonify(about_service.get_about())

if __name__ == '__main__':
    about_service.start_about()
    users_service.start_users()
    Sched.start()
    app.run()