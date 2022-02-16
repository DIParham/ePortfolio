# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 11:47:51 2022

@author: danielle parham
Class: CS 499
Category: Software Engineering and Design
Title: TaskService_test

"""
import unittest
import TaskService

#Task Service tests
#ensures the task service CRUD functionality
#tests to ensure that invalid input is not used
#tests are designed to fail if an exception is not thrown
#or if invalid input is used.

class taskServiceTest(unittest.TestCase):
    
          
    #tests add task function
    def test_addTask(self):
        ts =  TaskService
        tk = ts.task_Serve()
        taskID = "123"
        taskName = "Python"
        taskDes = "Programming"
        
        ok = tk.addTask(taskID, taskName, taskDes)
        
        #asserts that task is added
        self.assertTrue(ok)
        
        print("Add Task Test ")
    
    def test_invalidTask(self):
    
        ts = TaskService
        tk = ts.task_Serve()
        
        #expects exception to be raised
        #passes if exception raised
        #tests invalid input
        with self.assertRaises(Exception):
        
           taskID = "321"
           taskName = None
           taskDes = "software engineering and design" 
           #adds task and assigns to ok variable
           tk.addTask(taskID, taskName, taskDes)
           
        with self.assertRaises(Exception):
            #when taskID > 10, it should throw an exception
            taskID = "098765432100"
            taskName = "CS 499"
            taskDes = "Software Engineering and Design"
            
            tk.addTask(taskID, taskName, taskDes)
        
        print("Invalid Task Test")
                
        
        
    def test_removeTask(self):
        ts = TaskService
        tk = ts.task_Serve()
        taskID = "123"
        taskName = "Python"
        taskDes = "Programming"
                
        #add test data
        ok = tk.addTask(taskID, taskName, taskDes)
        #assures that test data added successfully
        self.assertTrue(ok)
        #remove test data
        ok = tk.removeTask(taskID)
        #asserts that test data has been removed
        #would fail if ok is true
        self.assertFalse(ok)
        
        print("Remove Task Test")
        
    def test_removeInvalidTaskID(self):
        ts = TaskService
        tk = ts.task_Serve()
        tk.addTask("123", "Python", "Programming")
                 
        taskID = "321"
        
        #asserts that exception is raised when task ID is invalid
        self.assertRaises(Exception, tk.removeTask(taskID))
        self.assertRaises(Exception, tk.removeTask(None))
        
        print("Invalid Remove Task Test ")
     
    def test_updateTask(self):
       ts = TaskService
       tk = ts.task_Serve()
       taskID = "123"
       
       #add test data
       tk.addTask(taskID, "Python", "Programming")
       
       #update taskName and assign to ok variable
       ok = tk.updateTask(taskID, "Java", "Programming")
       
       #asserts that ok is true
       self.assertTrue(ok)
       
       print("Update Task Test")
       
       
    def test_invalidUpdateTask(self):
       ts = TaskService
       tk = ts.task_Serve()
       taskID = "321"
       taskName = "Python"
       taskDes = "Programming"
       tk.addTask(taskID, taskName, taskDes)
       
       #tests against None input
       taskName = None
       self.assertRaises(Exception, tk.updateTask(taskID, taskName, taskDes))
       
       #tests against char limit
       taskName = "0012345678900987654321"
       self.assertRaises(Exception, tk.updateTask(taskID, taskName, taskDes))
       
       print("Invalid Update Task Test")
    
      
    def test_displayTask(self):
        ts = TaskService
        tk = ts.task_Serve()
        taskID = "123"
        taskName = "Python"
        taskDes = "Programming"
        
        tk.addTask(taskID, taskName, taskDes)
        
        #assigns to ok variable 
        ok = tk.displayTask(taskID)
        #asserts that ok is true
        #if true then display function passes 
        self.assertTrue(ok)
        
        print("Display Task Test ")
     
        #Failed
    def test_InvalidDisplayTask(self):
        ts = TaskService
        tk = ts.task_Serve()
        taskID = "123"
        taskName = "0123456789012345678900"
        taskDes = "Programming"
        
        #asserts exception is thrown if invalid input used
        self.assertRaises(Exception, tk.updateTask(taskID, taskName, taskDes))
        
        taskDes = None
        self.assertRaises(Exception, tk.updateTask(taskID, taskName, taskDes))
        
        print("Invalid Display Task Test ")
            
        
if __name__ == '__main__':
    unittest.main()
    
    print("All Testing Complete..")

        
