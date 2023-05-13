"""
password mananger
master password -> all passwords
"""

import linecache


def npass():

    count = 0
    qtdpass = int(input("How much Passwords: "))

    with open("psw.txt", "a") as txt:
        while count < qtdpass:
            newpass = input("What do You Want to Save: ")
            txt.write("\n" + newpass + "\n")
            count += 1
        txt.close()
        pswman()



def pswman():
    login = input("Already Have An Account? [y, n]: ").upper()

    if login == "Y":
        usr = input("User: ").upper()
        psw = input("Password: ").upper()
        #txt = open("psw.txt", "r")

        with open("psw.txt", "r") as txt:

            usrconf = linecache.getline("psw.txt", 1).strip()
            pswconf = linecache.getline("psw.txt", 2).strip()

            if usrconf == usr and pswconf == psw:
                print(txt.read())
                confer = input("Add More Passwords [y, n]: ").upper()
                if confer == "Y":
                    npass()
                else: print("Ok! Finishing...")

            else:
                print("Invalid User or Password")

    elif login == "N":

        crt_acc_usr = input("Let's Create One? Enter With Your User: ").upper()
        crt_acc_psw = input("Enter With Your Master Password: ").upper()

        print("Creating User...")

        with open("psw.txt", "w") as txt:
            txt.write(crt_acc_usr + "\n" + crt_acc_psw)

        pswman()

    else:
        print("Invalid Answare")
        pswman()

pswman()
