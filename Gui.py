#!/usr/bin/python3
from flaskwebgui import FlaskUI
from myapp import create_app, db
# from myapp.models import *

app = create_app()
# with app.app_context():
#     db.create_all()

ui = FlaskUI(app, close_server_on_exit=True, idle_interval=30)

# https://github.com/ClimenteA/flaskwebgui
# using flaskwebgui to run this app directly.
if __name__=='__main__':
    ui.run()
