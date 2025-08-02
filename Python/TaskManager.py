tasks = [{"task":"Quran", "completed":True},
        {"task":"Salah", "completed":True}, 
        {"task":"Study", "completed":False}, 
        {"task":"Exercise", "completed":True}, 
        {"task":"Sleep", "completed":False}, 
        {"task":"Visit Hamada", "completed":True}]

def main ():
    massage = """1- add task to list 
2- mark task as complete 
3- view tasks 
4-quite"""
   
    while True :
        print(massage)
        choice = input("Enter your Choice:")

        if choice == "1":
            # 1- add task to list 
            add_tasks()

        elif choice == "2":
            # 2- mark task as complete 
            mark_tasks()
        
        elif  choice == "3":
            # 3- view tasks 
            view_tasks(tasks)
        
        elif choice == "4":
            # 4-quite"
            break 
        
        else :print(input("Invalid Choice. Please Chose again: "))  

# 1- add task to list 
def add_tasks():
  #get  add task
  task = input("Enter your task: ")
  #define task 
  task_info = {"task": task, "completed": False}
  #add task to list
  tasks.append(task_info)
  print("Task added Successfully !!")
  print(tasks)
  

def mark_tasks():
    #get list of incomplete tasks
    incomplete_tasks = [task for task in tasks if task["completed"] == False]
    
    if not incomplete_tasks:
        print("no tasks to mark.")
        print("_"*30)
        return
    #show them to user 
    for i, task in enumerate(incomplete_tasks):
        print(f"{i+1} - {task['task']}")
        print("_"*30)
    
    #get task from user
    try :
        task_number = int(input("chose the task number to complete: "))
        if task_number < 1  > len(incomplete_tasks):
            print("Invalid task number, pleas chose a valid  task number.") 
        #mark task as complete
        incomplete_tasks[task_number -1]["completed"] = True

        #print conformation message
        print ("task marked as completed")
    except ValueError:
        print("Invalid Input, pleas enter a number.")



def view_tasks(self):
    #if there no tasks print message and return
    if not self:
        print("No Tasks to view.")
        print("_"*30)
        return
    for i,task in enumerate(self):
        # if task["completed"]:
        #     status = "✔"
        # else:
        #     status = "❌"
        status = "✔" if task["completed"] else "❌"
        print(f'{i+1} - {task["task"]} {status}')


if __name__ =="__main__":
    main()
