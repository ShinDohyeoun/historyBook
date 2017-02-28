import common.config as config

class posInfo:
    fileName = None
    fileBaseName = None
    init_position = None
    end_position = None

class dictionaryClass:
    dicList = None
    validType = config.validType

    def __init__(self):
        self.dicList = dict()


    def append(self, word, type, filename, init_position, end_position):
        if word in self.dicList:
            if type in self.dicList[word]:
                self.dicList[word][type].append(self.setPosInfo(filename, init_position, end_position))
            else:
                self.dicList[word][type] = [self.setPosInfo(filename, init_position, end_position)]
        else:
            tmp = dict()
            tmp[type]= [self.setPosInfo(filename, init_position, end_position)]
            self.dicList[word]=tmp

    def setPosInfo(self, filename, init_position, end_position):
        info = posInfo()
        info.fileName = filename
        info.fileBaseName = filename[filename.rfind('/') + 1:]
        info.init_position = init_position
        info.end_position = end_position
        return info

    def getrepetitionKeys(self):
        repetitionKeys = []

        for word in self.dicList.keys():
            if len(self.dicList[word]) >= 2:
                repetitionKeys.append(word)
        return repetitionKeys


    def filteringDic(self):
        for word in self.dicList.keys():
            if len(word.decode('utf-8')) <= 1:
                del self.dicList[word]
            else:
                for type in self.dicList[word].keys():
                    if type not in self.validType:
                        del self.dicList[word][type]

