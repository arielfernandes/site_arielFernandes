import os
from flask import Flask, render_template, Blueprint
from src.site.agenda import agenda_blueprint
app = Flask(__name__)
app.register_blueprint(agenda_blueprint)

if __name__ == '__main__':
    port = int(os.getenv('PORT'), '5000')
    app.run(host='0.0.0.0', port=port)
