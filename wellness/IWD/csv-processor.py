# data digestion
import csv

teachers = []


def main():
	filterCSV('iwd.csv')
	# makeCSV()


def filterCSV(fileName):
    with open(fileName) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        # ONLY CHANGE THE TEACHERNAMES ARRAY
        teacherNames = ["Dwyer", "Fang", "Firdman", "Flores", "Garber", "Greenwald",
            "Khevelev", "Luczak", "Montserrat", "Siegel", "Stuzin", "Wisotsky", "Wong"]
        # A dictionary of teachers and their students
        teachers = {}
        for teacherName in teacherNames:
            teachers[teacherName] = []
        # print teachers

        # Read CSV, add students to appropriate teachers
        for row in readCSV:
            name = row[1].title()
            for i in range(5, 19):
                if row[i] in teachers:
                   teachers.row[i].append(name)
        print teachers

def makeCSV():
	f = open("teachersForm.csv", "w")
	line = ""
	counter = 0

	for teacher in teachers:
		line = ""
		line += teacherNames[counter] + "\n"
		for period in teacher:
			if len(period) == 1:
				line += ""
			else:
				line += "\n"
				for student in period:
					line += student + ","
		line += "\n"
		f.write(line)
		counter+=1
	f.close()
	print("DONE")

main()
