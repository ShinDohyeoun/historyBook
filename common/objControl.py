import cPickle


def objectWrite(fileName, data):
    f = open(fileName, "wb")
    cPickle.dump(data , f, cPickle.HIGHEST_PROTOCOL)
    f.close()

def objRead(fileName):
    f = open(fileName, "rb")
    data = cPickle.load(f)
    f.close()
    return data