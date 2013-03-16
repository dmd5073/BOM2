import sys


<<<<<<< HEAD
def yes_no(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes', 'Y', 'Ye', 'Yes', 'YES'):
            return True
        if ok in ('n', 'no', 'nop', 'nope', 'N', 'No', 'NO'):
=======
def yesno(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        reply0 = raw_input(prompt)
        if reply0.lower()[0]=="y":
            return True
        if reply0.lower()[0]=="n":
>>>>>>> New Updates
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint

<<<<<<< HEAD
yes_no("Would you like to continue (Y/N): ")
=======


>>>>>>> New Updates
