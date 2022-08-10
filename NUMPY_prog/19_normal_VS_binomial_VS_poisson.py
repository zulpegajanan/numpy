from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
# The main difference is that normal distribution is continous whereas binomial is discrete, but if there are enough data points it will be quite similar to normal distribution with certain loc and scale.
sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')
sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')
plt.show()