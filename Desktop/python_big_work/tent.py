import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from mpl_toolkits.mplot3d import Axes3D



def lineChart1():
    """单一曲线"""
    x = np.linspace(-1, 1, 50) #等分区间[-1 1]
    y = 2*x + 1
    plt.figure()               #创建一幅图
    plt.plot(x, y)             #画一条线，plot是折线
    plt.show()                 #显示这幅图

def lineChart2():
    """多条曲线"""
    x = np.linspace(-3, 3, 50)
    y1 = 2 * x + 1
    y2 = x ** 2
    plt.figure()             #创建一幅图
    plt.plot(x, y1)          #画一条线
    plt.plot(x, y2)          #在画一条线
    plt.show()

def lineChart3():
    """设置托条曲线的样式"""
    x = np.linspace(-3, 3, 50)
    y1 = 2 * x + 1
    y2 = x ** 2
    plt.figure(num = 3, figsize = (5,5))    #编号为3；大小为(8, 5)
    plt.plot(x, y1)
    plt.plot(x, y2, color = "red", linewidth=1.0, linestyle='--')
    plt.show()
    """
    # 曲线的颜色属性(color)为红色;曲线的宽度(linewidth)为1.0；
      曲线的类型(linestyle)为虚线. 使用plt.show显示图像
    """

def lineChart4():
    """设置座标轴样式"""
    x = np.linspace(-3, 3, 50)
    y1 = 2 * x + 1
    y2 = x ** 2
    plt.figure(num = 3, figsize = (5,5))    #编号为3；大小为(8, 5)
    plt.plot(x, y1)
    plt.plot(x, y2, color = "red", linewidth=1.0, linestyle='--')
    plt.xlim((-1, 2))  #使用plt.xlim设置x坐标轴范围
    plt.ylim((-2, 3))
    plt.xlabel('I am x') #使用plt.xlabel设置x坐标轴名称
    plt.ylabel('I am y')
    plt.show()
    plt.show()

def lineChart5():
    """重新定XY轴刻度"""
    x = np.linspace(-3, 3, 50)
    y1 = 2 * x + 1
    y2 = x ** 2
    plt.figure(num = 3, figsize = (8,5))    #编号为3；大小为(8, 5)
    plt.plot(x, y1)
    plt.plot(x, y2, color = "red", linewidth=1.0, linestyle='--')
    plt.xlim((-1, 2))  # 使用plt.xlim设置x坐标轴范围
    plt.ylim((-2, 3))
    plt.xlabel('I am x') #使用plt.xlabel设置x坐标轴名称
    plt.ylabel('I am y')
    new_ticks = np.linspace(-1, 2, 5)
    print(new_ticks)
    plt.xticks(new_ticks)
    plt.yticks([-2, -1.8, -1, 1.22, 3], [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])
    """
    'r'是防止字符转义的 如果路径中出现'\t'的话 不加r的话\t就会被转义 而加了'r'之后'\t'就能保留原有的样子
    使用plt.yticks设置y轴刻度以及名称：刻度为[-2, -1.8, -1, 1.22, 3]；
    对应刻度的名称为[‘really bad’,’bad’,’normal’,’good’, ‘really good’]. 
    """
    plt.show()

def lineChart6():
    x = np.linspace(-3, 3, 50)
    y1 = 2 * x + 1
    y2 = x ** 2
    plt.figure()
    plt.plot(x, y2)
    plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
    plt.xlim((-1, 2))
    plt.ylim((-2, 3))
    new_ticks = np.linspace(-1, 2, 5)
    plt.xticks(new_ticks)
    plt.yticks([-2, -1.8, -1, 1.22, 3], ['$really\ bad$', '$bad$', '$normal$', '$good$', '$really\ good$'])
    ax = plt.gca()    #使用plt.gca获取当前坐标轴信息
    ax.spines['right'].set_color('red') #右边框是红的
    ax.spines['top'].set_color('blue')  #上边框是蓝的
    ax.xaxis.set_ticks_position('bottom') #使用.xaxis.set_ticks_position设置x坐标刻度数字或名称的位置：
                                          # （所有位置：top，bottom，both，default，none）
    ax.spines['bottom'].set_position(('data', 0))  #
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))
    #使用.spines设置边框：y轴；
    # 使用.set_position设置边框位置：x=0的位置；
    # （位置所有属性：outward，axes，data） 使用plt.show显示图像.
    plt.show()

def lineChart7():
    """lengend图例"""
    x = np.linspace(-3, 3, 50)
    y1 = 2 * x + 1
    y2 = x ** 2

    plt.figure()
    # set x limits
    plt.xlim((-1, 2))
    plt.ylim((-2, 3))
    # set new sticks
    new_sticks = np.linspace(-1, 2, 5)
    plt.xticks(new_sticks)
    # set tick labels
    plt.yticks([-2, -1.8, -1, 1.22, 3],
               [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])
    l1, = plt.plot(x, y1, label='hahaha')
    l2, = plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--', label=u"lala")
    plt.legend(loc='upper right') #legend将要显示的信息来自于上面代码中的 label.
                                # 所以我们只需要简单写下一下代码, plt 就能自动的为我们添加图例.
                                 #参数 loc='upper right' 表示图例将添加在图中的右上角.
    plt.legend(handles=[l1, l2], labels=['up', 'down'], loc='best') #
    #如果我们想单独修改之前的 label 信息, 给不同类型的线条设置图例信息.
    # 我们可以在 plt.legend 输入更多参数. 如果以下面这种形式添加 legend,
    # 我们需要确保, 在上面的代码 plt.plot(x, y2, label='linear line')
    # 和 plt.plot(x, y1, label='square line') 中有用变量 l1 和 l2 分别存储起来.
    # 而且需要注意的是 l1, l2,要以逗号结尾, 因为plt.plot() 返回的是一个列表.
    #这样我们就能分别重新设置线条对应的 label 了.
    plt.show()

def lineChart8():
    """给图项标注信息"""
    x = np.linspace(-3, 3, 50)
    y = 2 * x + 1
    plt.figure(num=1, figsize=(8, 5), )
    plt.plot(x, y)

    ax = plt.gca()
    ax.xaxis.set_ticks_position('bottom') #坐标轴上数字位置
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data', 0)) #让底部坐标轴在y=0线上
    ax.spines['left'].set_position(('data', 0))#让左部坐标轴在y=0线上
    ax.spines['right'].set_color('none') #让右部坐标轴消失
    ax.spines['top'].set_color('none')#让上部坐标轴消失

    """再画出一条虚线
       用plt.plot([x0, x0,], [0, y0,], 'k--', 
       linewidth=2.5) 画出一条垂直于x轴的虚线.
    """
    x0 = 1
    y0 = 2 * x0 + 1
    plt.plot([x0, x0, ], [0, y0, ], 'k--', linewidth=2.5)
    # set dot styles
    plt.scatter([x0, ], [y0, ], s=50, color='b') #x0,y0这个点用散点图表示

    """其中参数xycoords='data' 是说基于数据的值来选位置, xytext=(+30, -30)
       和 textcoords='offset points' 对于标注位置的描述 和 xy 偏差值,
        arrowprops是对图中箭头类型的一些设置
    ."""
    plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
                 textcoords='offset points', fontsize=16,
                 arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))

    """
    其中-3.7, 3,是选取text的位置, 空格需要用到转字符\ ,fontdict设置文本字体.
    """
    plt.text(-3.7, 3, r'$This\ is\ the\ some\ text. \mu\ \sigma_i\ \alpha_t$',
             fontdict={'size': 16, 'color': 'r'})
    plt.show()
    """
    xy=(横坐标，纵坐标)  箭头尖端
    xytext=(横坐标，纵坐标) 文字的坐标，指的是最左边的坐标
    arrowprops键	描述
    width	箭头宽度，以点为单位
    frac	箭头头部所占据的比例
    headwidth	箭头的底部的宽度，以点为单位
    shrink	移动提示，并使其离注释点和文本一些距离
    **kwargs	matplotlib.patches.Polygon的任何键，例如facecolor
    | 参数 | 坐标系 | 
    | 'figure points' | 距离图形左下角的点数量 | 
    | 'figure pixels' | 距离图形左下角的像素数量 | 
    | 'figure fraction' | 0,0 是图形左下角，1,1 是右上角 | 
    | 'axes points' | 距离轴域左下角的点数量 | 
    | 'axes pixels' | 距离轴域左下角的像素数量 | 
    | 'axes fraction' | 0,0 是轴域左下角，1,1 是右上角 | 
    | 'data' | 使用轴域数据坐标系 |
    
    """

def lineChart9():
    """\tick 能见度"""
    x = np.linspace(-3, 3, 50)
    y = 0.1 * x

    plt.figure()
    # 在 plt 2.0.2 或更高的版本中, 设置 zorder 给 plot 在 z 轴方向排序
    plt.plot(x, y, linewidth=10, zorder=1)
    plt.ylim(-2, 2)
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))
    """
    其中label.set_fontsize(12)重新调节字体大小，bbox设置目的内容的透明度相关参，
    facecolor调节 box 前景色，edgecolor 设置边框， 本处设置边框为无，alpha设置透明度. 
    """
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(12)
        # 在 plt 2.0.2 或更高的版本中, 设置 zorder 给 plot 在 z 轴方向排序
        label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7, zorder=2))
    plt.show()


def threedGraph():
    """绘制3D图形"""
    fig = plt.figure()
    ax = Axes3D(fig) #先定义一个图像窗口，在窗口上添加3D坐标轴
    X = np.arange(-4, 4, 0.25)
    Y = np.arange(-4, 4, 0.25)
    X, Y = np.meshgrid(X, Y)  # x-y 平面的网格 #
    R = np.sqrt(X ** 2 + Y ** 2)
    # height value
    Z = np.sin(R)
    #做出一个三维曲面，并将一个 colormap rainbow 填充颜色，
    # 之后将三维图像投影到 XY 平面上做一个等高线图。 plot 3D 图像：
    #rstride 和 cstride 分别代表 row 和 column 的跨度。
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
    ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.get_cmap('rainbow'))
    #如果 zdir 选择了x，那么效果将会是对于 XZ 平面的投影
    ax.set_zlim(-2, 2)
    plt.show()
    plt.close()

lineChart8()
