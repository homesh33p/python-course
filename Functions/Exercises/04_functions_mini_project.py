'''
Note: Make sure that your functions are modular and epress every individual functionality
of the application
Keep a comment at the beginning of every function explaining its functionality
ALso amke sure your every function is modular and doesnot become very lengthy
(preferably but not mandatory) not more than 15 lines each.
Make sure that you ahndle exceptional user input like an unknown book
'''


'''
Below is my library:
'''
LibraryGenesys={
	"Science":{
		"technology":{
			"electrical":{
				1:"Basic Electronics",
				2:"Machines",
				3:"Transmission",
				4:"Digital Electronics",
				5:"Power Electronics",
				6:"High Voltage"
			},
			"civil":{
				1:"Bridges",
				2:"Dams",
				3:"Roads",
				4:"Tunnels",
				5:"Sky Scrapers",
				6:"Reservoirs"
			},
			"compsci":{
				1:"Data Structures",
				2:"Algorithms",
				3:"Compiler Design",
				4:"Network Security",
				5:"Protocols",
				6:"Microprocessor"
			}
		},
		"medicine":{
			"cardiovascular":{
				1:"ECG",
				2:"Blood Sugar",
				3:"Effects of exercise",
				4:"Food Habits",
				5:"Nicotine Addiction",
				6:"Heart"
			},
			"orthopedic":{
				1:"Hands",
				2:"Legs",
				3:"Skull",
				4:"Spine",
				5:"Hips",
				6:"Old People"
			}
		}
	},
	"Business":{
		"MBA":{
				1:"Accounting",
				2:"Presentation",
				3:"Networking",
				4:"Strategy",
				5:"Finance Technology",
				6:"Business Plans"
		},
		"Statistics":{
				1:"Data Science",
				2:"Image Processing",
				3:"Graph Theory",
				4:"Fuzzy Logic",
				5:"Machine Learning",
				6:"Business Analytics"
		}
	}
}

'''
Below is my register
'''

LibraryRegister={
	"technology":{
		"electrical":{
			1:"",
			2:"",
			3:{
				"Issued on":"06-oct-2020",
				"Submission Date":"15-oct-2020",
				"Checked Out By":3
			},
			4:"",
			5:"",
			6:""
		},
		"civil":{
			1:"",
			2:"",
			3:"",
			4:"",
			5:{
				"Issued on":"06-sept-2020",
				"Submission Date":"20-oct-2020",
				"Checked Out By":6
			},
			6:""
		},
		"compsci":{
			1:{
				"Issued on":"08-oct-2020",
				"Submission Date":"25-oct-2020",
				"Checked Out By":1
			},
			2:"",
			3:"",
			4:"",
			5:"",
			6:""
		}
	},
	"medicine":{
		"cardiovascular":{
			1:"",
			2:"",
			3:"",
			4:"",
			5:{
				"Issued on":"20-oct-2020",
				"Submission Date":"25-oct-2020",
				"Checked Out By":3
			},
			6:""
		},
		"orthopedic":{
			1:"",
			2:"",
			3:"",
			4:"",
			5:"",
			6:""
		}
	},
	"Business":{
		"MBA":{
				1:"",
				2:{
					"Issued on":"06-oct-2020",
					"Submission Date":"16-oct-2020",
					"Checked Out By":2
					},
				3:"",
				4:{
					"Issued on":"08-oct-2020",
					"Submission Date":"15-oct-2020",
					"Checked Out By":7
					},
				5:"",
				6:""
		},
		"Statistics":{
				1:"",
				2:"",
				3:"",
				4:"",
				5:"",
				6:{
					"Issued on":"01-oct-2020",
					"Submission Date":"21-oct-2020",
					"Checked Out By":4
					}
		}
	}
}

students=["Swapnil","Prakash","Kaushal","Monu","Himshikhar","Neha","Navneet"]

'''
1. 

You are the librarian.
A student comes to you. Gives their name.
Asks them if they want to issue a book o submit a book.

if they want to issue a book, ask them:
	department: not mandatory if subdepartment available
	subdepartment: not mandatory if department avaialable
	book name: mandatory

if the book is already issued, say sorry and exit

if book is available, ask:
	Submission Date

Issue the book and update the register accordingly and print it. 
The roll number of the student is their position in the list starting from 1 instead of 0

if they want to submit a book, ask them:
	bookname
	department: not mandatory if subdepartment available
	subdepartment: not mandatory if department avaialable

if submitted on time, tell thank you

if not submitted on time, print the fine:
	if number of days above submission date exceeds 1 week: Warning
	if number of days above submission date exceeds 2 weeks: Monetary fine of Rs. 100
	if number of days above submission date exceeds 3 weeks: Temporary ban of 1 month from library
	if number of days above submission date exceeds 4 weeks: Permanent ban

Update the register and print it.
'''


'''
2. 

Write another function, which calls the same function as above, but checks if the student is registered in the college
If yes then the above function is called , if no then print "i am calling the campus security"
'''