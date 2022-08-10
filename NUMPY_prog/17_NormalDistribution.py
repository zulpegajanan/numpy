#Normal Distribution is also called the Gaussian Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.normal(size=(2, 3))
print(x)


sns.distplot(random.normal(size=1000), hist=False)
plt.show()