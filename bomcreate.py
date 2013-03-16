import csv
import yesno
import youenter

<<<<<<< HEAD
print "Welcome to the project Bill of Materail Creator. Would like to continue? Y/N"
def confirm(prompt, resp=False):
    """prompts for yes or no response from the user. Returns True for yes and
    False for no.

    'resp' should be set to the default value assumed by the caller when
    user simply types ENTER.

    >>> confirm(prompt='Create Directory?', resp=True)
    Create Directory? [y]|n: 
    True
    >>> confirm(prompt='Create Directory?', resp=False)
    Create Directory? [n]|y: 
    False
    >>> confirm(prompt='Create Directory?', resp=False)
    Create Directory? [n]|y: y
    True

    """
    
    if prompt is None:
        prompt = 'Confirm'

    if resp:
        prompt = '%s [%s]|%s: ' % (prompt, 'y', 'n')
    else:
        prompt = '%s [%s]|%s: ' % (prompt, 'n', 'y')
        
    while True:
        ans = raw_input(prompt)
        if not ans:
            return resp
        if ans not in ['y', 'Y', 'n', 'N']:
            print 'please enter y or n.'
            continue
        if ans == 'y' or ans == 'Y':
            return True
        if ans == 'n' or ans == 'N':
            return False
        
print "Please Enter Your ENE Project Number:"
print "Please Enter Your Cleint's Name:"
print "Please Enter Your Cleint's Workorder Number"
print "Please Enter Your Design Pressure:"
print "Please Enter Your Design Factor:"
=======
if(not yesno.yesno("Welcome to the Bill of Material Creator. Would you like to continue (Y/N)?")):
    exit()

ProjectNum = raw_input ("Please Enter Your ENE Project Number:")
youenter.youenter(ProjectNum, "Please Renter Your ENE Project Number:")

Clientname = raw_input ("Please Enter Your Client's Name:")
youenter.youenter(Clientname, "Please Renter Your Client's Name:")
                        
ClientWON = raw_input ("Please Enter Your Client's Workorder Number:")
youenter.youenter(ClientWON, "Please Renter Your Client's Workorder Number:")

DP = raw_input ("Please Enter Your Design Pressure:")
youenter.youenter(DP, "Please Renter Your Design Pressure:")

DF = raw_input ("Please Enter Your Design Factor:")
youenter.youenter(DF, "Please Renter Your Design Factor:")

DWG_NO = raw_input("Please Enter the Drawing Number where the Bill of Material item will be located:")
youenter.youenter(DWG_NO, "Please Renter Your Drawing Number:")
>>>>>>> New Updates
