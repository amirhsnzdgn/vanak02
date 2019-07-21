import glob


class Node:
    instance = {}

    def __new__(cls, name):
        if name in cls.instance:
            return cls.instance[name]

        res = super().__new__(cls)
        res._initialized = False
        return res

    @classmethod
    def count(cls):
        return len(cls.instance)

    def __init__(self, name):
        if not self._initialized:
            self.name = name
            self.parent = None
            self.children = []
            self.instance.update({name: self})
        self._initialized = True

    @property
    def has_parent(self):
        return self.name == 0

    @property
    def has_children(self):
        return self.children == []
        # return bool(self.children)

    def set_parent(self, parent: int):
        self.parent = Node(parent)
        self.parent.add_child(self)

    def add_child(self, child):
        self.children.append(child)

    def chain(self):
        if not self.has_parent:
            return [self]

        return self.parent.chain() + [self]



list_of_files = glob.glob('./files/*.txt')

for f in list_of_files:
    child_name = f[8:-4]
    parent_name = open(f).read()
    child_name = int(child_name)
    parent_name = int(parent_name)

    n = Node(child_name)
    n.set_parent(parent_name)


print(Node.count())
#
# answer = []
# for name, node in Node.instance.items():
#     if not node.has_children:
#         answer.append(name)
#
# print(len(answer))
