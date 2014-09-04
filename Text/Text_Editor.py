'''
Created on 17.08.2014

@author: Thomas
'''

from tkinter import *

class Dapeton(Frame):
    
    def __init__(self, parent):
        Frame.__init__(self, parent, background = "white")
        
        self.parent = parent
        
        self.initUI()
        
    def initUI():
        
        self.parent.title()

def main():
    pass

if __name__ == '__main__':
    main()