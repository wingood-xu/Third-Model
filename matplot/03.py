import matplotlib.pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

a = ["猩球崛起3：终极之战", "敦刻尔克", "蜘蛛侠：英雄归来", "战狼2"]
b_16 = [15746, 312, 4497, 319]
b_15 = [12357, 156, 2045, 168]
b_14 = [2358, 399, 2358, 362]

x = range(len(a))

plt.figure(figsize=(15, 6), dpi=80)
plt.bar(x, b_14, width=0.1)
plt.bar([i + 0.1 for i in x], b_15, width=0.1)
plt.bar([i + 0.2 for i in x], b_16, width=0.1)
plt.xticks([i + 0.1 for i in x], a, fontproperties=my_font)

plt.show()
