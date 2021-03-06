from matplotlib import  pyplot as plt
import  numpy as np
plt.style.use('ggplot')
plt.rcParams['font.sans-serif']=['Microsoft YaHei']
name=('李晓梦','陈京云','樊亚雪','邱其雅','郑诗琪')
height_1=[173,189,178,167,176]
weight_1=[52,49,46,51,49]
plt.figure(figsize=(10,5))
bar_width = 0.5
index_weight_1= np.arange(len(name))  
index_height_1 =index_weight_1 + bar_width  

rect1=plt.bar(index_weight_1,height_1, alpha=0.7,width = bar_width,  facecolor = 'purple', edgecolor = 'b', lw=1, label='身高')
recr2=plt.bar(index_height_1 ,weight_1, alpha=0.7,width = bar_width,  facecolor = 'lightblue', edgecolor = 'b', lw=1, label='体重')
def add_labels(rects):
    for rect in rects:
        height=rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2,height,height,ha='center',va='bottom')
        rect.set_edgecolor('white')
add_labels(rect1)
add_labels(recr2)
plt.legend()
plt.xticks(index_height_1 -  bar_width/2,name)
plt.title('小姐姐一览表')
plt.ylabel('number')
plt.xlabel('name')
plt.show()
