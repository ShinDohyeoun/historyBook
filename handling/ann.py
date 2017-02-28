import sys
sys.path.append("/var/www/brat/myscript/script_py")
from controller.ann import exportAnn
from controller.ann import importAnn
import common.config as config

"""
exportAnn = exportAnn()
exportAnn.to_pkl()
"""
importAnn = importAnn()
importAnn.autoTagging("/var/www/brat/data/")