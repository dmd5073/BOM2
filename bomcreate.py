import csv
import yesno
import youenter

if(not yesno.yesno("Welcome to the Bill of Material Creator. Would you like to continue (Y/N)?")):
    exit()

ProjectNum = raw_input ("Please Enter Your ENE Project Number:")
youenter.youenter(ProjectNum, "Please Renter Your ENE Project Number:")

Clientname = raw_input ("Please Enter Your Client's Name:")
youenter.youenter(Clientname, "Please Renter Your Client's Name:")
                        
ClientWON = raw_input ("Please Enter Your Client's Workorder Number:")
youenter.youenter(ClientWON, "Please Renter Your Client's Workorder Number:")

print "Now that you have provide the information require to setup the Bill of Material file."
print "Please provide the following design parameters." 

while True:
    if (yesno.yesno("Will your design information change throughout this project(Y/N)?")):

    else:
        print "I Work"

yesno.yesno("Will you have mutiple drawing that you will be adding to the Bill of Material(Y/N)?")

DWG_NO = raw_input("Please Enter the Drawing Number where the Bill of Material item will be located:")
youenter.youenter(DWG_NO, "Please Renter Your Drawing Number:")

DP = raw_input ("Please Enter Your Design Pressure:")
youenter.youenter(DP, "Please Renter Your Design Pressure:")

DF = raw_input ("Please Enter Your Design Factor:")
youenter.youenter(DF, "Please Renter Your Design Factor:")

print"Thank you for adding your design information."
