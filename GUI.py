import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['axes.unicode_minus']=False
x=np.linspace(0,5,20)
x1=np.linspace(0,10,10)
X=[2,1.5,1,0.5]

def discrete_sin():
    y1=2*np.sin(0.6*np.pi*x)
    plt.title('2*sin(0.6πt)')
    plt.grid(True)
    plt.stem(x,y1)
    plt.show()

def discrete_ex():
    A=2
    a=0.6
    y4=A*a**x1
    plt.grid(True)
    plt.title('2*0.6^x')
    plt.stem(x1,y4)
    plt.show()

def discrete_step():
    def step(t):
        r=np.where(t>=-2.0,1.5,0.0)
        return r
        n=np.arange(-5,3)
        plt.ylim(0,2)
        plt.title('阶跃信号')
        plt.grid(True)
        plt.stem(n,step(n))
        plt.show()
def discrete_impulse():
    def impulse(temp):
        r=np.where(temp==3.0,1.5,0.0)
        return r
        m=np.arange(-4,8)
        plt.ylim(0,2)
        plt.title('冲激信号')
        plt.grid(True)
        plt.stem(m,impulse(m))
        plt.show()

from tkinter import *
tk=Tk()
tk.title("离散信号图像")
Button(tk,text="离散sin",command=discrete_sin).pack(side=LEFT)
Button(tk,text="离散e^x",command=discrete_ex).pack(side=LEFT)
Button(tk,text="离散阶跃",command=discrete_step).pack(side=LEFT)
Button(tk,text="离散冲击",command=discrete_impulse).pack(side=RIGHT)
tk.mainloop()
