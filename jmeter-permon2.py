from matplotlib import pyplot as plt
from matplotlib import style
import datetime

data= open("./082002.csv", "r")

cpu_list = []
network_list = []

for line in data.readlines():
    line = line.strip()
    line = line.split(',')
    if 'timeStamp' in line[0]: continue
    if 'CPU' in line[2]:
        cpu_value = int(line[1])
        cpu_list.append(cpu_value/1000)
    if 'Network' in line[2]:
        network_value = int(line[1])
        network_list.append(network_value)

print('CPU {}'.format(cpu_list))
print ('Network {}'.format(network_list))

style.use('ggplot')
fig, ax1 = plt.subplots(figsize=(20, 7))

ax1.plot(cpu_list,linewidth=1,color='tab:red')
ax1.tick_params(axis='y', labelcolor='tab:red')
plt.title('JMETER CPU % and MB/s{}'.format(datetime.datetime.now()))
ax1.set_ylabel('CPU%')
ax1.legend(['CPU'],loc=3)
fig.tight_layout()
ax2 = ax1.twinx()
ax2.plot(network_list,linewidth=1,color='tab:blue')
ax2.tick_params(axis='y', labelcolor='tab:blue')
ax2.set_ylabel('Network MB/s')
ax2.legend(['MB/s'],loc=4)
plt.show()