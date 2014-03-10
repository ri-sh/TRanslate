# translating words using google translation api
#install goslate a python module for translating using google translate api i n windows easy_install goslate
import goslate
gs = goslate.Goslate()
text= raw_input('enter the string to be translated ')
text = text.strip()
dest=raw_input("enter Destination language for example hi for hindi ")
dest = dest.strip()
print " translation of " +text+" in "+dest+" is :"
print gs.translate(text, dest)
