# Introduction
This is an implementation of The Banker's Algorithm using Python Which is a resource allocation and deadlock avoidance algorithm that tests for safety by simulating the allocation of predetermined maximum possible amounts of all resources, and then makes an "s-state" check to test for possible deadlock conditions for all other pending activities.
# Requirments
Visual Studio Code & Python 3.10 or higher
# Installation
**This is a Python file and it is recommended to run it in Visual Studio Code since it was initially created on it so here are the steps:**
1. Click on **[VS Code](https://code.visualstudio.com/Download)** to download it
2. Click on **[Python](https://www.python.org/downloads/)** to download any version you want   "***Note: it is recommended to use Python 3.10 or Higher***"
3. Open VS Code and Choose the Python Interpeter as your Python version
* Open The Console and type ***"pip install pyqt5"*** when it is finished type ***"pip install pyqt5.tools"***
* Open The Extensions on the left bar and make sure both ***"Python"*** & ***"PYQT Integeration"*** are both installed then restart VS Code
* Open The Python file in VS Code and run it 
# How To Use
## First Window - Take Inputs
This is the initial window for the program it will ask you to enter the number of processes and number of rescources to get started

![First Window](/Screenshot/First_Window.png "First Window")

After you fill the inputs you click on "***Next***" so it can the take you to the next window and save the number of processes and rescourses

***Note :*** **Exception Handling is preformed on all the cells to make sure the values taken are positive integers only (Numbers only,non-negative values,non-null cells)**

![First Window Filled](/Screenshot/First_Window_Filled.png "First Window Filled")
## Second Window - Take Inputs 2
Here Table Widgets are created based on the number of processes and number of rescources

![Second Window](/Screenshot/Second_Window.png "Second Window")

### Table Widgets
* **Maximum Need** : Takes the inputs for the maximum need of each process for every resource
* **Current Allocation** : Takes the inputs for the currently allocated rescource for every process
* **Total Rescources** : Takes The inputs for the total rescources the system has

![Second Window Filled](/Screenshot/Second_Window_Filled.png "Second Window Filled")

Then after filling the tables with data we click on "***Next***" to take us to the third window

***Note :*** **Exception Handling is preformed on all the cells to make sure the values taken are positive integers only (Numbers only,non-negative values,non-null cells)**
## Third Window - Take Inputs 3
Here Are Another table widgets but it's advised to set all the cells here in 0 as no test were done with values in those table widgets

![Third Window](/Screenshot/Third_Window.png "Third Window")

### Table Widgets
* **Available Rescources** : Takes the inputs for the available rescources for the processes
* **Rescources Requested** : Takes the inputs for the number of rescources requested by a certain process
### Combo Box
* **Process Requesting** : Define the process that is requesting rescources

After Filling the tables click on "***Check***" to calculate the available rescources and need tables in the next window

***Note :*** **Exception Handling is preformed on all the cells to make sure the values taken are positive integers only (Numbers only,non-negative values,non-null cells)**

## Fourth Window - Finalizing The Tables for calculations
Here the available rescources for the process and the need table are calculated and displayed

![Fourth Window](/Screenshot/Fourth_Window.png "Fourth Window")

### Table Widgets
* **Available Rescources** : The Available Rescources for the processes are displayed here after the calculation (***Available Rescources = Total Rescources - Current Allocation***)
* **Need Table** : The Need Table is displayed which represents the remaining need of each process for each rescource after it was calculated (***Need Table = Maximum Need - Current Allocation***)

After Checking the tables click (***Output***) to Check whether the system is safe or not and see the process sequence

## Fifth Window - Display Output
Here The System checks whether it's safe for the process to take rescources or not and if it's safe the sequence is displayed in the output box and a message appears to show that the access is granted & if the system isn't safe then a message box appears and tells the user that it isn't safe
### Safe

![Final Window](/Screenshot/Final_Window.png "Final Window")

### Unsafe

![Final2 Window](/Screenshot/Final2_Window.png "Final2 Window")

After you finish the checking and the results are shown you can then click "***Restart***" to restart the whole algorithm from the beginning
# Credits
This Program was created by Walid Atef
