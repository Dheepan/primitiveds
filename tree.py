#! /usr/bin/python

import subprocess

class Node(object):

    def __init__(self,data):
        self.data=data
        self.children=[]
        return

    def add_child(self,obj):
        self.children.append(obj)
        return True

    def is_leaf(self):
        if len(self.children)==0:
            return True
        return False

    def display(self):
        print self.data
        print self.children

    def traverse(self):
        if len(self.children)==0:
            return
        else:
            for c in self.children:
                print c.data
                c.traverse()


if __name__=="__main__":

    t=Node("root")
    node=None
    prev=t
    while True:
        print "1.createnode\n2.addchild\n3.display\n4.remove\n5.exit\n6.clear\n7.Traverse"
        i=input("choice:")
        if i==5:
            exit(0)
        if i==1:
            j=input("enter a number")
            node=Node(j)
        if i==2:
            prev.add_child(node)
            prev=node
        if i==3:
            t.display()
        if i==4:
            t.remove()
        if i==6:
            subprocess.call(['clear'])
        if i==7:
            t.traverse()
