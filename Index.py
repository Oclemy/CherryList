import os

import cherrypy
from jinja2 import Environment, FileSystemLoader

# GET CURRENT DIRECTORY
CUR_DIR = os.path.dirname(os.path.abspath(__file__))
env=Environment(loader=FileSystemLoader(CUR_DIR),
trim_blocks=True)

# OUR CONTROLLER
class Index(object):

    # INDEX ACTION MAPPED TO HOMEPAGE
    @cherrypy.expose()
    def index(self):
        template = env.get_template('index.html')
        # RENDER TEMPLATE PASSING IN DATA
        return template.render(title='Amazing Universe', description='Our universe is quite amazing',list_header="Galaxies!", galaxies=self.get_galaxies(),site_title="Camposha.info")

    # HELPER FUNCTION TO RETURN GALAXIES LIST
    def get_galaxies(self):
        galaxies=["Messier 81","StarBurst","Black Eye","Cosmos Redshift","Sombrero","Hoags Object","Andromeda","Centarus A","Whirlpool","Canis Major Overdensity"]
        return galaxies

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    # RUN
    cherrypy.quickstart(Index(), '/', conf)
