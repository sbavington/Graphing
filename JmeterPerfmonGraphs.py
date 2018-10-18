from matplotlib import pyplot as plt
from matplotlib import style
import datetime

data_noopt = open("./NoOpt.csv", "r")
data_t4 = open("./Opt.csv", "r")
data_crypt = open("./Crypt.csv", "r")

cpu_percent_noopt = []
cpu_percent_t4 = []
cpu_percent_crypt = []
mem_noopt = []
mem_t4 = []
mem_crypt = []

for line in data_noopt.readlines():
    line = line.strip()
    line = line.split(';')
    this_cpu = (float(line[1]))
    print('>>{}'.format(line[2]))
    this_mem = (float(line[2]))
    print(type(this_cpu),this_cpu)
    print(type(this_mem),this_mem)
    cpu_percent_noopt.append(this_cpu)
    mem_noopt.append(this_mem)
for line in data_t4.readlines():
    line = line.strip()
    line = line.split(';')
    this_cpu = (float(line[1]))
    this_mem = (float(line[2]))
    print(type(this_cpu),this_cpu)
    print(type(this_mem),this_mem)
    cpu_percent_t4.append(this_cpu)
    mem_t4.append(this_mem)

for line in data_crypt.readlines():
    line = line.strip()
    line = line.split(';')
    this_cpu = (float(line[1]))
    this_mem = (float(line[2]))
    print(type(this_cpu),this_cpu)
    print(type(this_mem),this_mem)
    cpu_percent_crypt.append(this_cpu)
    mem_crypt.append(this_mem)

print (cpu_percent_noopt)
print (cpu_percent_t4)
print (cpu_percent_crypt)

style.use('ggplot')
ticks = 1017

x = range(1,ticks)
fig, ax1 = plt.subplots(figsize=(20, 7))
color1 = 'tab:red'
color2 = 'tab:blue'
color3 = 'tab:green'
ax1.plot(cpu_percent_noopt,linewidth=1)
ax1.plot(cpu_percent_t4,linewidth=1)
ax1.plot(cpu_percent_crypt,linewidth=1,linestyle='--')
ax1.tick_params(axis='y', labelcolor=color1)

plt.title('JMETER CPU Percent {}'.format(datetime.datetime.now()))
ax1.set_ylabel('CPU%')
ax1.set_xlabel('Ticks')
ax1.legend(['CPU NoOpt','CPU T4','CPU Crypt'],loc=3)
fig.tight_layout()
plt.show()

fig, ax1 = plt.subplots(figsize=(20, 7))
color1 = 'tab:red'
color2 = 'tab:blue'
color3 = 'tab:green'
ax1.plot(mem_noopt,linewidth=1)
ax1.plot(mem_t4,linewidth=1)
ax1.plot(mem_crypt,linewidth=1,linestyle='--')
ax1.tick_params(axis='y', labelcolor=color1)

plt.title('JMETER Mem Percent {}'.format(datetime.datetime.now()))
ax1.set_ylabel('Mem%')
ax1.set_xlabel('Ticks')
ax1.legend(['Mem NoOpt','Mem T4','Mem Crypt'],loc=3)
fig.tight_layout()
plt.show()

