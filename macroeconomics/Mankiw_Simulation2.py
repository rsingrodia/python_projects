from matplotlib import pyplot as plt
from Mankiw import Mankiw

s = Mankiw(eps=1.)
paths = s.simulate_path(16)
epsilon = paths[0]
v = paths[1]
y = paths[2]
r = paths[3]
pi = paths[4]
e_pi = paths[5]
i = paths[6]
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
t = ['t-3','t-2','t-1','t','t+1','t+2','t+3','t+4','t+5','t+6','t+7','t+8','t+9','t+10','t+11','t+12']

# Plot Demand Shock
plt.plot(x,epsilon,marker='o',color='grey')
plt.plot(x[3],epsilon[3],marker='o',color='r')
plt.xticks(x,t)
plt.title('(a) Demand Shock')
plt.xlabel('time')
plt.ylabel('\\epsilon_{t}')
plt.ylim([-2, 2])
plt.axhline(y=epsilon[0], color='lightgrey', linestyle='--')
plt.show()

# Plot Output
plt.plot(x,y,marker='o',color='g')
plt.plot(x[3],y[3],marker='o',color='r')
plt.xticks(x,t)
plt.title('(b) Output')
plt.xlabel('time')
plt.ylabel('Yt')
plt.ylim([99, 101])
plt.axhline(y=y[0], color='lightgrey', linestyle='--')
plt.show()

# Plot Real Interest Rate
plt.plot(x,r,marker='o',color='b')
plt.plot(x[3],r[3],marker='o',color='r')
plt.xticks(x,t)
plt.title('(c) Real Interest Rate')
plt.xlabel('time')
plt.ylabel('rt (%)')
plt.ylim([1, 3])
plt.axhline(y=r[0], color='lightgrey', linestyle='--')
plt.show()

# Plot Inflation
plt.plot(x,pi,marker='o',color='orange')
plt.plot(x[3],pi[3],marker='o',color='r')
plt.xticks(x,t)
plt.title('(d) Inflation')
plt.xlabel('time')
plt.ylabel('pi (%)')
plt.ylim([0, 3.5])
plt.axhline(y=pi[0], color='lightgrey', linestyle='--')
plt.show()

# Plot Nominal Interest Rate
plt.plot(x,i,marker='o',color='m')
plt.plot(x[3],i[3],marker='o',color='r')
plt.xticks(x,t)
plt.title('(e) Nominal Interest Rate')
plt.xlabel('time')
plt.ylabel('it (%)')
plt.ylim([2, 6])
plt.axhline(y=i[0], color='lightgrey', linestyle='--')
plt.show()
