
class queue:

    def __init__(self):
        self.queue=[]
        return

    def enqueue(self):
        return
    
    def dequeue(self):
        return

    def display(self):
        return

if __name__=="__main__":

   q=queue(3)
    while True:
        print "1.push\n2.pop\n3.peek\n4.display\n5.exit"
        i=input("choice:")
        if i==5:
            exit(0)
        if i==1:
            print "Enter element to push"
            e=input(":")
            s.push(e)
        if i==2:
            s.pop()
        if i==3:
            s.peek()
        if i==4:
            s.display()
