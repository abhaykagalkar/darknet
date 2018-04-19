import os
import shutil
import sys
import argparse

def check_arg(args=None):
    homedir = os.environ['HOME']
    parser = argparse.ArgumentParser(description='Input Parameters to be passed')
    parser.add_argument('-i', '--input',
                        help='Test Input Directory',
                        required='True',
                        default=os.getcwd())
    parser.add_argument('-o', '--out',
                        help='Output of Our Algorithm',
                        default=homedir+"/Documents/RejectedImages")

    results = parser.parse_args(args)
    return (results.input,results.out)

fixed = " ./darknet detector test cfg/coco.data cfg/yolov3.cfg yolov3.weights "
inputDir,outputDir= check_arg(sys.argv[1:])
images = os.listdir(inputDir)
for img in images:
  #os.system("cd darknet")
  fr=open("area.txt","w+")
  command = fixed+os.path.join(inputDir,img)
  os.system(command)
  if(os.stat('area.txt').st_size!=0):
    p=fr.read()
    b=p.strip().split(' ')
    sum1=0
    for i in range(len(b)):
      b[i]=int(b[i])
      if(i!=0):
        sum1=sum1+b[i]
      if(((sum1/(b[0]*1.0))*100)>40):
        print(img,"will be discarded")
        shutil.move(os.path.join(inputDir,img),outputDir)
  os.remove("area.txt")
  #os.system("cd ..")

