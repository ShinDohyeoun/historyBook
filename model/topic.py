import common.config as config
import json
import os
class srcInfo:
    srcName =""


class topicClass:
    word = None
    fileName = None
    relatedWord = None
    time = None
    space = None
    person = None
    book = None




    def __init__(self):
        self.word = ""
        self.fileName = ""
        self.relatedWord = []
        self.time = []
        self.space = []
        self.person = []
        self.book = []

    def toCSV(self):
        result = self.word+"\t"
        result += json.dumps(self.relatedWord, ensure_ascii=False, encoding='utf-8') +"\t"
        result += json.dumps(self.time, ensure_ascii=False, encoding='utf-8') +"\t"
        result += json.dumps(self.space, ensure_ascii=False, encoding='utf-8') + "\t"
        result += json.dumps(self.person, ensure_ascii=False, encoding='utf-8') + "\t"
        result += json.dumps(self.book, ensure_ascii=False, encoding='utf-8')+"\t"
        result += os.path.basename(self.fileName)
        return result.replace("[","").replace("]","").replace('"',"")

    def toJson(self):
        result = "{\n\tword : "+self.word +",\n\t"
        result += "relatedWord : "+json.dumps(self.relatedWord, ensure_ascii=False, encoding='utf-8') +",\n\t"
        result += "time : "+json.dumps(self.time, ensure_ascii=False, encoding='utf-8') +",\n\t"
        result += "space : "+json.dumps(self.space, ensure_ascii=False, encoding='utf-8') +",\n\t"
        result += "person : "+json.dumps(self.person, ensure_ascii=False, encoding='utf-8') +",\n\t"
        result += "book : "+json.dumps(self.book, ensure_ascii=False, encoding='utf-8') +"\n"
        result += "fileName : "+os.path.basename(self.fileName)+",\n\t"

        result += "}"
        return result