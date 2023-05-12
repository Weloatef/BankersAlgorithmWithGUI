# BankersAlgorithmWithGui
This is an implementation of The Banker's Algorithm using Python Which is a resource allocation and deadlock avoidance algorithm that tests for safety by simulating the allocation of predetermined maximum possible amounts of all resources, and then makes an "s-state" check to test for possible deadlock conditions for all other pending activities.
# Requirments
Visual Studio Code & Python 3.10 or higher
# Installation
**This is a Python file and it is recommended to run it in Visual Studio Code since it was initially created on it so here are the steps:**
* Click on **[VS Code](https://code.visualstudio.com/Download)** to download it
* Click on **[Python](https://www.python.org/downloads/)** to download any version you want   "***Note: it is recommended to use Python 3.10 or Higher***"
* Open VS Code and Choose the Python Interpeter as your Python version
* Open The Console and type ***"pip install pyqt5"*** when it is finished type ***"pip install pyqt5.tools"***
* Open The Extensions on the left bar and make sure both ***"Python"*** & ***"PYQT Integeration"*** are both installed then restart VS Code
* Open The Python file in VS Code and run it 
# How To Use
## First Window - Take Inputs
This is the initial window for the program it will ask you to enter the number of processes and number of rescources to get started

![First Window](/Screenshot/First_Window.png "First Window")

After you fill the inputs you click on next so it can the take you to the next window and save the number of processes and rescourses

![First Window Filled](/Screenshot/First_Window_Filled.png "First Window Filled")
## Second Window - Take Inputs 2
Here Table Widgets are created based on the number of processes and number of rescources

![Second Window](/Screenshot/Second_Window.png "Second Window")

### Table Widgets
* **Maximum Need** : Takes the inputs for the maximum need of each process for every resource
* **Current Allocation** : Takes the inputs for the currently allocated rescource for every process
* **Total Rescources** :Takes The inputs for the total rescources the system has

![Second Window Filled](/Screenshot/Second_Window_Filled.png "Second Window Filled")


