# A simple program that packages Py2D-based projects with Py2D in a zip file.
# All hidden folders and directories are ignored.

# python Py2DPackager.py [input file] --include-py2d-source --include-project-source --compile-project-source --include-exts=[...] --main=[module] --output=[out.zip]

def help():
    print "Py2DPackager"
    print "   [input] {options}"
    print "   --output={fileName}"
    print "   --include-py2d-source"
    print "   --include-project-source"
    print "   --include-exts=[...]"
    print "   --main={moduleName}"
    print "   --compile-project-source"
    print ""
    print "   Use the -h flag to display this message and then exit."
    # print "   --compile-project-source"

import sys,zipfile,os,compiler

LOAD_SCRIPT = """
if __name__ == "__main__":
    import sys
    sys.path.append('./Py2D')
    sys.path.append('%s')
    import %s

"""

if __name__ == "__main__":
    if "-h" in sys.argv:
        help()
        exit(0)

    # Get the input project.
    if len(sys.argv) < 2:
        print "Py2DPackager error: No input project specified."
        sys.exit()
    else:
        input_project = sys.argv[1]

    include_exts=[]
    mainmodule=input_project
    output_path = input_project+".zip"
    for arg in sys.argv:
        if arg.startswith("--include-exts="):
            include_exts = arg.split("=")[1][1:-1].split(",")
        elif arg.startswith("--main="):
            mainmodule = arg.split("=")[1]
        elif arg.startswith("--output="):
            output_path = arg.split("=")[1]

    COMPILE_PROJECT_SOURCE = "--compile-project-source" in sys.argv
    INCLUDE_PROJECT_SOURCE = "--include-project-source" in sys.argv
    INCLUDE_PY2D_SOURCE = "--include-py2d-source" in sys.argv

    # Does the Input project exist.
    if not os.path.exists(input_project):
        print "Py2DPackager error: Project %s does not exist."%input_project
        exit()

    # Get Py2D installation location
    py2d_inst_dir_path = os.path.join(os.path.expanduser("~"),".py2d_inst_dir")
    if os.path.exists(py2d_inst_dir_path):
        py2dpath=open(py2d_inst_dir_path,'r').read()
    else:
        print "Py2DPackager error: Unable to find Py2D installation location."
        print "\t~/.py2d_inst_dir_path is missing."
        sys.exit()

    print "Ready to build " + output_path
    zfile = zipfile.ZipFile(output_path,'w')

    # Package execute script
    zfile.writestr('run.py',LOAD_SCRIPT%("./%s"%input_project,"%s.%s"%(input_project,mainmodule)))

    # Package Project
    print "Packaging %s"%input_project
    for dirpath,dirnames,filenames in os.walk(input_project):
        filenames = [f for f in filenames if not f[0] == '.']
        dirnames[:] = [d for d in dirnames if not d[0] == '.']
        cpath = os.path.join(os.path.relpath(input_project),os.path.relpath(dirpath))
        for f in filenames:
            path = os.path.relpath(os.path.join(dirpath,f))
            # Package if include source or compile source, and is source file
            #   or if is pyc file and not compile source
            #   or if the extension is in include_exts
            if ((INCLUDE_PROJECT_SOURCE or COMPILE_PROJECT_SOURCE) and f.endswith(".py")) or (f.endswith(".pyc") and not COMPILE_PROJECT_SOURCE) or (f.split(".")[len(f.split("."))-1] in include_exts):
                print "    %s"%os.path.join(dirpath,f),
                bytes = open(path,'r').read()
                
                # Write Source file if it exists
                if INCLUDE_PROJECT_SOURCE and path.endswith('.py'):
                    zfile.writestr(path,bytes)

                # Write Compiled source
                if COMPILE_PROJECT_SOURCE and path.endswith('.py'):
                    print " & " + path + 'c',
                    compiler.compileFile(path)
                    bytes = open(path+'c','r').read() # Open the generated pyc file
                    path += 'c'
                zfile.writestr(path,bytes)
                print "\n",

    # Package Py2D
    print "Packaging Py2D"
    for dirpath,dirnames,filenames in os.walk(py2dpath):
        filenames = [f for f in filenames if not f[0] == '.']
        dirnames[:] = [d for d in dirnames if not d[0] == '.']

        cpath = os.path.join(os.path.relpath(input_project),os.path.relpath(dirpath))
        for f in filenames:
            # Only package Py2D binary files unless --include-py2d-source is specified.
            if (INCLUDE_PY2D_SOURCE and f.endswith(".py")) or f.endswith(".pyc"):
                print "    %s"%os.path.join(dirpath,f)
                zfile.write(os.path.relpath(os.path.join(dirpath,f)))

    print "Packaged Py2D with %s in %s"%(input_project,output_path)
    print "Have a nice day."
