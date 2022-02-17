# CS 499 ePortfolio

# Professional Self Assessment

# Enhancement One
Briefly describe the artifact.

For the software engineering category of my ePortfolio, I chose to focus on the Task and TaskService projects from the CS 320: Software Testing, Automation, and Quality Assurance course. Created in February of 2021, these projects aimed to provide create, update, and delete functions for a task program. At the same time, this project incorporated JUnit testing to ensure that the Task and TaskService programs functioned as required by project specifications.   

Justify the inclusion of the artifact in your ePortfolio.

This project was selected due to the utilization of white box testing, specifically JUnit testing. White box testing allows me to demonstrate my ability to anticipate potential software design vulnerabilities and bugs to enhance the overall security of the software. In this project, JUnit testing is used to ensure that the program functions as anticipated when unexpected input like null, is used. Initially, this project was written in the Java programming language. For this enhancement, I wanted to rewrite this project in Python. This would showcase not only my ability to utilize white box testing to ensure program functionality but also my knowledge of Python. However, unlike the initial project, I incorporated a read function which would give the program complete CRUD functionality that was absent in the initial project. Aside from this, I created additional unit tests which tested against invalid input. Originally, the JUnit tests investigated null values and did not have any tests which tested against the character limits. This artifact was further improved through the inclusion of thorough testing which ensured that invalid inputs, null and those exceeding the character limits, would raise exceptions. 

Course Objectives.
 
Reflecting on the code review, I had stated that with this artifact I aimed to achieve two course objectives: “Employ strategies for building collaborative environments that enable diverse audiences to support organizational decision making in the field of computer science” and “Develop a security mindset that anticipates adversarial exploits in software architecture and designs to expose potential vulnerabilities, mitigate design flaws, and ensure privacy and enhanced security of data and resources”. Through this artifact, I believe that I was able to showcase my abilities of meeting these course objectives. Additionally, through this artifact, I was able to reach another course objective: “Demonstrate an ability to use well-founded and innovative techniques, skills, and tools in computing practices for the purpose of implementing computer solutions that deliver value and accomplish industry specific goals”. In the enhancement process of this artifact, I had to utilize the unittest Python module which is a tool used to conduct white-box testing in software development. This ensures that the software meets expectations and project requirements. Simultaneously, the usage of the unittest module showcased my ability to anticipate potential software design vulnerabilities and flaws. The previous version of this project did not include comments that would encourage or influence collaborative environments. In this enhancement, I remedied this issue by incorporating comments which would promote better understanding of the project and further encourage collaboration. 

Reflection

Through this enhancement, I was able to better my understanding of Python, the unittest module, and white-box testing. It was a challenging yet interesting project to tackle. For this enhancement, it required further research and investigation into Python’s testing modules such as unittest and PyTest. In this investigation, I acquired knowledge of the unittest assert methods and how and when to utilize them. It was also relatively helpful to learn how to interpret the test results and in determining flaws in the program. Aside from this, I had to revisit some Python concepts that were quite puzzling to me in the past. However, through this research process, I was able to better my comprehension of them.  
There were a couple of instances which posed an issue in the development of this project. In the Task Service module, there were if statements which compared the getTaskID values to the taskID:

	if task.getTaskID == taskID:
		#Do something
 
This determined that if the task.getTaskID was equivalent to the taskID variable that it would execute the code in the if statements. The functions that utilized this comparison (remove, display, and update) failed the unittests as it was comparing the task.getTaskID function to the taskID value instead of calling the getTaskID function. Further research determined that the function call was incomplete. I was able to resolve this issue by completing the function call:

	if task.getTaskID() == taskID:
		#Do something
 
In doing so, it allowed the Task Service module to pass its unittests. Another issue I encountered were with the unittests themselves. The following code block instructed the program to expect an exception to be thrown:
 
	with self.assertRaises(Exception):
		taskID = None
      		tk.removeTask(taskID)
      
It aimed to test against invalid input. In this instance, it is testing to ensure that an exception is called for the remove function if an invalid input is used. Further research determined that this was an incorrect usage of assert raises. I was able to remedy this issue like this:

	self.assertRaises(Exception, tk.removeTask(taskID))

This ensured that the exception was raised when the remove function is called. Since the taskID was invalid, the program raised the exception. However, in an instance that the taskID was valid, it would fail the test as the exception would not be raised. 

# Enhancement Two
Briefly describe the artifact.

For the Data Structures and Algorithms portion of the ePortfolio, I chose to focus on the Binary Search Tree project from the CS 260: Data Structures and Algorithms course. This project was created in the June of 2020 during the 20EW6 term. The project aimed to demonstrate the usage and functionality of Binary Search Trees using the C++ programming language. It allowed users to filter and sort through a file of bids.

Justify the inclusion of the artifact in your ePortfolio.

I had selected this item because it gives me the opportunity to display my familiarity of the C++ programming language as well as my knowledge of the binary search tree data structure. Initially, this project had limited functionality. Through this artifact, I am able to illustrate my understanding of how I can use the binary tree structure to search, insert, sort, and remove data. Through the refinement process, I aim to improve the efficiency of this artifact. There were methods that were incomplete or did not function as expected. Originally, the method which sorted the bids in order by bid ID was incomplete. At the time of the artifact’s creation, it was not a required function. However, through the enhancement process, I wanted to highlight my ability to use the binary tree structure to sort bids in order by their bid ID. Aside from this, I also aimed to demonstrate my knowledge of other sorting methods such as post and pre order to reorganize the bids. In doing so, it illustrated my understanding of how binary search trees work. For instance, the in order sort prints the left side of the tree, the root, and lastly, the right side. This would allow the program to print the data in order from least to greatest, or alphabetically, as shown by the second binary search tree which was incorporated to sort the bids based on their title. In post order, the left tree is displayed and then followed by the right side and lastly the root. Pre order first visited the root, the left side of the tree and then the right. A second binary search tree was incorporated into this artifact to further improve the efficiency of it. This binary tree utilized the bid title as its key. This enabled the program to order the bids based on title rather than the bid ID. It would allow users to find specific bids much easier. 

Course Objectives.

Reflecting on the code review, I had stated that I wanted to use this artifact to demonstrate the course objective: “Design and evaluate computing solutions that solve a given problem using algorithmic principles and computer science practices and standards appropriate to its solution, while managing the trade-offs involved in design choices.” . Aside from this objective, I was also able to achieve the following course outcome: “Develop a security mindset that anticipates adversarial exploits in software architecture and designs to expose potential vulnerabilities, mitigate design flaws, and ensure privacy and enhanced security of data and resources.” . To showcase the first course objective, I incorporated a second binary search tree to improve the efficiency of the program. This inclusion allowed users to find bids easier as they are given the option of sorting bids either alphabetically, in order based on bid ID, post ordered, or pre ordered. The second course objective that I had mentioned is obtained through the correction of memory deallocation. In the code review, I had noticed the lack of memory deallocation and potential memory leak. With further research, I was able to properly deallocate the memory and showcase a security mindset that is able to anticipate design flaws and potential vulnerabilities in software. 

Reflection.

I had conducted a lot of research for this artifact. I began with revisiting binary tree data structure and its concepts. This helped to enhance my understanding of the data structure and how it is used to navigate data. Initially, my understanding of these data structures was quite limited. Through this artifact, I was able to obtain a better perspective of the binary tree data structure. I did find it quite challenging creating the second binary tree structure and in finishing some incomplete methods. Once I had a better understanding of how to use a binary search tree to sort through the bids, it was quite fun using different transversals to navigate the bids. It was enjoyable to see how the different transversals changed how the bids were sorted and ordered. 
 Aside from the research conducted on the data structure, I also researched and reviewed information regarding memory allocation and deallocation. This was a topic briefly discussed in the CS 405: Secure Coding class. I mentioned in the code review that I had suspected  memory leak errors which could hinder the function of the program. In some aspect, this issue was a bit challenging due to unfamiliarity with memory leak errors. Further research demonstrated that memory leak errors commonly occur when memory is allocated, and we forget to deallocate that memory. With that understanding, I was able to identify a couple of areas of which the memory was not deallocated and therefore produced memory leak errors. In my original code, there were instances of node pointers like left and right, that were never deallocated. With the additional binary search tree, more node pointers were allocated memory. The lack of deallocation would create memory issues as the memory usage would be continuously increasing. I was able to resolve this issue by using the delete function: 
 
      if (left) {
         delete left;
      }
      
As seen here, the delete function is used to delete the node pointer, left. Quite similarly, this method is used to deallocate the other node pointers. 

# Enhancement Three
Describe the artifact.

For Databases section of the ePortfolio, I selected to utilize restaurant data from the DAT 220 Final Project. The final project aimed to demonstrate methods of data mining and how tools, like JMP, can be used to illustrate patterns and outliers. This took place in the August of 2020, during the 20EW6 term. 

Justify the inclusion of the artifact. 

I selected this item because it would grant me the opportunity to showcase my ability and understanding of python, data bases, and data mining concepts. Through the enhancement process of this artifact, I aimed to create an interactive dashboard using pymongo, dash, Plotly, and other python imports. This artifact would be utilizing knowledge and skills learned from the CS 340: Advanced Programming Concepts course as well as the data mining techniques that were established through the DAT 220: Fundamentals of Data Mining class. Initially, I began the refinement process by importing the restaurant data into MongoDB. This showcased my understanding of MongoDB. Once that was completed, I used python (with several imports) to establish a connection to the local MongoDB server. In doing so, allowed me to build a dashboard using this data. This enhancement displayed the data in an easier to read format and incorporated a scatter plot to aid in depicting patterns in the data. 

Course Objectives

Reflecting on the code review, I stated that I aimed to meet the following course objective: “Design, develop, and deliver professional-quality oral, written, and visual communications that are coherent, technically sound, and appropriately adapted to specific audiences and context”. However, through this artifact refinements I was also able to achieve two additional course objectives: “Employ strategies for building collaborative environments that enable diverse audiences to support organizational decision making int the field of computer science” and “Demonstrate an ability to use well-founded and innovative techniques, skills, and tools, in computing practices for the purpose of implementing computer solutions that deliver value and accomplish industry-specific goals”. The first course objective was achieved through the incorporation of the scatter plot which communicates data patterns to users. I designed the graph to change according to dropdown selection. This would allow users to compare data against various values. For instance, it would depict which age groups are more likely to purchase from the webstore, or which state has the least amount of restaurant purchases. The second course objective was achieved through the usage of commenting. This allows other programmers to better understand the intent behind the program. In doing so, it creates an opportunity for discussion and improvement. As for the last course objective, I was able to achieve this objective through the incorporation of MongoDB. I was able to showcase how I could incorporate databases like MongoDB into a program. 

Reflection.

This project gave me the opportunity to research topics that I had only brushed up on in previous courses. It allowed me to better understand the advanced programming concepts demonstrated in CS 340. I was able to experiment with the various graphs offered by Plotly like scatter plots and pie charts. By experimenting with the various graphs, I was able to determine which graph better illustrated the data and showcased the comparisons between data. With this enhancement, I became more familiar with the various Python imports like dash and Plotly. I was also given the opportunity to enhance my understanding of callbacks which were quite confusing for me in a previous course. 
The most challenging portion of the project revolved around linking the drop downs to the graphs and having the graphs change according to the drop down selections. This was tricky. Initially, I thought the problem was with the callbacks. After much research, I was able to conclude that the callbacks were not the issue. Rather, it was the scatter plot’s x and y values. I had set the x and y values as a specific column from the restaurant data. For instance, x was assigned to restaurant and y was assigned to state. From this experience, I learned that if I wanted the graph to alter based on drop down selections that I needed to use the drop down IDs as the x and/or y values. 
Another issue that I found was adding and saving data to MongoDB from the dashboard. I have been able to add rows to the data table however, it did not except user input. This was a challenge that required me further research and experimentation. Through this process, I had found that the "editable" parameter had not been set. The default value for this parameter is set to "False" which prevents editing within the database. By adjusting the parameter's value to "True", it resolved this issue.   

# Code Review
Link: https://www.screencast.com/t/xoiB2GQ8Jtb7

# Artifact Files
[CS 499 A1 Final.zip](https://github.com/DIParham/ePortfolio/files/8090062/CS.499.A1.Final.zip)
[CS 499 A2 Final.zip](https://github.com/DIParham/ePortfolio/files/8090064/CS.499.A2.Final.zip)
[CS 499 A3 Final.zip](https://github.com/DIParham/ePortfolio/files/8090067/CS.499.A3.Final.zip)

