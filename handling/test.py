from controller.ann import exportAnn
from controller.ann import importAnn
import common.config as config
import common.parse as parse
import controller.extract.topic as topic
from model.topic import topicClass
import json

"""
app = exportAnn()
app.to_pkl()
"""
def printAll(array):
    for data in array:
        print(data)

topic.extract()