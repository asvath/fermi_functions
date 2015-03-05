import pyfits
import os
import cfg
import subprocess

i=9
for i in range(9,314,4):
	week1=i
	week2=i+3
	#print(['%s' %(cfg.pythoncommand),'stest3.py','%d' %week1,'%d' %week2])
	subprocess.call(['%s' %(cfg.pythoncommand),'stest3.py','%d' %week1,'%d' %week2])







