class NoDuplicated:
    instances = {}
    def __new__(cls, name):
        if name in cls.instances:
            return cls.instances[name]

        res = super().__new__(cls)
        res._initialized = False
        return res

    def __init__(self, name):
        if not self._initialized:
            self.instances.update({name: self})
            self.name = name
        self._initialized = True




a = NoDuplicated("A")
b = NoDuplicated("A")
c = NoDuplicated("B")

print(id(a), id(b), id(c), sep='\n')