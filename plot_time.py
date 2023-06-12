import re
import matplotlib.pyplot as plt


path = "log.txt"

with open(path, "r") as file:
    lines = file.readlines()  
diffs = []
for line in lines:
    if line.startswith("TimeModule in"):
        diffs.append(float(line.split(" ")[3]))
diffs.pop(0) #this is diff between init and update of the first ever time, ignore this
print(len(diffs))
# Plot the differences
plt.plot(diffs, '-')
plt.xlabel('Index')
plt.ylabel('Time Difference in ms')
plt.title('Time Differences between consecutive calls of ExeTime')
plt.show()