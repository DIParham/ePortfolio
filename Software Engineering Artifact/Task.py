# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 13:33:02 2022

@author: danielle parham
Class: CS 499
Category: Software Design and Engineering
title: Task 

"""
#task_func class
#designed to limit task variables: taskID, taskName, and taskDes
#to prevent invalid input: char limit or None values
class task_func:
    def task_details(self, taskID, taskName, taskDes):
        
        #verify taskID is valid
        if taskID == None or len(taskID) > 10:
            #calls error message statement
            self.errMessage()
        
        #verify taskName is valid
        if taskName == None or len(taskName) >20:
            self.errMessage()
        
        #verify task Description is valid
        if taskDes == None or len(taskDes)>50:
            self.errMessage()
            
        #default else statement
        else:
        
            print("Confirmed: Task Added")
            self._taskID = taskID
            self._taskName = taskName
            self._taskDes = taskDes
            
    # setters and getters
    
    def getTaskID(self):
       
       return self._taskID
        
    def setTaskID(self, taskID):
        self._taskID = taskID
    
    def getTaskName(self):
        return self._taskName
    
    def setTaskName(self, taskName):
        self._taskName = taskName
    
    def getTaskDes(self):
        return self._taskDes
    
    def setTaskDes(self, taskDes):
        self._taskDes = taskDes
    
    #error message to be printed if conditions are met
    def errMessage(self):
        raise Exception("Invalid Input")            
        

