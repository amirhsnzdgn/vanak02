import my_module


n1 = my_module.Node(0, 0)
n2 = my_module.Node(1, 1)
n3 = my_module.Node(0, 1)
n4 = my_module.Node(1, 2)
e1 = my_module.Element(n1, n2)
e2 = my_module.Element(n2, n3)
e3 = my_module.Element(n1, n3)
e4 = my_module.Element(n1, n4)

truss = my_module.Truss(e1, e2, e3, e4)

truss.show(outfile="./image.png")
