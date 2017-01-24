import datetime
import matplotlib.dates as md
from pylab import figure, show
s=[1,2,3,4,5,6,7,8,9,10,11,12]
n=[]
for a in s:
    #y=a[0:4]
    #m=a[-2:]
    #print int(y),int(m)
    #dt=datetime.datetime(int(y),int(m),1)

    n.append(a)

#y=[626592,651427,640711,595366,706369,533270,568666,672728,1005325,1310415,837757,897076] 
y=[10,100,-100,2,3,6,7,8,10,1533,55,33]
z=[1,2,3,4,5,6,7,8,9,10,11,12] 
fig = figure()
ax = fig.add_subplot(111)
ax.plot(n, y, '*-')
ax.plot(n, z, '.-')
#fig.autofmt_xdate()
show()


#http://ithelp.ithome.com.tw/articles/10127225
