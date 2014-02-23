#what is the purpose of the following line?
#-*- coding: utf-8-*-
#this line tells that the text here should be encoded using utf-8

#decode bytes
print 'decoded bytes from ascii:', 'some text'.decode('ascii')
print 'decoded bytes from utf-8:', 'some text'.decode('utf-8')
print 'encoded bytes using utf-8:', u'some text: ÅÅÅ'.encode('utf-8')
#this works
print 'some str stuff'
#this works
print u'whatever'
#this works 
print u'some unicode stuff: ÅÅÅÅ'
#this works too if encoding specified
print 'some unicode stuff: ÅÅÅÅ'
