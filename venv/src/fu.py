import matplotlib
import numpy as np
from matplotlib import pyplot as plt

zhfont1 = matplotlib.font_manager.FontProperties(fname="SimHei.ttf")

x = np.arange(1, 11)
y = 2 * x + 5
plt.title("菜鸟教程 - 测试", fontproperties=zhfont1)

# fontproperties 设置中文显示，fontsize 设置字体大小
plt.xlabel("x 轴", fontproperties=zhfont1)
plt.ylabel("y 轴", fontproperties=zhfont1)
plt.plot(x, y,",r")
plt.show()