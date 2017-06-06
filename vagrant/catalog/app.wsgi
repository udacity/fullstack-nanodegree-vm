#!/usr/bin/python
import os
import re
import sys
import subprocess
import logging

sys.path.insert(0,"/var/www/catalog/")

sys.stdout = sys.stderr

logging.basicConfig(stream=sys.stderr)

# Starting virtual environment
VIRTUAL_ENV_DIR=os.environ['VIRTUAL_ENV_DIR']='/var/www/catalog/venv/'
CATALOG_APP=os.environ['CATALOG_APP']='/var/www/catalog/'


activate_this=os.path.join(VIRTUAL_ENV_DIR,'bin','activate_this.py')
execfile(activate_this, dict(__file__=activate_this))



os.chdir(CATALOG_APP)

from app import app as application
application.secret_key = 'AIzaSyBnsw4CDFk8wyf06jZoSu18bzzt1Cct1SY'


application_path=os.path.join(CATALOG_APP,'application.py')
sys.argv = [application_path,'-p 80']
execfile(application_path, dict(__file__=application_path))
