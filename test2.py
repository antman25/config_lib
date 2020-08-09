#!/usr/bin/python3

import Config
import json

obj1 = { 'key1' : 'val1' }
obj2 = { 'key2' : 'val2',
         'key3' : [ 0, 1] }

a = Config.AttributeDict(obj1)
b = Config.AttributeDict(obj2)
c = {}
c.update(a)
c.update(b)

print (a)
print (b)
print (c)
print (c.keys())
print (a.key1)
print (c['key3'])

j = json.dumps(c, indent = 4)   
print (j)
#print (c)
