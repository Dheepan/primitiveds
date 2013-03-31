#! /usr/bin/python
import subprocess

class stack:
   
   #constructor
    def __init__(self):
        self.stack=[]
        self.top=0
        return

    #push 
    def push(self,e):
        self.stack.append(e)
        self.top+=1
        return True

     #pop
    def pop(self):
        if self.top==0:
            print "stack empty, cannot pop anymore"
            return False
        self.top-=1
        e=self.stack.pop()
        print "popped: "+str(e)
        return e

    #peek
    def peek(self):
        if self.top==0:
            print "Stack empty, nothing to peek"
            return False
        print self.stack[self.top-1]
        return self.stack[self.top-1]

    #display
    def display(self):
        print self.stack

    #isEmpty
    def isEmpty(self):
        if self.top==0:
            print "true"
            return True
        print "false"
        return False

    #size
    def size(self):
        print self.top
        return self.top

if __name__=="__main__":
    
    s=stack()
    while True:
        
        print "1.push\n2.pop\n3.peek\n4.display\n5.isEmpty\n6.size\nn8.exit\n9.clear"
        i=input("choice:")
        if i==8:
            exit(0)
        if i==9:
            subprocess.call('clear')
        if i==1:
            e=input("push:")
            s.push(e)
        if i==2:
            s.pop()
        if i==3:
            s.peek()
        if i==4:
            s.display()
        if i==5:
            s.isEmpty()
        if i==6:
            s.size()

