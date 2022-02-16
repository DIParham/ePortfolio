# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 13:59:09 2022

@author: danielle parham
Class: CS 499
Category: Software Design and Engineering
Title: TaskService

"""
#Task Module
#create CRUD functions for the tasks program
#it allows user to create, add, update, and delete tasks from a list
#imports task_func to prevent invalid values from being used
from Task import task_func

class task_Serve:
   
    def __init__(self):
        #creates empty list
        
        self.tasklist = []
        
    #add task to tasklist
    def addTask(self, taskID, taskName, taskDes):
        
        #instantiate task_func
        task = task_func()
        
        task.task_details(taskID, taskName, taskDes)
        
        #add task to list
        self.tasklist.append(task)
        return True
    
    #delete task from tasklist
    def removeTask(self, taskID):
        #sorts through task list
        for task in self.tasklist:
            #sets condition that should be met
            
            if task.getTaskID() == taskID:
                #removes task from tasklist
                self.tasklist.remove(task)
                return False
            
           #throws errorMessage() from Task.py if condition is not met
                
        return False
     
    #edit task from tasklist           
    def updateTask(self, taskID, taskName, taskDes):
        
        for task in self.tasklist:   
            #if condition is met, update task variables
            if task.getTaskID() == taskID:
                task.setTaskName(taskName)
                task.setTaskDes(taskDes)
                return True
            #throws errorMessage() from Task.py if condition is not met
                           
        return False
    
    #read task
    def displayTask(self, taskID):
        for task in self.tasklist:
            #if condition is met, print task
            if task.getTaskID() == taskID:
                print(task)
                return True
            #throws errorMessage() from Task.py  if condition is not met
            
        return False
    
    

    