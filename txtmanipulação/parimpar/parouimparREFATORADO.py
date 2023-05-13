"""

This version supports more than one digit

"""



import linecache

with open("file.txt", "w") as txt:
    print("Use [0] to Stop")
    usr_w = ""

    while usr_w != "0":
        usr_w = input("Insert What do You Want to Write: ")
        lista = []

        lista.append(usr_w)
        txt.write(lista[0] + "\n")

    txt.close()

with open("file.txt", "r") as txt:

    lentxtlist = txt.readlines()
    lentxt = len(lentxtlist)

    line = 1
    count = 0
    while count < lentxt:
        rdtxt = linecache.getline("file.txt", line).strip()

        try:
            rdtxt = int(rdtxt)
            calc = rdtxt % 2

            if calc == 0:
                print(f"{rdtxt} is Pair")
            else:
                print(f" {rdtxt} is Odd")

        except:
            print(f"Invalid, '{rdtxt}' Isn't a Number")



        line += 1
        count += 1
