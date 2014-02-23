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
print 'printing str type text:', str_type
print 'printing unicode type text:', unicode_type

#are these equal?
print 'some text' == u'some text'
#equal because bytes are decoded with ascii encoding
