from model.dictionary import dictionaryClass
import subprocess
import common.config as config
import common.objControl as objControl
import common.cmd as cmdControl
import cPickle

class exportAnn():
    dictionary = dictionaryClass()

    def readAnn(self):
        for filename in subprocess.check_output('find ' + config.srcPath + ' -name "*.ann" -size +0', shell=True).split(
                '\n'):
            print(filename)

            if filename == "":
                continue
            f = open(filename, 'r')
            while True:
                line = f.readline()
                if not line: break
                if "#" in line: continue
                word = line.strip().replace(" ", "\t").split("\t")
                if len(word) == 5:
                    self.dictionary.append(word[4], word[1], filename, word[2], word[3])
            f.close()

    def to_pkl(self):
        self.readAnn()
        objControl.objectWrite(config.dataPath+"dicList.pkl", self.dictionary.dicList)

    def to_txt(self):
        self.readAnn()
        for word in self.dictionary.dicList.keys():
            for type in self.dictionary.dicList[word].keys():
                print(word.decode('utf-8') + " : " + type + " : " + str(len(self.dictionary.dicList[word][type])))
                f = open(config.dataPath + "dicList.txt", "a")
                f.write(word + " : " + type + " : " + str(len(self.dictionary.dicList[word][type])) + "\n")
                f.close()


class importAnn():
    invalidType = config.invalidType

    # global value
    dictionary = dictionaryClass()

    def readDicList(self):
        self.dictionary.dicList = objControl.objRead(config.dataPath+"dicList.pkl")

    def invalidCheck(self, filename):
        try:
            f = open(filename.replace(".txt", ".ann"), 'r')
        except IOError, e:
            return False
        while True:
            line = f.readline()
            if "#" in line: continue
            if not line: break

            for type in self.invalidType:
                if type in line:
                    return True
        f.close()
        return False



    def autoTagging(self, path):
        self.readDicList()
        self.dictionary.filteringDic()

        txtFiles = cmdControl.findTxtFile(path)
        for txtFile in txtFiles:
            if self.invalidCheck(txtFile):
                print(txtFile+ " already processed by person")
                continue
            else:
                f = open(txtFile, 'r')
                inputData = f.read();
                f.close()

                outputData = ""
                count = 1
                for word in self.dictionary.dicList.keys():
                    if word in inputData:
                        for type in self.dictionary.dicList[word].keys():
                            outputData += "T" + str(count) + "\t" + type + " " + str(
                                inputData.decode('utf-8').index(word.decode('utf-8'))) + \
                                          " " + str(inputData.decode('utf-8').index(word.decode('utf-8')) + len(
                                word.decode('utf-8'))) + "\t" + word + "\n"
                            count += 1

                # print(outputData)
                f = open(txtFile.replace("txt", "ann"), 'w')
                f.write(outputData)
                f.close()