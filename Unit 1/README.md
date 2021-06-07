# This Week's Reading
This week, please read the following:
- Beginner's guide to Python in ArcGIS Pro, Part 1: Why?
- Beginner’s guide to Python in ArcGIS Pro, Part 2: How?
- Chapters 1 and Chapters 4 of Python Scripting for ArcGIS Pro

# Last Year's Week 1 Lecture Recording
Here are the links to the first lecture from last year. This link is not intended to be used in place of this week's lecture. I am providing it as an additional resource for extra context.
- First half of lecture - https://slu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=e01fab5b-e86b-4f7a-b584-ab41016e8a56
- Second half of lecture - https://slu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=d55b6de0-817d-479d-86d6-ab410188ecf4

# Presentations
Here are the PowerPoint slides that I plan to use for week 1.
Attached Files:

    File Lecture_1_Slides.pptx Click for more options (2.058 MB)
    File Welcome.pptx Click for more options (515.31 KB) 

# Data and Notebooks
This week's lecture notebooks can be found in the [GIS 4090\5090 Unit 1 Notebooks](This week's lecture notebooks can be found in the GIS 4090\5090 Unit 1 Notebooks group on ArcGIS Online or downloaded here. Please download the Missouri.gdb.zip so that we can use it for the lecture.) 
group on ArcGIS Online or downloaded here. 
Please download the Missouri.gdb.zip so that we can use it for the lecture.
Attached Files:

    File unit_1_lesson_1_introto_python.ipynb Click for more options (36.852 KB)
    File unit_1_lesson_2_more_python.ipynb Click for more options (19.851 KB)
    File Missouri.gdb.zip Click for more options (10.712 MB) 
    
# Configuring Jupyter Notebooks
This document provides instructions to configure Jupyter Notebooks on your computer. We will go through this process 
to setup Jupyter Notebooks on your lab computer or personal computer.
Attached Files:

    File configuring_the_notebook_directory.html Click for more options (269.886 KB) 
    
# Unit 1 Exercise and Discussion Questions
## Exercises

Before completing the assignment, I recommend completing the following exercises. Completing these 3 exercises should not take more than an hour.

    Complete the Hello, Notebook !exercise. After you complete it, add another map object and a different dataset to the map. Save the Notebook and share the link to the Notebook here. I will be able to see your notebook even if you don't explicitly share it with me in ArcGIS Online because I am an administrator in the ArcGIS Online organization.
    Please complete Python Scripting for ArcGIS Pro Exercise 1. This should take no more than 15 minutes.
    Please complete Python Scripting for ArcGIS Pro Exercise 4. This will take a little bit longer but I think you will find it very helpful. Please submit the Python scripts that you create.

## Discussion Questions

Please submit a Word file or text file that answers the following questions.

    What is the version Python that comes with ArcGIS Pro?
    Name 3 methods of string objects in Python and give an example of each.
    What two values can a boolean take on?
    How do you denote a comment line in Python and what should yo use comments?
   
# Unit 1 Assignment
## Assignment

Please submit a Word file, text file, or ArcGIS Notebook that answers the following questions. If you do this in ArcGIS Notebooks, you can save the notebook and just send me a URL to the item in ArcGIS Online. 

1. Consider the following variable called happyCow

happyCow = 'meadows.shp'

Determine the following:

    happyCow[0]
    happyCow[0:5] + happyCow[-4:]
    len(happyCow)
    happyCow[0:5]
    happyCow[-4:]
    happyCow[11]
    happyCow[:5]
    happyCow in "5meadows.shp"
    happyCow[5]
    'W' in happyCow


2.  Determine if each statement is True or False using the variable LCS_ID = '0017238'

    '17' in LCS_ID
    LCS_ID.isdigit()
    LCS_ID.lstrip('0') == '17238'
    LCS_ID.zfill(10) == '10101010'
    LCS_ID + '10' == 17248
    LCS_ID[6] == '3'
    len(LCS_ID) == 7
    LCS_ID[0:7] == '0017238'
    int(LCS_ID) + 10 == 17248
    LCS_ID != 17238

3.  The list variable 'census' is as follows:

census = ['4', '3', '79', '1', '66', '9', '1']

Determine the following:

    len(census)
    census.insert(0,2)
    census.append(2)
    census.remove('1')
    census = '0'.join(census)
    census.pop(3)
    census.count('1')
    census.sort()
    census.reverse()


4. Consider the following list:

mylist = ["Athens", "Barcelona", "Cairo", "Florence", "Helsinki"]

Determine the results of the following:

    len(mylist)
    mylist[2]
    mylist[1:]
    mylist[-1]
    mylist.index("Cairo")
    mylist.pop(1)
    mylist.sort(reverse = True)
    mylist.append("Berlin")

These operations are all to be performed on the original list—that is, not as a sequence of operations. Try to determine the answer manually first, and then check your result by running the code.
