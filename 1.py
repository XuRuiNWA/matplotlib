from matplotlib import  pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.font_manager as fm
kaiti=fm.FontProperties(fname='C:\WINDOWS\FONTS\STKAITI.TTF')
x=np.linspace(-2*np.pi,2*np.pi,1024,endpoint=True)
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1, 0, 1],
           [r'$-1$', r'$0$', r'$1$'])
c=np.sin(x)*np.sin(x)*np.sin(x)*np.sin(x)*np.sin(x)
t=np.cos(x)*np.cos(x)*np.cos(x)*np.cos(x)*np.cos(x)
plt.plot(x,c,color='black',marker='.',label='五次正弦')
plt.plot(x,t,color='red',marker='.',label='五次余弦')
plt.xlabel('时间',fontproperties=kaiti)
plt.ylabel('温度',fontproperties=kaiti)
plt.legend(prop=kaiti)
plt.title('绘制的图',fontproperties=kaiti)
plt.show()

