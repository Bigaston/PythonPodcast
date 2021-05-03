import bottle
import os
os.chdir(os.path.dirname(__file__))

import index

application = bottle.default_app()