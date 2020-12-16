import numpy as np
import random
class SparseVector():

    def __init__(self,n,contents):
        self.n = n
        self.contents = contents 
        self.x = sorted(contents,key=self.getkey)
        self.avg = self.calc_avg()

    def getkey(self,item):
        # https://www.pythoncentral.io/how-to-sort-a-list-tuple-or-object-with-sorted-in-python/
        return item[1]

    def __mul__(self,other):
        """
        Perform dot prod of x * y
        """
        return self._dot(other)
    
    def _dot(self,other):
        prods = []
        for x_i,y_i in zip(self.x,other.x):
            x_i,y_i = x_i[0],y_i[0]
            prod = x_i * y_i
            prods.append(prod)
        return sum(prods)

    def calc_avg(self):
        sum = 0
        for x_i in self.x[0]:
            sum += x_i
        return sum/self.n
    
def cov(x,y):
    assert(x.n == y.n)

    # term 1
    prods = []
    for x_i,y_i in zip(x.x,y.x):
        x_i,y_i = x_i[0],y_i[0]
        prod = x_i * y_i
        prods.append(prod)
    d_prod = sum(prods)
    term1 = d_prod/x.n

    # term 2 
    term2 = x.avg * y.avg
    
    #term2 = (sum(self.x) * sum(other.x))/self.n**2
    return term1 - term2

def main():
    x = [(-0.946, 6),
        (-0.541, 11),
        ( 0.211, 61),
        (-0.966, 62),
        (-0.380, 91),
        (-0.736, 101),
        ( 0.743, 123),
        (-0.426, 139),
        (-0.038, 159),
        ( 0.787, 195)]

    y =  [(-0.849, 3),
        ( 0.579, 6),
        (-0.876, 57),
        ( 0.933, 62),
        (-0.323, 69),
        ( 0.008, 101),
        ( 0.953, 108),
        ( 0.522, 116),
        ( 0.100, 139),
        ( 0.106, 143),
        (-0.162, 159),
        (-0.594, 161),
        (-0.196, 167),
        ( 0.379, 195)]

    x = SparseVector(200,x)
    y = SparseVector(200,y)

    test = x * y

    print("x avg = ", x.avg)
    print("y avg = ", y.avg)

    res = cov(x,y)
    print(res)

    #res2 = np.cov(x.x,y.x)
    #print(res2)

if __name__ == "__main__":
    main()