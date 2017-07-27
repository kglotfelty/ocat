

import os
import sys

assert "ASCDS_INSTALL" in os.environ

ver = sys.version_info
os.environ["PYVER"] = "python{}.{}".format(ver[0],ver[1])

from distutils.core import setup


setup( name='qocat',
        version='0.0.1',
        description='Query the Chandra Observation Catalog by ObsId',
        author='Anonymous',
        author_email='WhoDat@cfa.harvard.edu',
        url='https://github.com/kglotfelty/ocat/',
        scripts = ["qocat"],
        )

