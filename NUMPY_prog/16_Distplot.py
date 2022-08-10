import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5])
plt.show()

sns.distplot([0, 1,5,6, 2, 3, 4, 8, 5], hist=False)
plt.show()