import sys, os

# 1. We check args
# 2. We make the vivado tcl script
# 3. We execute it

def Usage(): # print the correct usage of this script
	print ("Use: python pyPackage.py [-opts] [cmd [args]]")

	

	print(" ")
	print("Options:")
	print(" ")
	
	print("\t-help   Display the options and the usage of this script.")
	print("\t-top    Path of the VHDL top.")
	print("\t-out    Path of the IP output.")
	print("\t-tcl    Export a Vivado tcl script.")

#print ('Number of arguments: ' + str(len(sys.argv)) + ' arguments.')
#print ('Argument List : ' + str(sys.argv))

if len(sys.argv) <= 1: 	# Incorrect usage of the script
	Usage()
	sys.exit(0)
else:

	sys.argv.pop(0)		# Remove the name of the script
	nextArg = 0
	topPath = ""
	ipPath = ""
	tclMode = 0

	for arg in sys.argv:
		if nextArg != 0:
			if nextArg == 1:
				topPath = arg		# We save the top vhdl path
			elif nextArg == 2:
				ipPath = arg		# We save the output path
			else:
				Usage()
				sys.exit(0)
				
			nextArg = 0
		else:
			if arg ==  "-help":
				Usage()
				sys.exit(0)
			elif arg == "-top":
				nextArg = 1				# The next arg is the path of the top vhd
			elif arg == "-out":
				nextArg = 2				# The next arg is a path where the IP will be saved
			elif arg == "-tcl":
				tclMode = 1
			else:
				print ("Unknown option " + arg)
				Usage()
				sys.exit(0)
				
	if os.path.exists(topPath) == False:
		print ("Incorrect top vhdl file. Bye")
		sys.exit(0)
	
	if os.path.isdir(ipPath) == False:
		print ("Output ip path file set to ./")
		ipPath = "./"
	
	# todo :
	# Open the top vhdl file
	# read ports
	# close the file
	
	# try to detect interfaces
	# make the tcl script
	# optionnal : save this script
	# Execute this script
	
	