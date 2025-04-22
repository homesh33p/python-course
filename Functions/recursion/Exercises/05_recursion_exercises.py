# Create a function to sum a list/tuple without using any inbuilt python function like sum()

# Create a function to find the factorial of a number: 5! = 5*4*3*2*1

# Create a function to find the value of pi till 25 decimal points

# take any nested dictionary, create a function that takes a key and returns its value from that dictionary
# if the key does not exist, it returns None

'''take a nested list and flatten it:
	ex: [1,[1.2,1.3,1.4],2,3]
	output: [1,1.2,1.3,1.4,2,3]

	ex: [1,[1.2,[1.21,1.24],1.3,1.4],2,3]
	output: [1,1.2,1.21,1.24,1.3,1.4,2,3]
'''

'''take a nested dictionary and flatten it:
nested = {
			1:{
				1.1:"one.one",
			   	1.2:{
						1.23:"one.twothree",
						1.21:"one.twoone"
					}
			   },
			2:{
				2.6:"two.six",
			   	2.8:"two.eight"
			}
		}

output = {
			1:{
				1.1:"one.one",
			   	1.2:{
						1.23:"one.twothree",
						1.21:"one.twoone"
					}
			   },
			1.1:"one.one",
			1.2:{
					1.23:"one.twothree",
					1.21:"one.twoone"
				},
			1.23:"one.twothree",
			1.21:"one.twoone",
			2:{
				2.6:"two.six",
			   	2.8:"two.eight"
			},
			2.6:"two.six",
			2.8:"two.eight"
		}

'''


'''
import the dictionary from the libgen.py file in the same folder
hint: include this line at top of your file -> from libgen import LibraryGenesys
create a function that takes the department or subdepartment and the book code
return the book name
'''

'''
	if the file handling chapter is completed, attempt the following:
'''

# Take any folder in your system, and print all folder names within the folder
# You must print all folders inside your subfolders as well
# it should not print any files inside, only the folders

# Take a user input folder path, create the path in your system
# ex: "C:\users\folder1\folder2\folder3\folder4
# it must create all the above folders, even if the parent folder doesnot exist




