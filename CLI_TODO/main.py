# author - SARWAT RAZZAQUE CHOUDHURY
from datetime import datetime
import prettytable
# creating a global list for username , password, date and time of account creation
UserList = list()
UserPassList = list()
UserAccountCreatedDate = list()
UserAccountCreatedTime = list()
# static malloc() for 1000 users
TodoList = [[] for i in range(1000)]
TodoDate = [[] for i in range (500)]

class Register:
    def __init__(self,name,password):
        self.name = name
        self.password = password
        currentDate = datetime.now()
        self.AccountCreatedDate = currentDate.strftime("%Y-%m-%d")
        self.AccountCreatedTime = currentDate.strftime("%H:%M:%S")
        
        
    def AuthenticateRegistration(self):
        
        for i in range(len(UserList)):
            if self.name == UserList[i]:
                print("Username already exists!")
                return False
                
                
        else:
            print("Account created")
            UserList.append(self.name)
            UserPassList.append(self.password)
            UserAccountCreatedDate.append(self.AccountCreatedDate)
            UserAccountCreatedTime.append(self.AccountCreatedTime)
            
            return True
            
            
            #print(UserList, UserPassList,UserAccountCreatedDate,UserAccountCreatedTime)
            

class Login(Register):
    def __init__(self,name,password):
        self.name = name
        self.password = password
        
    def AuthenticateLogin(self):
        
        FoundUser = self.name in UserList
        if FoundUser:
            UserIndex = UserList.index(self.name)
            if self.password == UserPassList[UserIndex]:
                #print(f"{self.name}  Logged in....")
                return True
            else:
                print("password doesn't match..")
                return False
            
        if FoundUser == False:
            print("Username doesn't match")
            return False
        
    def LoggedUser(self):
        return self.name
        
class Todo:
    
    def addTodo(self,task,name):
        self.task = task
        self.name = name
        TimeAdded = datetime.now()
        self.TimeAdded = TimeAdded.strftime("Time: %H:%M:%S Date: %Y-%m-%d")
        
        index = UserList.index(self.name)
        TodoList[index].append(self.task)
        TodoDate[index].append(self.TimeAdded)
    def DeleteTodo(self,task,name):
        try:
            self.task = task
            self.name = name
            findIndex = UserList.index(self.name)
            TodoList[findIndex].remove(self.task)
            return True
        except:
            return False
        
    def UpdateTodo(self,name,task,new):
        try:
            self.task = task
            self.name = name
            self.new = new
            index = UserList.index(self.name)
            updateIndex = TodoList[index].index(self.task)
            TodoList[index][updateIndex] = self.new
            TodoDate[index][updateIndex] = self.TimeAdded
            return True
        except:
            return False
            

    def ShowTodoList(self,name):
        self.name = name
        index = UserList.index(self.name)
            
        data = prettytable.PrettyTable()
        data.add_column('Task',TodoList[index])
        data.add_column('DATETIME',TodoDate[index])
        return data
    
    
print("TODO")
print("Select required entry")
print("1 -> REGISTRATION\n 2-> LOGIN\n 3-> TODOLIST\n 4-> ADD NEW TODO\n 5-> DELETE TODO\n 6-> UPDATE TODO\n 7-> LOGOUT")

while True:
    
    selectedNumber = int(input())
    if selectedNumber == 1:
        name = input("Enter name: ")
        password = input("Enter password: ")
        newUser = Register(name,password)
        if newUser.AuthenticateRegistration():
            print(f"REGISTRATION SUCCESSFUL \n USERNAME: {name} PASSWORD: {password}")
    if selectedNumber == 2:
        name = input("Enter username: ")
        password = input("Enter password: ")
        newLogin = Login(name,password)
        if newLogin.AuthenticateLogin():
            time = datetime.now()
            loginTime = time.strftime("%H:%M:%S")
            print(f"{name} logged in.... at {loginTime}")
            # if Login is true then starting a new while loop
            while True:
                selectedNumber = int(input())
                if selectedNumber == 3:
                    newShowTodo = Todo()
                    print(newShowTodo.ShowTodoList(name)) 
                if selectedNumber == 4:
                    newTask = input("Enter the task to be added: ")
                    addTodo = Todo()
                    addTodo.addTodo(str(newTask),name)
                    print("Task added..")
                if selectedNumber == 5:
                    newTask = input("Enter the task to be deleted: ")
                    deleteTodo = Todo()
                    if deleteTodo.DeleteTodo(newTask,name):
                        print(f"{newTask} deleted succesfully")
                    else:
                        print(f"Couldn't delete {newTask}")
                if selectedNumber == 6:
                    oldTask = input("Enter the task to be updated: ")
                    newTask = input("Enter the new task to be assigned: ")
                    updateTodo = Todo()
                    if updateTodo.UpdateTodo(name,oldTask,newTask):
                        print(f"{newTask} updated successfully")
                    else:
                        print("Couldn't update the task")
                # logout of the login screen
                if selectedNumber == 7:
                    time = datetime.now()
                    logoutTime = time.strftime("%H-%M-%S")
                    print(f"{name} logged out.... at {logoutTime}")
                    break
