import matplotlib.pyplot as plt

x = [3,5,1,6,7,2,4,8]
y = [2,1,5,3,4,8,7,6]

plt.scatter(x,y,label='skit',marker='*',s=100)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('GRAPH')
plt.legend()
plt.show()
