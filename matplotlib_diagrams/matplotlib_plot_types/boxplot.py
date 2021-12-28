import numpy as np
import matplotlib.pyplot as plt

mu,sigma = 172,4
values = np.random.normal(mu,sigma,200)
# Our mean value is 172, our standard deviation 4 and we generate
# 200 values.
plt.boxplot(values)
plt.title("Student's Height")
plt.ylabel('Height')
plt.show()
# It only gives information about the # spread of the values in the individual quartiles. Every quartile has 25% of the
# values but some have a very small spread whereas others have quite a large
# one.
          