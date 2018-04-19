import os
fh = open('a.txt','w+')
os.system('./darknet detect cfg/yolov3.cfg yolov3.weights data/taj-mahal-pose.jpg')
a=fh.read()
b=a.strip().split(' ')
for i in range(len(b)):
	b[i]=int(b[i])
s=sum(b[1:len(b)])
#print 'occulusion percentage:',((1.0*s)/b[0])*100,'%'
t=((1.0*s)/b[0])*100
if t<15.0:
	print 'Image is good. Keep it.'
else:
	print 'Image has occlusions. Discard it.'
fh.close()
os.remove('a.txt')
