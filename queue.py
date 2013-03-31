#! /usr/bin/python

import subprocess
class queue:
    
    def __init__(self):
        self.queue=[]
        self.frontp=-1
        return

    def enqueue(self,e):
        self.queue.insert(0,e)
        self.frontp+=1
        return True
    
    def dequeue(self):
        if self.frontp<0:
            print "queue empty"
            return 0
        e=self.queue.pop()
        print "removed from queue: "+str(e)
        self.frontp-=1
        return e

    def display(self):
        print self.queue
        return True

    def isEmpty(self):
        if self.frontp<0:
            print "true"
            return True
        print "false"
        return False

    def size(self):
        print self.frontp+1
        return self.frontp+1

    def front(self):
        if self.frontp<0:
            print "Queue empty"
            return False
        print "front: "+str(self.queue[self.frontp])
        return self.queue[self.frontp]

    def rear(self):
        if self.frontp<0:
            print "Queue empty"
            return False
        print "rear: "+str(self.queue[0])
        return self.queue[0]

    def reverse(self):
        self.queue.reverse()
        print self.queue
        return self.queue


if __name__=="__main__":
    
    q=queue()
    while True:
        
        print "1.enqueue\n2.dequeue\n3.isEmpty\n4.display\n5.size\n6.front\n7.rear\n8.exit\n9.clear\n10.reverse"
        i=input("choice:")
        if i==8:
            exit(0)
        if i==9:
            subprocess.call('clear')
        if i==1:
            e=input("enqueue:")
            q.enqueue(e)
        if i==2:
            q.dequeue()
        if i==3:
            q.isEmpty()
        if i==4:
            q.display()
        if i==5:
            q.size()
        if i==6:
            q.front()
        if i==7:
            q.rear()
        if i==10:
            q.reverse()

