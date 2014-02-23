#-*- coding: utf-8-*-
import sys
import codecs
#writing to a file requires bytes
with open ('test', 'w') as f:
        f.write('ÄÄÄÄ')
        f.write(u'ÖÖÖ'.encode('utf-8'))

#text read from the file is in bytes -> str
with open('test', 'r') as f:
        res = f.readline()
        print 'type:', type(res)
        unicode_res = res.decode('utf-8')
        print unicode_res.encode(sys.stdout.encoding), type(unicode_res)

#writing to a file without encoding it
#error, because print tries to encode into 'ascii'
#with open('test', 'a+') as f:
    #f.write(u'ÅÅÅÅ')

#when printing, it is not neccessary to explicitly encode
print u'ÅÅÅÅ'.encode('utf-8')
#-> it's okay to write like this
print u'ÅÅÅÅ'

print "printing contents of the file"
with codecs.open('testing', 'r', 'utf-8') as f:
    print f
    line = f.readline()
    print line, 'type:', type(line) 

with open('testing', 'r') as f:
    print f
    line = f.readline()
    print line, 'type:', type(line) 
