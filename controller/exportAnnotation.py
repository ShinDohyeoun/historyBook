# -*- coding:UTF-8 -*-

import subprocess
import common.config as config
import common.parse as parse
import cPickle

def exportAnnotation():
    categoryList = []
    for filename in subprocess.check_output('find '+config.srcPath+' -name "*.ann" -size +0', shell=True).split('\n'):
        if filename == "":
            continue
        f = open(filename, 'r')
        lines = f.readlines()
        categoryList.extend(parse.parsingAnnotation(lines, filename))
        f.close()



    #ordered되게 자료를 뽑기 위해서 파일오픈을 해서 쓴다...
    #order되지 않게 한다면 그냥 config에 있는 값을 가져오면 되는데.... 코드가 더러워졌다..
    f = open(config.dataPath+"categoryIndex.txt","r")
    lines = f.readlines()
    f.close


    categoryIdxOrdered = []
    for line in lines:
        data = line.strip().replace(")", "").split("(")
        categoryIdxOrdered.append(data[1])

    f = open(config.dataPath+"categoryList.txt","w")
    for code in categoryIdxOrdered:
        f.write(code + "\t")

        for category in categoryList:
            if category.categoryCode == code:
                f.write(category.word.encode('utf-8')+" ")
        f.write("\n")
    f.close()


"""
    f = open(config.commonPath+"categoryList.pkl", "wb")
    cPickle.dump(categoryList, f, cPickle.HIGHEST_PROTOCOL)
    f.close()
"""