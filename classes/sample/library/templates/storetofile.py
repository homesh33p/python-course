import pickle

def storefile(filename,obj):
	filehandler = open(filename+".pkl", 'wb')
	pickle.dump(obj, filehandler)

def retrievefile(filename):
	filehandler = open(filename+".pkl", 'rb')
	obj = pickle.load(filehandler)
	return obj


data = {
	"books":{
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
	},
	"register":{
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
	},
	"students":["Swapnil","Prakash","Kaushal","Monu","Himshikhar","Neha","Navneet"],
	"faculty":["Singh","Srivastava","Mishra","Verma","Kumar","Sengupta"]
}

for filename,val in data.items():
	storefile(filename=filename,obj=val)

# for filename in data:
# 	val = retrievefile(filename)
# 	print(val)