import os
import common.config as config
import common.objControl as objControl
import common.parse as parse

from model.topic import topicClass

def findTopic():
    dicList = objControl.objRead(config.dataPath + "dicList.pkl")
    fileList = []
    for word in dicList.keys():
        for type in dicList[word].keys():
            if type == "Topic":
                for posInfo in dicList[word][type]:
                    if posInfo.fileName in fileList:
                        continue
                    else:
                        fileList.append(posInfo.fileName)
    return fileList

def classifyDetail(topic, annLists):
    topicList = []
    for index, annData in enumerate(annLists):
        if annData.type == "Topic":
            topic.word = annData.word
        elif annData.type == "RelatedWord":
            topic.relatedWord.append(annData.word)
        elif annData.type == "Time":
            topic.time.append(annData.word)
        elif annData.type == "Space":
            topic.space.append(annData.word)
        elif annData.type == "Person":
            topic.person.append(annData.word)
        elif annData.type == "Book":
            topic.book.append(annData.word)
        elif annData.type == "EOP":
            if index == 0:
                continue
            newTopic = topicClass()
            newTopic.fileName = topic.fileName
            topicList.extend(classifyDetail(newTopic,annLists[index:]))
            break

    if topic.word != "":
        topicList.append(topic)

    return topicList

def fillDetail(hasTopic_fileList):
    result = []
    for fileName in hasTopic_fileList:
        f = open(fileName.replace("txt","ann"),"r")
        annLists = parse.parsingAnn(f.readlines())
        if parse.validAnnList(annLists) == False:
            print(fileName+" has ann structure error")
            continue

        f.close()
        topic = topicClass()
        topic.fileName = os.path.basename(fileName)
        result.extend(classifyDetail(topic, annLists))

    return result

def extract():
    hasTopic_fileList = findTopic()
    completed_topicList = fillDetail(hasTopic_fileList)

    f = open(config.dataPath+"topicList.txt", "w")
    for topic in completed_topicList:
        print(topic.toJson())
        f.write(topic.toCSV()+"\n")
    f.close()

"""
        print(topic.word + " : " +topic.fileName)
        output = ""
        for related in topic.relatedWord:
            output+= related+ " "
        print("related word : "+output)

"""