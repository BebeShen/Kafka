import matplotlib.pyplot as plt
import numpy as np

batchs = ['none','gzip','snappy']
latency = [6120.86, 6200.65, 6904.61]
x = np.arange(len(batchs))
plt.bar(x, latency, color=['red','green','blue'])
plt.ylim([5500, 7500])
plt.xticks(x, batchs)
plt.xlabel('compression.type')
plt.ylabel('Average Latency (ms)')
plt.savefig('./images/compression.png')
plt.show()