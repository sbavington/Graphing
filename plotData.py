from matplotlib import pyplot as plt
from matplotlib import style

data = open("./data", "r")

milliseconds = []
bitrate = []


for line in data.readlines():
    line = line.strip()
    line = line.split(',')
    milliseconds.append (int(line[0]))
    bitrate.append(int(line[1]))

print (milliseconds)
print (bitrate)

plt.plot(milliseconds,bitrate,linewidth=1)
plt.title('Bandwidth KB/s')
plt.ylabel('bitrate')
plt.xlabel('ms')
plt.show()