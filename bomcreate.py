import csv
import yesno
import youenter

if(not yesno.yesno("Welcome to the Bill of Material Creator. Would you like to continue?(Y/N)")):
    exit()

ProjectNum = raw_input ("Please Enter Your ENE Project Number:")
youenter.youenter(ProjectNum, "Please Renter Your ENE Project Number:")

Clientname = raw_input ("Please Enter Your Client's Name:")
youenter.youenter(Clientname, "Please Renter Your Client's Name:")
                        
ClientWON = raw_input ("Please Enter Your Client's Workorder Number:")
youenter.youenter(ClientWON, "Please Renter Your Client's Workorder Number:")

print "Now that you have provide the information require to setup the Bill of Material file."
print "Please provide the following design parameters." 

while (yesno.yesno("Will you have mutiple drawing that you will be adding a Bill of Material too?(Y/N)")):
    if (yesno.yesno("Will your design information change from drawing to drawing?(Y/N)")):
        while (DWGNO = raw_input("Please Enter the Drawing Number where the Bill of Material item will be located:")):
            youenter.youenter(DWG_NO, "Please Renter Your Drawing Number:")

            DP = raw_input ("Please Enter Your Design Pressure:")
            youenter.youenter(DP, "Please Renter Your Design Pressure:")

            DF = raw_input ("Please Enter Your Design Factor:")
            youenter.youenter(DF, "Please Renter Your Design Factor:")

            yesno.yesno("Would you like to add another drawing?(Y/N")
        print "WES ADDED THIS LINE"
    else:
        print "I Work"
        break



DWGNO = raw_input("Please Enter the Drawing Number where the Bill of Material item will be located:")
youenter.youenter(DWG_NO, "Please Renter Your Drawing Number:")

DP = raw_input ("Please Enter Your Design Pressure:")
youenter.youenter(DP, "Please Renter Your Design Pressure:")

DF = raw_input ("Please Enter Your Design Factor:")
youenter.youenter(DF, "Please Renter Your Design Factor:")

print"Thank you for adding your design information."
