#-*- coding: utf-8-*-
#!!!we talk only about Python2 in these examples!!!
# two types that deal with text:
#---->str 
#---->unicode

#for example:
str_type = 'some text'
print type(str_type)

unicode_type = u'some text'
print type(unicode_type)

#print them
print str_type
print unicode_type

#are these equal?
'some text' == u'some text'


###############################################################
#decode bytes
print 'decoded bytes from ascii:', 'some text'.decode('ascii')
print 'decoded bytes from utf-8:', 'some text'.decode('utf-8')
print 'decoded bytes from utf-8:', u'some text: ÅÅÅ'.encode('utf-8')
#this works
print 'some str stuff'
#this works too
print u'some unicode stuff: ÅÅÅÅ'


###############################################################
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
