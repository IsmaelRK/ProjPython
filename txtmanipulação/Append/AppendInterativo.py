with open("file.txt", "w") as txt:
    print("Use [0] to Stop")
    usr_w = ""

    while usr_w != "0":
        usr_w = input("Insert What do You Want to Write: ")
        txt.write(usr_w + "\n")

    txt.close()

with open("file.txt", "r") as txt:
    print(txt.read())
