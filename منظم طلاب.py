
def add():
    print('add the student name and his grade : ')
    ans='yes'
    while ans=='yes':
        name=str(input('the name is : '))
        grade=int(input('the grade is : '))
        Student_Manager[name]=grade
        ans=str(input('you want to add more: '))
    return Student_Manager

def show():
    if not Student_Manager:
         print('no data found')
    else:
        for key, value in Student_Manager.items():
            print(key,value)
def search():
    n1=str(input('enter the student name: '))
    if n1 in Student_Manager:
        x=Student_Manager.get(n1)
        print(n1,':',Student_Manager[n1])
    else:
        print('not found')
def delete():   
    n=str(input('Enter student name: '))
    if n in Student_Manager:
          del Student_Manager[n]
          print('Student deleted successfully.')
    else:
        print('Student not found.')
    
    
ans=1
Student_Manager={}
while ans!=0:
    num=int(input('Student Manager 1- Add Student2- Show Students3- Search Student4- Delete Student0- Exi'))
    if num==1:
        print(add())
    elif num==2:
        show()
    elif num==3:
        search()
    elif num==4:
        delete()
            