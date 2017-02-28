import sys
sys.path.append("/var/www/brat/myscript/script_py")
from controller.ann import exportAnn
from controller.ann import importAnn
import common.config as config
import common.parse as parse
import controller.extract.topic as topic
from model.topic import topicClass
import json

topic.extract()