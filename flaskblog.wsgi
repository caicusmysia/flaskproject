activate_this = '/var/www/peer.caicusmysia.com/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))
import sys
sys.path.insert(0,"/var/www/peer.caicusmysia.com/")
from flaskblog import create_app
application = create_app()
