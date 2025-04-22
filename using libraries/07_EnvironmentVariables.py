
	'''
	PYTHONHOME

    Change the location of the standard Python libraries. By default, the libraries are searched in prefix/lib/pythonversion and exec_prefix/lib/pythonversion, where prefix and exec_prefix are installation-dependent directories, both defaulting to /usr/local.
    import sys
	sys.executable
	'c:\\Python26\\python.exe'
	sys.exec_prefix
	'c:\\Python26'

	How to import a function or a package,relative import v/s absolute import

	Step1: When a module is imported then interpreter first searches it in sys.modules , 
	which is the cache of all modules which have been previously imported.

	Step2: If it is not found then it searches in all built-in modules with that name,
	if it is found then interpreter runs all of the code and makes available to file.

	Step3: If the module is not found then it searches for a file with the same name in the list of directories given by the variable sys.path

	You can import both packages and modules. (Note that importing a package essentially imports the package’s __init__.py file as a module)
	A module is a single file (or files) that are imported under one import
	A package is a collection of modules in directories that give a package hierarchy
	
	sys.path
	A list of strings that specifies the search path for modules. Initialized from the environment variable PYTHONPATH, plus an installation-dependent default.

	sys.path.append(PARENT_DIR)
	
	Python Path
	Augment the default search path for module files. 
	The format is the same as the shell’s PATH: one or more directory pathnames separated by os.pathsep (e.g. colons on Unix or semicolons on Windows).
	Non-existent directories are silently ignored.

	refer : https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time

	refer : https://stackoverflow.com/questions/35166821/valueerror-attempted-relative-import-beyond-top-level-package

	Very Important: Relative imports must be in the form from...import, and the location you’re importing from must start with a dot.

	You can inspect Python’s import path by printing sys.path. Broadly speaking, this list will contain three different kinds of locations:

    1. The directory of the current script (or the current directory if there’s no script, such as when Python is running interactively)
    2. The contents of the PYTHONPATH environment variable
    3. Other, installation-dependent directories

    A minor difference between scripts and modules is that
    when you import a module the system will attempt to use an existing .pyc file
    (provided it exists and is up to date and for that version of Python) 
    and if it has to compile from a .py file it will attempt to save a .pyc file. 
    When you run a .py file as script it does not attempt to load a previously compiled
    module, nor will it attempt to save the compiled code

	'''

	# set PYTHONPATH=C:\Shared\PythonCode\Giddu
	# echo %PYTHONPATH%

	