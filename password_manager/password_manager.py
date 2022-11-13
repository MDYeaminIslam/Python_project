#from cryptography.fernet import Fernet

#youtube video 1:28:00 minutes
master_pwd_key = "hello68"
master_pwd = input("What is the master password?")

def view():
    #here we will read the Account name and password which is entered early.
    #rstrip() will remove the extra space from the end of the line.
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user,passw = data.split("|")
            print("User:",user," | Password:",passw)

def add():
    name = input("Account name: ")
    pwd = input("Password: ")
    
    #this "with" will open the text file and automatically close the file
    #'w' is used to write the file
    # 'r' is used to write the file
    #'a' is used to append the file and create the file if this is not exit. And also read the file and also start write from the end of the file.

    with open('passwords.txt', 'a') as f:
        f.write(name + '|' + pwd + '\n')



if master_pwd_key == master_pwd:
    while True:
        mode = input("Would you like to add a new password or view existing ones (view, add) or press q to quit!").lower()
        if mode == "q" or mode == "Q":
            break

        if mode == "view":
            view()
        elif mode == "add":
            add()
        else:
            print("Invalid mode.")
            continue

else:
    print("Invalid master password!")
