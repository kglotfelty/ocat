

import os
import sys

assert "ASCDS_INSTALL" in os.environ, "Please run this after CIAO has been setup"


from distutils.core import setup
setup( name='qocat',
        version='4.13.0',
        description='Query the Chandra Observation Catalog by ObsId',
        author='Kenny Glotfelty',
        author_email='glotfeltyk@si.edu',
        url='https://github.com/kglotfelty/ocat/',
        scripts = ["qocat"]
        )

