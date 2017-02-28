from model.ann import annData
from model.category import categoryClass
import common.config as config

def validAnnList(annList):
    topicCheck = False
    for ann in annList:
        if ann.type == "Topic" and topicCheck==False:
            topicCheck = True
        elif ann.type == "Topic" and topicCheck==True:
            return False
        elif ann.type == "EOP" and topicCheck==False:
            return False
        elif ann.type == "EOP" and topicCheck==True:
            topicCheck = False
    return True

def sortAnnList(dicIdx):
    annList = []
    for idx in sorted(dicIdx):
        annList.append(dicIdx[idx])
    return annList

def parsingAnn(lines):
    annList_tmp = dict()
    for line in lines:
        if "#" in line: continue
        try:
            line = line.strip()
            ann = annData()

            tmp1 = line.strip().split("\t")
            tmp2 = line.strip().split("\t")[1].split(" ")

            ann.idx = tmp1[0]
            ann.word = tmp1[2]
            ann.type = tmp2[0]
            ann.init_position = tmp2[1]
            ann.end_position = tmp2[2]
            annList_tmp[float(ann.init_position)+len(ann.end_position)/10000.0+float(ann.idx.replace("T",""))/1000000.0] = ann
        except IndexError as e:
            print("error in parsingAnn")
            print(e)


    return sortAnnList(annList_tmp)


def parsingAnnotation(lines, fileName):
    ann = dict()
    categoryList = []
    try:
        for line in lines:
            if "#" in line and "AnnotatorNotes" in line:
                tmp1 = line.strip().split("\t")
                tmp2 = tmp1[1].split(" ")

                if tmp1[2] in config.categoryCode:
                    category = categoryClass()
                    category.fileName = fileName
                    category.idx = tmp1[0]
                    category.wordIdx = tmp2[1]
                    category.categoryCode = tmp1[2]
                    category.categoryName = config.categoryCode[category.categoryCode]
                    categoryList.append(category)
                else:
                    continue

            elif "#" in line and "AnnotatorNotes" not in line:
                continue
            elif "T" in line and "\t" in line:
                tmp = line.strip().split("\t")
                ann[tmp[0]] = tmp[2]

        for category in categoryList:
            category.word = ann[category.wordIdx].decode('utf-8')
    except IndexError as e:
        print("error in parsingAnn")
        print(e)

    return categoryList

