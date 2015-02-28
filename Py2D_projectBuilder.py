#########################
# AFlyingCar			#
# 2/19/15				#
# Py2D Project Builder 	#
#########################

import shutil,errno,os

PY2D_INSTALLATION_PATH = "C:\\Program Files\\Py2D"
# PY2D_INSTALLATION_PATH = ".\\Py2D" # Use to build with lastet build rather than the recommended one

def copyFiles(source,target):
	try:
		shutil.copytree(source,target)
	except OSError as exc:
		if exc.errno == errno.ENOTDIR:
			shutil.copy(source,target)
		else:
			raise

def buildProject():
	verifyPy2DInstallation()

	path = raw_input("Full path to the project: ")

	bin_path = os.path.join(path,"bin\\Py2D")
	resource_path = os.path.join(path,"resources")
	config_path = os.path.join(path,"Settings")

	if not os.path.exists(resource_path):
		os.makedirs(resource_path)

	if not os.path.exists(config_path):
		os.makedirs(config_path)

	open(bin_path[:4] + "__init__.py",'w').write("")

	try:
		copyFiles(PY2D_INSTALLATION_PATH,bin_path)
	except WindowsError as e:
		print "Files already copied. Skipping."

def verifyPy2DInstallation():
	if not os.path.exists(PY2D_INSTALLATION_PATH):
		print "Unable to find valid copy of Py2D. Please check that it properly installed in %s." % PY2D_INSTALLATION_PATH
		raise OSError("ERROR - Py2D not installed.")

if __name__ == '__main__':
	buildProject()