def openfiles():
    import csv
    file=open("salaries.txt", "r")

    firstname= [""]*50
    surname= [""]*50
    salary = [0]*50
    index= 0
    
    for row in csv.reader(file):
        firstname[index]=row[0]
        surname[index]=row[1]
        salary[index]=(int)(row[2])
        index=index +1
    return firstname, surname, salary, index

def averageS(salary):
    average=0
    for loop in range(0,50):
        average= average + salary[loop]
    averageS= average / 50
    print("the average salary is :", averageS)
    return averageS

def high_salaries(averageS):
    count=0
    for loop in range(0,50):
        if salary[loop]> averageS:
            count=count+1
    print("\nsalaries the number of people who earn more than the average salary is", count)

def highestS(firstname, surname, salary):
    highest=salary[0]
    for loop in range(0,50):
        if salary[loop] > highest:
            highest = salary[loop]
            count = loop
    print("\n", firstname[count], surname[count],"have got the highest salary with £", highest)

def lowestS(firstname, surname, salary):
    lowest=salary[0]
    for loop in range(0,50):
        if salary[loop] < lowest:
            lowest=salary[loop]
            count = loop
    print("\n", firstname[count], surname[count], "have got the lowest salary with £", lowest)

def find_person(firstname, surname, salary):
    print("enter the first name of a person to check their salary")
    name1=input()
    print("enter", name1,"'s surname to be more percise")
    name2=input()
    presence="n"
    found= False
    count=0
    while found == False and count < 50:
        if name1 == firstname[count] and name2 == surname[count]:
            line=count
            print(name1, name2, "earns £", salary[line])
            presence= "y"
            found = True
        else:
            count = count+1
            presence="n"
    if presence == "n":
        print("sorry, name is not found!")

def export(firstname, surname, salary):
    with open("50k.txt","w") as file:
        for loop in range(len(salary)):
            if salary[loop]> 50000:
                file.write(firstname[loop]+",")
                file.write(surname[loop]+",")
                file.write(str(salary[loop])+"\n")

#main program

firstname, surname, salary, index= openfiles()
averageS=averageS(salary)
high_salaries(averageS)
highestS(firstname, surname, salary)
lowestS(firstname, surname, salary)
find_person(firstname, surname, salary)
export(firstname, surname, salary)
