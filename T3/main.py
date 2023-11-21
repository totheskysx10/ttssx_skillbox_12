class MyDict(dict):
    def get(self, key):
        if key in self:
            return self[key]
        else:
            return 0

mydict = MyDict()
mydict['z'] = 1
mydict['x'] = 2
mydict['e'] = 3
mydict['t'] = 4


print(mydict.get('z'))
print(mydict.get('c'))