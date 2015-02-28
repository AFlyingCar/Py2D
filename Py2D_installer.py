import urllib2, sys, os, imp, marshal

WINDOWS_INSTALL_PATH = "C:\\Program Files\\Py2D\\"
MASTER_DOWNLOAD_URL = "https://raw.githubusercontent.com/AFlyingCar/Py2D/master/"
MANIFEST_FILE_URL = MASTER_DOWNLOAD_URL + "MANIFEST"

def getFileList():
	data = urllib2.urlopen(MANIFEST_FILE_URL).read()
	raw_list = data.split("\n")
	flist = []

	for f in raw_list:
		if not f:
			continue
		elif f.startswith("#"):
			continue
		else:
			flist.append(f)

	return flist

def getFile(url,install_path):
	try:
		data = urllib2.urlopen(url).read()
		path = os.path.abspath(install_path)

		writeStringToPYC(data,path)
	except urllib2.URLError as e:
		print e
		print "Error downloading file: %s\n" % url.split(MASTER_DOWNLOAD_URL)[1] 
		return

#
# Write a string as executable Python code to path
# Code mostly copied from Python's compile module
#
def writeStringToPYC(data,path):
	code_obj = compile(data,'','exec')

	fc = open(path,'wb')
	fc.write("\0\0\0\0")

	timestamp = long(os.stat(path).st_mtime)

	fc.write(chr( timestamp        & 0xff))
	fc.write(chr((timestamp >> 8)  & 0xff))
	fc.write(chr((timestamp >> 16) & 0xff))
	fc.write(chr((timestamp >> 24) & 0xff))

	marshal.dump(code_obj,fc)

	fc.flush()
	fc.seek(0,0)

	fc.write(imp.get_magic())
	fc.close()

def PrepareManifestVal(man_value):
	url = MASTER_DOWNLOAD_URL + man_value[1:]

	directory = man_value[2:]
	directory = directory.split("/")

	if len(directory) > 1:
		directory = directory[:len(directory)-1]
		directory = os.path.join(*directory)
	else:
		directory = ""

	path = WINDOWS_INSTALL_PATH + directory

	filepath = WINDOWS_INSTALL_PATH + man_value[2:]

	return (url,path,filepath)

def main():
	flist = getFileList()

	if not os.path.exists(WINDOWS_INSTALL_PATH):
		print "Creating %s.\n"%WINDOWS_INSTALL_PATH 
		os.makedirs(WINDOWS_INSTALL_PATH)

	for f in flist:
		url,path,filepath = PrepareManifestVal(f)

		if not os.path.exists(path):
			os.mkdir(path)
		
		print "Downloading %s...\n"%f[2:]

		getFile(url,filepath + "c")

if __name__ == "__main__":
	main()