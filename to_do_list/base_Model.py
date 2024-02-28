#!/usr/bin/python3
"""the base_model class that defines a to_do_list"""
import datetime

class BaseModel:

    def __init__(self):
        """initializatin process"""
        self.my_dict = {}

    def add(self):
        """defines adding a task to the to-do-list"""
        new_task = input("enter new task").isalnum()
        with open("list.txt", "a") as file:
            file.write(task + "\n")
        print(f"you added {task}")

    def load(self):
        """defines loading the contents of a file into a dictionary"""
        try:
           with open("list.txt","r") as file:
               for i,  line in enumerate(file, start=1):
                   self.my_dict[i] = line.strip('\n')
        except FileNotFoundError:
            self.my_dict = {}
