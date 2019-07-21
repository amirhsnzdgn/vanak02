class StrangeList(list):
    def __getattribute__(self, item):  # item= '_1'
        if item.startswith('_') and item[1:].isdigit():
            ind = int(item[1:])
            return self[ind]
        return super().__getattribute__(item)

    def __setattr__(self, key, value):
        if key.startswith('_') and key[1:].isdigit():
            ind = int(key[1:])
            self[ind] = value
        else:
            super().__setattr__(key, value)


tup = ['one', 'two', 'three', 'four']
st = StrangeList(tup)

print(st._2)
st._2 = 'THREE'
print(st._2)
print(st[2])




