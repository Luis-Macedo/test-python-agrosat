#!/home/luis/Área de Trabalho/workspace/testes/farm_project/farm_back/pyenv/bin/python3

import sys
# import osgeo_utils.gdal_sieve as a convenience to use as a script
from osgeo_utils.gdal_sieve import *  # noqa
from osgeo_utils.gdal_sieve import main
from osgeo.gdal import deprecation_warn


deprecation_warn('gdal_sieve')
sys.exit(main(sys.argv))
