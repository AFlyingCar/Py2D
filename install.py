import urllib2,os,sys

HOME = os.path.expanduser("~")

def installDependency(dep):
	response = urllib2.urlopen(dep)
	f=response.read()
	dlpath = os.path.join(HOME,"AppData","Local","Temp",dep.split("/")[len(dep.split("/"))])
	open(dlpath,'w').write(f)
	os.system(dlpath)

def installFile(path,fname,url):
	response = urllib2.urlopen(url+'/'+fname)
	f = response.read()
	open(path+'/'+fname,'w').write(f)

if len(sys.argv) > 1:
	instdir = sys.argv[1]
else:
	instdir = os.path.join(HOME,".Py2D")

print "Installing pygame."
installDependency("http://pygame.org/ftp/pygame-1.9.1.win32-py2.7.msi")

print "Installing Py2D."
filelist = urllib2.urlopen("http://raw.githubusercontent.com/AFlyingCar/Py2D/master/MANIFEST").read()
for line in filelist.split("\n"):
	installFile(instdir,line,"http://raw.githubusercontent.com/AFlyingCar/Py2D/master/Py2D/")

open(os.path.join(HOME,".py2d_inst_dir"),'w').write(instdir)
