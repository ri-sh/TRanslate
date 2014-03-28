# translating words using google translation api
#install goslate a python module for translating using google translate api i n windows easy_install goslate
#c:\\Users\\kiit\\SkyDrive\\Pictures\\new.txt
import codecs
from threading import Thread
import time
import goslate
gs = goslate.Goslate()
f=codecs.open("input.txt",encoding='utf-8',mode='r').read()
d= codecs.open ("output.txt",encoding='utf-8',mode='w')
hosts=f.split("\n")
resp=gs.translate(f,'hi')
d.write(resp)


"""class GetUrlThread(Thread):
    def __init__(self, url):
        self.url = url
        super(GetUrlThread, self).__init__()

    def run(self):
        if self.url=="\n":
            resp="\n"

        else:
            resp = gs.translate(self.url,'fr')
        print resp

def get_responses():
    urls =hosts
    start = time.time()
    threads = []
    for url in urls:
        t = GetUrlThread(url)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print "Elapsed time: %s" % (time.time()-start)

get_responses()

"""
