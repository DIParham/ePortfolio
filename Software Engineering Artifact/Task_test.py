# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 09:45:05 2022

@author: danie
Class: CS 499 
Category: Software Design and Engineering
Title: Task_Test

"""
import unittest
import Task

#tests for task module
#ensures that the task_func prevents invalid input as expected
#tests would fail if exceptions are not thrown or if invalid input is allowed
class tasktests(unittest.TestCase):
       
    #tests if exception is raised when task ID is None
    def test_TaskIDNone(self):
        
        taskID = None
        if taskID is None:
            self.assertRaises(Exception)
            print("Task ID Null Test passed")
        else:
            print("Valid task ID")
        
            
    #tests if exception is raised when taskID is > 10    
    def test_TaskID(self):
        taskID = "123456789012"
        if len(taskID) > 10:
            self.assertRaises(Exception)
            print("Task ID Character Limit Test passed")
        else:
            print("valid Task ID")
        
    #tests if exception raised when taskName is None
    def test_TaskNameNone(self):
        taskName = None
        if taskName is None:
            self.assertRaises(Exception)
            print("Task Name Null Test passed")
        else:
            print("Valid Task Name")
    
    #tests if exception is raised when taskName is >20
    def test_TaskName(self):
        taskName = "123456789098765432100"
        if len(taskName) > 20:
            self.assertRaises(Exception)
            print("Task Name Character limit Test passed")
        
        else:
            print("valid task Name")
        
    #tests if exception is raised when taskDes is None
    def test_TaskDesNone(self):
        taskDes = None
        if taskDes is None:
            #exception should be raised if task variable is None
            #test passes if exception is raised
            self.assertRaises(Exception)
            print("Task Description Null Test passed")
            
        else:
            print("valid task Description")
            
    #tests if exception is raised when taskDes is > 50
    def test_TaskDes(self):
        taskDes = "1234567890abcdefghijklmnopqrstuvwxyz1234567890000000"
        if len(taskDes)>50:
            #exception should be raised if char limit passed
            #test passes if exception is raised
            self.assertRaises(Exception)
            print("Task Description character limit test passed")
        else:
            print("valid task Description")
     
    #tests if task is added 
    def test_newTask(self):
        
        #instantiates and calls task_func
        newTask = Task.task_func()
        
        #assigns taskID, taskName, and TaskDes test data
        newTask.task_details("123", "CS 499", "Software Engineering and Design")
        
        #asserts true task values, if true test passed
        #if false test failed
        self.assertTrue(newTask.getTaskID() == "123")
        self.assertTrue(newTask.getTaskName() == "CS 499")
        self.assertTrue(newTask.getTaskDes() == "Software Engineering and Design")
  
        
if __name__ == "__main__":

    unittest.main()
    
    #verifies tests have passed
    print("Everything Passed")