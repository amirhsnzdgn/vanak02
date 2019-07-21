class WeirdList(list):
    def __getitem__(self, item: str):
        item = int(item)
        return super().__getitem__(item-1)

    def __setitem__(self, key:str, value):
        key = int(key) - 1
        return super().__setitem__(key, value)

tup = [10, 20, 30, 40]
wt = WeirdList(tup)

print(tup[0], wt['1'])
tup[0] = 1000
wt['1'] = 1000
print(tup[0], wt['1'])