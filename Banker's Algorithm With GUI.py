import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import numpy as np

#global variables
MaximumNeed=[]
CurrentAllocation=[]
TotalRescources=[]
AvailableRescources=[]
RescourcesRequested=[]
Need=[]
Allocation=[]

class Ui_FirstWindow(object):
    def setupUi(self, FirstWindow):
        FirstWindow.setObjectName("FirstWindow")
        FirstWindow.resize(299, 407)
        self.centralwidget = QtWidgets.QWidget(FirstWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout.setSpacing(50)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Proccess_Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Proccess_Label.setFont(font)
        self.Proccess_Label.setObjectName("Proccess_Label")
        self.verticalLayout.addWidget(self.Proccess_Label)
        self.Process_EditText = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.Process_EditText.setFont(font)
        self.Process_EditText.setText("")
        self.Process_EditText.setObjectName("Process_EditText")
        self.verticalLayout.addWidget(self.Process_EditText, 0, QtCore.Qt.AlignHCenter)
        self.Resources_Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.Resources_Label.setFont(font)
        self.Resources_Label.setObjectName("Resources_Label")
        self.verticalLayout.addWidget(self.Resources_Label)
        self.Resources_EditText = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.Resources_EditText.setFont(font)
        self.Resources_EditText.setObjectName("Resources_EditText")
        self.verticalLayout.addWidget(self.Resources_EditText, 0, QtCore.Qt.AlignHCenter)
        self.Next_Button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Next_Button.setFont(font)
        self.Next_Button.setObjectName("Next_Button")
        self.verticalLayout.addWidget(self.Next_Button)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        FirstWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(FirstWindow)
        QtCore.QMetaObject.connectSlotsByName(FirstWindow)

    def retranslateUi(self, FirstWindow):
        _translate = QtCore.QCoreApplication.translate
        FirstWindow.setWindowTitle(_translate("FirstWindow", "FirstWindow"))
        self.Proccess_Label.setText(_translate("FirstWindow", "No. of Process"))
        self.Resources_Label.setText(_translate("FirstWindow", "No. of Resources"))
        self.Next_Button.setText(_translate("FirstWindow", "Next"))

#function for the resart button in the final window
    def Restart_Button_Clicked(self):
        FirstWindow.show()
        self.FifthWindow.close()
        self.Next_Button.clicked.connect(ui.Next_Button_Clicked)

#function for the output button in the final window
    def Output_Button_Clicked(self):
        processes_num = int(self.Process_EditText.text())
        resources_num = int(self.Resources_EditText.text())
        self.FinalWindow.close()
        self.go_to_fifth_window()
        self.FifthWindow.show()
        self.bankersAlgorithm(processes_num, resources_num, Need, Allocation, AvailableRescources)
        self.ui.Restart_Button.clicked.connect(ui.Restart_Button_Clicked)

#function for the check button in the third window
    def Check_Button_Clicked(self):
        if(self.check_inputwid_third()):
            if(self.check_inputwid_val_third()):
                if(self.check_positivewid_third()):
                    self.save_table_widget_third()
                    self.ui.Output_Button.clicked.connect(ui.Output_Button_Clicked)

#function for the next1 button in the second window
    def Next1_Button_Clicked(self):
        if(self.check_inputwid()):
           if(self.check_inputwid_val()):
                if(self.check_positivewid()):
                    self.save_table_widget()
                    self.ui.Check_Button.clicked.connect(ui.Check_Button_Clicked)

#function for the next button
    def Next_Button_Clicked(self):
        if(self.check_input()):
            if(self.check_input_val()):
                if(self.check_positive()):
                    self.save_input()
                    self.ui.Next1_Button.clicked.connect(ui.Next1_Button_Clicked)

#function to check if the inputs are not empty in the first window
    def check_input(self):
        if(self.Process_EditText.text() == "" or self.Resources_EditText.text() == ""):
            self.display_error("Please enter a number")
            return False
        return True
    
#function to check if the inputs are not empty in table widget in the second window
    def check_inputwid_val(self):
        processes_num = int(self.Process_EditText.text())
        resources_num = int(self.Resources_EditText.text())
        for i in range(processes_num):
            for j in range(resources_num):
                if  self.ui.TableWidget_MaximumNeed.item(i, j) is not None and \
                    self.ui.TableWidget_CurrentAllocation.item(i, j) is not None and \
                    self.ui.TableWidget_TotalRescources.item(0, j) is not None:
                    if(self.ui.TableWidget_MaximumNeed.item(i, j).text() == "" or self.ui.TableWidget_CurrentAllocation.item(i, j).text() == "" or self.ui.TableWidget_TotalRescources.item(0, j).text() == ""):
                        self.display_error("Please enter a number")
                        return False
                else:
                    self.display_error("Please enter a number")
                    return False
        return True
    
    def check_inputwid_val_third(self):
        resources_num = int(self.Resources_EditText.text())
        for j in range(resources_num):
            if  self.ui.TableWidget_AvailableRescources.item(0, j) is not None and \
                self.ui.TableWidget_RescourcesREquested.item(0, j) is not None:
                if(self.ui.TableWidget_AvailableRescources.item(0, j).text() == "" or self.ui.TableWidget_RescourcesREquested.item(0, j).text() == ""):
                    self.display_error("Please enter a number")
                    return False
            else:
                self.display_error("Please enter a number")
                return False
        return True

#function to check if the inputs are numbers in table widget in the second window
    def check_inputwid(self):
        processes_num = int(self.Process_EditText.text())
        resources_num = int(self.Resources_EditText.text())
        for i in range(processes_num):
            for j in range(resources_num):
                if  self.ui.TableWidget_MaximumNeed.item(i, j) is not None and \
                    self.ui.TableWidget_CurrentAllocation.item(i, j) is not None and \
                    self.ui.TableWidget_TotalRescources.item(0, j) is not None:
                    if(not self.ui.TableWidget_MaximumNeed.item(i, j).text().isnumeric() or not self.ui.TableWidget_CurrentAllocation.item(i, j).text().isnumeric() or not self.ui.TableWidget_TotalRescources.item(0, j).text().isnumeric()):
                        self.display_error("Please enter numbers only")
                        return False
                else:
                    self.display_error("Please enter numbers only")
                    return False
        return True
    
    def check_inputwid_third(self):
        processes_num = int(self.Process_EditText.text())
        resources_num = int(self.Resources_EditText.text())
        for i in range(processes_num):
            for j in range(resources_num):
                if  self.ui.TableWidget_AvailableRescources.item(0, j) is not None and \
                    self.ui.TableWidget_RescourcesREquested.item(0, j) is not None:
                    if(not self.ui.TableWidget_AvailableRescources.item(0, j).text().isnumeric() or not self.ui.TableWidget_RescourcesREquested.item(0, j).text().isnumeric()):
                        self.display_error("Please enter numbers only")
                        return False
                else:
                    self.display_error("Please enter numbers only")
                    return False
        return True

#functionto check if the inputs are positive integers in table widget in the second window
    def check_positivewid(self):
        processes_num = int(self.Process_EditText.text())
        resources_num = int(self.Resources_EditText.text())
        for i in range(processes_num):
            for j in range(resources_num):
                if  self.ui.TableWidget_MaximumNeed.item(i, j) is not None and \
                    self.ui.TableWidget_CurrentAllocation.item(i, j) is not None and \
                    self.ui.TableWidget_TotalRescources.item(0, j) is not None:
                    if(int(self.ui.TableWidget_MaximumNeed.item(i, j).text()) < 0 or int(self.ui.TableWidget_CurrentAllocation.item(i, j).text()) < 0 or int(self.ui.TableWidget_TotalRescources.item(0, j).text()) < 0):
                        self.display_error("Please enter positive integers only")
                        return False
                else:
                    self.display_error("Please enter positive integers only")
                    return False
        return True
    
    def check_positivewid_third(self):
        processes_num = int(self.Process_EditText.text())
        resources_num = int(self.Resources_EditText.text())
        for i in range(processes_num):
            for j in range(resources_num):
                if  self.ui.TableWidget_AvailableRescources.item(0, j) is not None and \
                    self.ui.TableWidget_RescourcesREquested.item(0, j) is not None:
                    if(int(self.ui.TableWidget_AvailableRescources.item(0, j).text()) < 0 or int(self.ui.TableWidget_RescourcesREquested.item(0, j).text()) < 0):
                        self.display_error("Please enter positive integers only")
                        return False
                else:
                    self.display_error("Please enter positive integers only")
                    return False
        return True
    

    #function to change the names of the columns and rows in the table widget in the second window
    def change_names(self, processes_num, resources_num):
        for i in range(1, processes_num+1):
            self.ui.TableWidget_MaximumNeed.setVerticalHeaderItem(i-1, QtWidgets.QTableWidgetItem("Process " + str(i)))
            self.ui.TableWidget_CurrentAllocation.setVerticalHeaderItem(i-1, QtWidgets.QTableWidgetItem("Process " + str(i)))
            self.ui.TableWidget_TotalRescources.setVerticalHeaderItem(i-1, QtWidgets.QTableWidgetItem("Total"))
        for i in range(1, resources_num+1):
            self.ui.TableWidget_MaximumNeed.setHorizontalHeaderItem(i-1, QtWidgets.QTableWidgetItem("Resource " + str(i)))
            self.ui.TableWidget_CurrentAllocation.setHorizontalHeaderItem(i-1, QtWidgets.QTableWidgetItem("Resource " + str(i)))
            self.ui.TableWidget_TotalRescources.setHorizontalHeaderItem(i-1, QtWidgets.QTableWidgetItem("Resource " + str(i)))

    def change_names_third(self, processes_num, resources_num):
        for i in range(1, processes_num+1):
            self.ui.TableWidget_AvailableRescources.setVerticalHeaderItem(i-1, QtWidgets.QTableWidgetItem("Total"))
            self.ui.TableWidget_RescourcesREquested.setVerticalHeaderItem(i-1, QtWidgets.QTableWidgetItem("Total"))
        for i in range(1, resources_num+1):
            self.ui.TableWidget_AvailableRescources.setHorizontalHeaderItem(i-1, QtWidgets.QTableWidgetItem("Resource " + str(i)))
            self.ui.TableWidget_RescourcesREquested.setHorizontalHeaderItem(i-1, QtWidgets.QTableWidgetItem("Resource " + str(i)))

    def change_names_final(self, processes_num, resources_num):
        for i in range(1, processes_num+1):
            self.ui.TableWidget_AvailableRescources1.setVerticalHeaderItem(i-1, QtWidgets.QTableWidgetItem("Total"))
            self.ui.TableWidget_RemainingRescources.setVerticalHeaderItem(i-1, QtWidgets.QTableWidgetItem("Process " + str(i)))
        for i in range(1, resources_num+1):
            self.ui.TableWidget_AvailableRescources1.setHorizontalHeaderItem(i-1, QtWidgets.QTableWidgetItem("Resource " + str(i)))
            self.ui.TableWidget_RemainingRescources.setHorizontalHeaderItem(i-1, QtWidgets.QTableWidgetItem("Resource " + str(i)))


    #function to save the table widget inputs in variables 2d arrays when the next1 button is clicked
    def save_table_widget(self):
        processes_num = int(self.Process_EditText.text())
        resources_num = int(self.Resources_EditText.text())
        TotalRescources.append([])
        for j in range(resources_num):
            TotalRescources[0].append(int(self.ui.TableWidget_TotalRescources.item(0, j).text()))
        for i in range(processes_num):
            MaximumNeed.append([])
            CurrentAllocation.append([])
            for j in range(resources_num):
                MaximumNeed[i].append(int(self.ui.TableWidget_MaximumNeed.item(i, j).text()))
                CurrentAllocation[i].append(int(self.ui.TableWidget_CurrentAllocation.item(i, j).text()))
        self.go_to_third_window()
        self.ui.TableWidget_AvailableRescources.setColumnCount(resources_num)
        self.ui.TableWidget_AvailableRescources.setRowCount(1)
        self.ui.TableWidget_RescourcesREquested.setColumnCount(resources_num)
        self.ui.TableWidget_RescourcesREquested.setRowCount(1)
        for i in range(processes_num):
            self.ui.comboBox.addItem("Process " + str(i+1))
        self.change_names_third(processes_num, resources_num)


    def save_table_widget_third(self):
        processes_num = int(self.Process_EditText.text())
        resources_num = int(self.Resources_EditText.text())
        AvailableRescources.append([])
        RescourcesRequested.append([])
        for j in range(resources_num):
            AvailableRescources[0].append(int(self.ui.TableWidget_AvailableRescources.item(0, j).text()))
            RescourcesRequested[0].append(int(self.ui.TableWidget_RescourcesREquested.item(0, j).text()))
        ProcessRequesting = self.ui.comboBox.currentIndex() + 1
        self.go_to_final_window()
        self.ui.TableWidget_AvailableRescources1.setColumnCount(resources_num)
        self.ui.TableWidget_AvailableRescources1.setRowCount(1)
        self.ui.TableWidget_RemainingRescources.setColumnCount(resources_num)
        self.ui.TableWidget_RemainingRescources.setRowCount(processes_num)
        self.change_names_final(processes_num, resources_num)
        self.calculate_allocated_rescources(Allocation,ProcessRequesting)
        self.calculate_need_rescources(Need)
        self.calculate_available_rescources()
        #set the values of list into the table widget
        for j in range(resources_num):
            self.ui.TableWidget_AvailableRescources1.setItem(0, j, QtWidgets.QTableWidgetItem(str(AvailableRescources[0][j])))
        #set the values of list into the table widget
        for i in range(processes_num):
            for j in range(resources_num):
                self.ui.TableWidget_RemainingRescources.setItem(i, j, QtWidgets.QTableWidgetItem(str(Need[i][j])))
        



    #function to display error message
    def display_error(self, message):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText(message)
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()



    #function to save the inputs in variables when the check button is clicked
    def save_input(self):
        processes_num = int(self.Process_EditText.text())
        resources_num = int(self.Resources_EditText.text())
        self.go_to_second_window()
        self.ui.TableWidget_MaximumNeed.setColumnCount(resources_num)
        self.ui.TableWidget_MaximumNeed.setRowCount(processes_num)
        self.ui.TableWidget_CurrentAllocation.setColumnCount(resources_num)
        self.ui.TableWidget_CurrentAllocation.setRowCount(processes_num)
        self.ui.TableWidget_TotalRescources.setColumnCount(resources_num)
        self.ui.TableWidget_TotalRescources.setRowCount(1)
        self.change_names(processes_num, resources_num)


    #function to check if the input is a number or not when the check button is clicked
    def check_input_val(self):
        try:
            int(self.Process_EditText.text())
        except ValueError:
            self.display_error("Please numbers only")
            return False
        try:
            int(self.Resources_EditText.text())
        except ValueError:
            self.display_error("Please numbers only")
            return False
        return True
    
    #function to calculate available rescources
    def calculate_available_rescources(self):
        processes_num = int(self.Process_EditText.text())
        resources_num = int(self.Resources_EditText.text())
        for i in range(resources_num):
            AvailableRescources[0][i] = TotalRescources[0][i]
            for j in range(processes_num):
                AvailableRescources[0][i] = AvailableRescources[0][i] - Allocation[j][i]

    #function to calculate need rescources
    def calculate_need_rescources(self, Need):
        processes_num = int(self.Process_EditText.text())
        resources_num = int(self.Resources_EditText.text())
        for i in range(processes_num):
            Need.append([])
            for j in range(resources_num):
                Need[i].append(int(MaximumNeed[i][j] - CurrentAllocation[i][j]))

    #function ro calculate aloocated rescources
    def calculate_allocated_rescources(self, Allocation, ProcessRequesting):
        processes_num = int(self.Process_EditText.text())
        resources_num = int(self.Resources_EditText.text())
        for i in range(processes_num):
            Allocation.append([])
            for j in range(resources_num):
                Allocation[i].append(int(RescourcesRequested[0][j]+CurrentAllocation[i][j]))

    # function to run the banker's algorithm

    def bankersAlgorithm(self,process, rescources, need, allocation, available):


            # calculate safe sequence and output the available table after each iteration
            # show error message if safe sequence does not exist
            # show info message if safe sequence exists

            # Check if the request can be fulfilled by comparing it with the Available resources:
            if any(RescourcesRequested[0][i] > available[0][i] for i in range(rescources)):
                QtWidgets.QMessageBox.warning(
                    self.centralwidget, "Result", "Request Denied, since it exceeds the Available resources")
                return

            # Check if the request can be fulfilled by comparing it with the Need resources:
            if any(RescourcesRequested[0][i] > need[0][i] for i in range(rescources)):
                QtWidgets.QMessageBox.warning(
                    self.centralwidget, "Result", "Request Denied, since it exceeds the Need resources")
                return

            safeSeq = []
            work = available.copy()
            finish = [False] * process
            while False in finish:
                for i in range(process):
                    if finish[i] == False:
                        for j in range(rescources):
                            if need[i][j] > work[0][j]:
                                break
                        else:
                            for j in range(rescources):
                                work[0][j] += allocation[i][j]
                            finish[i] = True
                            safeSeq.append(i + 1)
                            self.ui.outputTextEdit.append(
                                f"Available after P{i + 1} is executed: {work}")
                            

            if len(safeSeq) == process:
                QtWidgets.QMessageBox.information(
                    self.centralwidget, "Result", "Request Granted, since it is safe")
                return str(safeSeq)
            else:
                return "No safe sequence exists"

    #function to check if the input is a positive number or not when the check button is clicked
    def check_positive(self):
        if int(self.Process_EditText.text()) < 0:
            self.display_error("Please enter a positive number")
            return False
        if int(self.Resources_EditText.text()) < 0:
            self.display_error("Please enter a positive number")
            return False
            
        return True

    #function to go to second window if the input is correct
    def go_to_second_window(self):
            self.SecondWindow = QtWidgets.QMainWindow()
            self.ui = Ui_SecondWindow()
            self.ui.setupUi(self.SecondWindow)
            self.SecondWindow.show()
            FirstWindow.hide()

    def go_to_third_window(self):
            self.ThirdWindow = QtWidgets.QMainWindow()
            self.ui = Ui_ThirdWindow()
            self.ui.setupUi(self.ThirdWindow)
            self.ThirdWindow.show()
            self.SecondWindow.close()
            

    def go_to_final_window(self):
            self.FinalWindow = QtWidgets.QMainWindow()
            self.ui = Ui_FinalWindow()
            self.ui.setupUi(self.FinalWindow)
            self.FinalWindow.show()
            self.ThirdWindow.close()

    def go_to_fifth_window(self):
            self.FifthWindow = QtWidgets.QMainWindow()
            self.ui = Ui_FifthWindow()
            self.ui.setupUi(self.FifthWindow)
            self.FifthWindow.show()
            self.FinalWindow.close()


class Ui_SecondWindow(object):
    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.MaximumNeed_Label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.MaximumNeed_Label.setFont(font)
        self.MaximumNeed_Label.setObjectName("MaximumNeed_Label")
        self.horizontalLayout_2.addWidget(self.MaximumNeed_Label)
        self.TableWidget_MaximumNeed = QtWidgets.QTableWidget(self.widget)
        self.TableWidget_MaximumNeed.setObjectName("TableWidget_MaximumNeed")
        self.TableWidget_MaximumNeed.setColumnCount(0)
        self.TableWidget_MaximumNeed.setRowCount(0)
        self.horizontalLayout_2.addWidget(self.TableWidget_MaximumNeed)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.CurrentAllocation_Label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.CurrentAllocation_Label.setFont(font)
        self.CurrentAllocation_Label.setObjectName("CurrentAllocation_Label")
        self.horizontalLayout_3.addWidget(self.CurrentAllocation_Label)
        self.TableWidget_CurrentAllocation = QtWidgets.QTableWidget(self.widget)
        self.TableWidget_CurrentAllocation.setObjectName("TableWidget_CurrentAllocation")
        self.TableWidget_CurrentAllocation.setColumnCount(0)
        self.TableWidget_CurrentAllocation.setRowCount(0)
        self.horizontalLayout_3.addWidget(self.TableWidget_CurrentAllocation)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.HorizontalLayout = QtWidgets.QHBoxLayout()
        self.HorizontalLayout.setObjectName("HorizontalLayout")
        self.TotalRescources_Label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.TotalRescources_Label.setFont(font)
        self.TotalRescources_Label.setObjectName("TotalRescources_Label")
        self.HorizontalLayout.addWidget(self.TotalRescources_Label)
        self.TableWidget_TotalRescources = QtWidgets.QTableWidget(self.widget)
        self.TableWidget_TotalRescources.setObjectName("TableWidget_TotalRescources")
        self.TableWidget_TotalRescources.setColumnCount(0)
        self.TableWidget_TotalRescources.setRowCount(0)
        self.HorizontalLayout.addWidget(self.TableWidget_TotalRescources)
        self.verticalLayout_2.addLayout(self.HorizontalLayout)
        self.Next1_Button = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Next1_Button.setFont(font)
        self.Next1_Button.setObjectName("Next1_Button")
        self.verticalLayout_2.addWidget(self.Next1_Button, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addWidget(self.widget)
        SecondWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "SecondWindow"))
        self.MaximumNeed_Label.setText(_translate("SecondWindow", "Maximum Need"))
        self.CurrentAllocation_Label.setText(_translate("SecondWindow", "Current Allocation"))
        self.TotalRescources_Label.setText(_translate("SecondWindow", "Total Rescources"))
        self.Next1_Button.setText(_translate("SecondWindow", "Next"))


class Ui_FifthWindow(object):
    def setupUi(self, Fifthwindow):
        Fifthwindow.setObjectName("Fifthwindow")
        Fifthwindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Fifthwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 771, 561))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.outputTextEdit = QtWidgets.QTextEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.outputTextEdit.setFont(font)
        self.outputTextEdit.setReadOnly(True)
        self.outputTextEdit.setObjectName("outputTextEdit")
        self.verticalLayout.addWidget(self.outputTextEdit)
        self.Restart_Button = QtWidgets.QPushButton(self.widget)
        self.Restart_Button.setObjectName("Restart_Button")
        self.verticalLayout.addWidget(self.Restart_Button, 0, QtCore.Qt.AlignHCenter)
        Fifthwindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(Fifthwindow)
        QtCore.QMetaObject.connectSlotsByName(Fifthwindow)

    def retranslateUi(self, Fifthwindow):
        _translate = QtCore.QCoreApplication.translate
        Fifthwindow.setWindowTitle(_translate("Fifthwindow", "Fifthwindow"))
        self.outputTextEdit.setHtml(_translate("Fifthwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400;\"><br /></p></body></html>"))
        self.Restart_Button.setText(_translate("Fifthwindow", "Restart"))


class Ui_ThirdWindow(object):
    def setupUi(self, ThirdWindow):
        ThirdWindow.setObjectName("ThirdWindow")
        ThirdWindow.resize(626, 503)
        self.centralwidget = QtWidgets.QWidget(ThirdWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.AvailableREscource_Label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.AvailableREscource_Label.setFont(font)
        self.AvailableREscource_Label.setObjectName("AvailableREscource_Label")
        self.horizontalLayout_2.addWidget(self.AvailableREscource_Label)
        self.TableWidget_AvailableRescources = QtWidgets.QTableWidget(self.widget)
        self.TableWidget_AvailableRescources.setObjectName("TableWidget_AvailableRescources")
        self.TableWidget_AvailableRescources.setColumnCount(0)
        self.TableWidget_AvailableRescources.setRowCount(0)
        self.horizontalLayout_2.addWidget(self.TableWidget_AvailableRescources)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.RescourceRequested_Label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.RescourceRequested_Label.setFont(font)
        self.RescourceRequested_Label.setObjectName("RescourceRequested_Label")
        self.horizontalLayout_3.addWidget(self.RescourceRequested_Label)
        self.TableWidget_RescourcesREquested = QtWidgets.QTableWidget(self.widget)
        self.TableWidget_RescourcesREquested.setObjectName("TableWidget_RescourcesREquested")
        self.TableWidget_RescourcesREquested.setColumnCount(0)
        self.TableWidget_RescourcesREquested.setRowCount(0)
        self.horizontalLayout_3.addWidget(self.TableWidget_RescourcesREquested)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ProcessRequesting_Label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ProcessRequesting_Label.setFont(font)
        self.ProcessRequesting_Label.setObjectName("ProcessRequesting_Label")
        self.horizontalLayout.addWidget(self.ProcessRequesting_Label)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.Check_Button = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Check_Button.setFont(font)
        self.Check_Button.setObjectName("Check_Button")
        self.verticalLayout_2.addWidget(self.Check_Button, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.widget)
        ThirdWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ThirdWindow)
        QtCore.QMetaObject.connectSlotsByName(ThirdWindow)

    def retranslateUi(self, ThirdWindow):
        _translate = QtCore.QCoreApplication.translate
        ThirdWindow.setWindowTitle(_translate("ThirdWindow", "ThirdWindow"))
        self.AvailableREscource_Label.setText(_translate("ThirdWindow", "Available Rescources"))
        self.RescourceRequested_Label.setText(_translate("ThirdWindow", "Rescources Requested By Process"))
        self.ProcessRequesting_Label.setText(_translate("ThirdWindow", "Process Requesting Rescource"))
        self.Check_Button.setText(_translate("ThirdWindow", "Check"))

        



class Ui_FinalWindow(object):
    def setupUi(self, FinalWindow):
        FinalWindow.setObjectName("FinalWindow")
        FinalWindow.resize(800, 522)
        self.centralwidget = QtWidgets.QWidget(FinalWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.AvailableRescource1_Label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.AvailableRescource1_Label.setFont(font)
        self.AvailableRescource1_Label.setObjectName("AvailableRescource1_Label")
        self.horizontalLayout_2.addWidget(self.AvailableRescource1_Label)
        self.TableWidget_AvailableRescources1 = QtWidgets.QTableWidget(self.widget)
        self.TableWidget_AvailableRescources1.setObjectName("TableWidget_AvailableRescources1")
        self.TableWidget_AvailableRescources1.setColumnCount(0)
        self.TableWidget_AvailableRescources1.setRowCount(0)
        self.horizontalLayout_2.addWidget(self.TableWidget_AvailableRescources1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.RemainingRescources_Label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.RemainingRescources_Label.setFont(font)
        self.RemainingRescources_Label.setObjectName("RemainingRescources_Label")
        self.horizontalLayout_3.addWidget(self.RemainingRescources_Label)
        self.TableWidget_RemainingRescources = QtWidgets.QTableWidget(self.widget)
        self.TableWidget_RemainingRescources.setObjectName("TableWidget_RemainingRescources")
        self.TableWidget_RemainingRescources.setColumnCount(0)
        self.TableWidget_RemainingRescources.setRowCount(0)
        self.horizontalLayout_3.addWidget(self.TableWidget_RemainingRescources)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.Output_Button = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.Output_Button.setFont(font)
        self.Output_Button.setObjectName("Output_Button")
        self.verticalLayout_2.addWidget(self.Output_Button, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.widget)
        FinalWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(FinalWindow)
        QtCore.QMetaObject.connectSlotsByName(FinalWindow)

    def retranslateUi(self, FinalWindow):
        _translate = QtCore.QCoreApplication.translate
        FinalWindow.setWindowTitle(_translate("FinalWindow", "FinalWindow"))
        self.AvailableRescource1_Label.setText(_translate("FinalWindow", "Available Rescources"))
        self.RemainingRescources_Label.setText(_translate("FinalWindow", "Need Table"))
        self.Output_Button.setText(_translate("FinalWindow", "Output"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FirstWindow = QtWidgets.QMainWindow()
    ui = Ui_FirstWindow()
    ui.setupUi(FirstWindow)
    FirstWindow.show()
    ui.Next_Button.clicked.connect(ui.Next_Button_Clicked)
    sys.exit(app.exec_())
    
