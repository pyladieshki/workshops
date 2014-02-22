#-*- coding: utf-8-*-
#writing to a file requires bytes
with open ('test', 'w') as f:
        f.write('ÄÄÄÄ')
        f.write(u'ÖÖÖ'.encode('utf-8'))

#text read from the file is in bytes -> str
with open('test', 'r') as f:
        res = f.readline()
        print 'type:', type(res)
        unicode_res = res.decode('utf-8')
        print unicode_res.encode('utf-8'), type(unicode_res)

#writing to a file without encoding it
#error, because print tries to encode into 'ascii'
#with open('test', 'a+') as f:
    #f.write(u'ÅÅÅÅ')

print u'ÅÅÅÅ'.encode('utf-8')

