
class array2d:

    def __init__(self,r,c):
        self.array=[[0]*c for x in xrange(r)]
    
    def transpose(self):
        self.transpose=map(lambda *row: list(row), *self.array)
        print self.transpose
        return self.transpose

    def display(self):
        print self.array

if __name__=="__main__":
    row=3
    col=4
    a=array2d(row,col)

    for i in xrange(row):
        for j in xrange(col):
            a.array[i][j]=i+j
    a.display()
    a.transpose()
    a.display()
