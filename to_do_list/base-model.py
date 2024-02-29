#!/usr/bin/python3
"""a to-do-list application"""

import sys
import datetime
import time

class Todolist:
    
    """initializing"""
    def __init__(self):
        self.task = []

    def add(self, task):
        """adds a task """
        self.task.append({"task": task , "completed": False})
        
    def remove(self, task):
        """deletes a task"""
        if not self.task:
            print("no tasks to be deleted")
        else:
            for i in self.task:
                if i["task"]== task:
                    self.task.remove(i)
                    break
    
    def listing(self):
        for i , t in enumerate(self.task, start=1):
            status = "completed" if t["completed"] else "pending"
            print(f"index {i} = {t['task']} : {status}")
            
    def completed(self, task):
        for i in self.task:
            if i["task"] == task:
                i["completed"] = True
                break
        print(f"{task} completed")
            
    def report(self):
        complete = 0
        pending =0
        for t in self.task:
            if t["completed"] == True:
                complete += 1
            else:
                pending += 1
        print(f"Total completed tasks: {complete}")
        print(f"Total pending tasks: {pending}")
    def main(self):
    
        while True:
            
            print("\n MAIN-MENUE\n1. Add a new task \n2. delete task \n3. list task \n4. completed \n5. report \n6. exit")
            chose = input("enter your choice (1 - 5): ")
            if chose == '1':
                task = input("enter task to be added: ")
                print(f"\naddding {task}....")
                self.add(task)
            elif chose == '2':
                task = input("enter task to delete: ")
                self.remove(task)
            elif chose == '3':
                self.listing()
        
            elif chose == '4':
                task = input("enter name of task to be marked as completed: ")
                time.sleep(3)
                self.completed(task)
                
            elif chose == '5':
                self.report()
            
            else:
                print("you entered an invalid choice, choose btw (1-5)")
            time.sleep(2)    
            main_menu = input("go back to main menu (yes / no)? ")
            if main_menu == "no":
                break
        
if __name__ == "__main__":
     my_list = Todolist()
     my_list.main()
