import csv

def main():
    filterCSV("iwd.csv")
    makeCSV()

teachers = {}

def filterCSV(filename):
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter = ",")
        teacherNames = ["Dwyer", "Fang", "Firdman", "Flores", "Garber", "Greenwald",
            "Khevelev", "Luczak", "Montserrat", "Siegel", "Stuzin", "Wisotsky", "Wong"]
        # A dictionary of teachers and their students
        for teacherName in teacherNames:
            teachers[teacherName] = []
        # print teachers

        # Read CSV, add students to appropriate teachers
        for row in readCSV:
            name = row[1].title()
            timestamp = row[0].title() #adds when the people went
            osis = row[2].title()
            for i in range(4, len(row)):
                if row[i] in teachers:
                    if row[i] == "Garber":
                        teacher = row[i]
                        entry = name + " -- " + osis + "; Timestamp: " + timestamp
                        teachers[teacher].append(entry)
                    else:
                        teacher = row[i]
                        entry = name + " -- " + osis
                        teacher = teachers[teacher] #convert teacher into its constituent array
                        if len(teacher) == 0:
                            teacher.append(entry)
                        else:
                            safe = True
                            #remove dupes
                            for i in teacher:
                                if entry == i:
                                    safe = False
                            if safe:
                                teacher.append(entry)

                        #print i

        #print teachers["Garber"]

def makeCSV():
    file = open("students.csv", "w")
    for teacher in teachers:
        line = ""
        line += teacher + ":"
        for student in teachers[teacher]:
            #print teacher, student
            line += " ," + student + "," + "\n"
        line += "\n" + "," "\n"
        file.write(line)
    file.close()

main()
