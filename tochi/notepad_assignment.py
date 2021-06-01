file_path = r"C:\Users\HP\Documents\UNIVELCITY\DATA_SCIENCE\git\4B3b-Assignments-Project\tochi\files\login_details.csv"

file = open(file_path,"r")
contents = file.read()


# def checkPassword():
#     if password == " username[1].password"

def write_file():   
    task = input("Which tasks do you have for today --> ")
    task_file_path = r"C:\Users\HP\Documents\UNIVELCITY\DATA_SCIENCE\git\4B3b-Assignments-Project\tochi\files\task_file.txt"
    task_file = open(task_file_path, "a")

    # i = 0
    # while i < 10 i+=1:
    print(task,file=task_file)

def login():
    username = input('enter your username :-> ')
    if username not in contents:
        new_user_response = input('It appears you are a new user. Do you want to create an account? (y/n) -> ')
        if new_user_response == 'y':
            new_username = input('Please enter your new username --> ')
            new_pass = input(" Create your new password --> ")
            user_dict = {new_username:{"username":new_username, "password": new_pass}}
            file = open(file_path, "a")
            print(user_dict, file=file)
            print(f"Welcome {username} Good day")
            return write_file()

        else:
            print('Closing App ----> \n Have a nice day')

    else:
        user_pass = input("Enter your password --> ")
        if user_pass in contents:
            write_file()
        else:
            login()
            

login()




