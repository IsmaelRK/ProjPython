"""

This version doesn't support more than one digit

"""


import linecache

with open("file.txt", "w") as txt:
    print("Use [0] to Stop")
    usr_w = ""

    while usr_w != "0":
        usr_w = input("Insert What do You Want to Write: ")

        txt.write(usr_w + "\n")

    txt.close()

with open("file.txt", "r") as txt:

    lentxtlist = txt.readlines()
    lentxt = len(lentxtlist)

    line = 1
    count = 0
    while count < lentxt:
        rdtxt = linecache.getline("file.txt", line).strip()
        for n in rdtxt:
            try:
                n = int(n)
                calc = n % 2
                if calc == 0:
                    print(f"{n} is Pair")
                else:
                    print(f" {n} is Odd")
            except:
                print(f" {n} is Invalid!")
                break

        line += 1
        count += 1
