import sys
sys.path.append("/var/www/brat/myscript/script_py")
import common.config as config
import common.cmd as cmdControl
import controller.ann as ann


srcBooks = config.srcBooks

print("Name\tTotal\tProcessed\tUnprocessed\tPercentage")
ann = ann.importAnn()

for book in srcBooks:
    txtFiles = cmdControl.findTxtFile(config.srcPath+book)
    total = len(txtFiles)
    processed = 0
    for txtFile in txtFiles:
        if ann.invalidCheck(txtFile) == True:
            processed+=1

    print(book+"\t"+str(total)+"\t"+str(processed)+"\t"+str(total-processed)+"\t"+str(float(processed)/total*100))