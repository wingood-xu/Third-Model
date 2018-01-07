import matplotlib.pyplot as plt
from matplotlib import font_manager
import random

my_font = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')
fit = plt.figure(figsize=(10, 6), dpi=80)

# x = range(2, 26, 2)
# y = [15, 13, 14.5, 17, 20, 25, 26, 26, 24, 22, 18, 15]
#
# plt.plot(x,y)
# plt.xticks(x[::2])
x = range(120)
random.seed(10)
y = [random.uniform(20, 35) for i in range(120)]
random.seed(11)
y1 = [random.uniform(20, 35) for j in range(120)]

plt.plot(x, y, linestyle=':', color='r', label='今天')
plt.plot(x, y1, linestyle='-', color='g', label='明天')
_x_ticks = ["10点{}分".format(i) for i in x if i < 60]
_x_ticks += ["11点{}分".format(i - 60) for i in x if i >= 60]
plt.xticks(x[::5], _x_ticks[::5], rotation=45, fontproperties=my_font)
plt.xlabel('时间', fontproperties=my_font)
plt.ylabel('温度(°C)', fontproperties=my_font)
plt.title('10点到12点每分钟温度变化情况', fontproperties=my_font)
plt.legend(prop=my_font, loc='best')

plt.show()
