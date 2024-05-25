from dotenv import load_dotenv
load_dotenv()

from flask import Flask, jsonify
from services import AboutService
import Scheduler as Sched


app = Flask(__name__)

@app.route('/about', methods=['GET'])
def get_about():
    return jsonify(AboutService.getAbout())

if __name__ == '__main__':
    AboutService.startAbout()
    Sched.start()
    app.run()