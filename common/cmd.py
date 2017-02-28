import subprocess

def findTxtFile(path):
    fileList = subprocess.check_output('find ' + path + ' -name "*.txt"', shell=True).split("\n")
    fileList.pop()
    return fileList

def findAnnFile(path):
    fileList = subprocess.check_output('find ' + path + ' -name "*.ann"', shell=True).split("\n")
    fileList.pop()
    return fileList