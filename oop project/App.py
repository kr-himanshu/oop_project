from mydb import Database
from MyApi import ApiManager

class Nlpapp:
    def __init__(self):
        self.__db = Database()
        self.__api = ApiManager()
        self.__first_menu()

    def __first_menu(self):
        first_input = input("""
        Hi! How would you like to proceed?
        1. Not a Member, Register.
        2. Already a Member, Login.
        3. Exit
        """)
        if first_input == "1":
            self.__register()
        elif first_input == "2":
            self.__login()
        elif first_input == "3":
            exit()
        else:
            print("Invalid option. Please enter a valid option.")
            self.__first_menu()

    def __second_menu(self):
        second_input = input("""
        Hi! How would you like to proceed?
        1. Sentiment Analysis
        2. NER
        3. Emotion Analysis
        4. Abuse Detection
        5. Logout
        """)
        if second_input == "1":
            text = input("Enter Text: ")
            response = self.__api.sentiment_analysis(text)
            print(response)
        elif second_input == "2":
            text =input("Enter Text ")
            response = self.__api.ner(text)
            print(response)
        elif second_input == "3":
            text = input("Enter Text ")
            response = self.__api.emotion_analysis(text)
            print(response)
        elif second_input == "4":
            text=input("Enter Text ")
            response= self.__api.abuse_detection(text)
            print(response)
        elif second_input == "5":
            print("Thank You For using NlpApp")
            exit()
        else:
            print("Invalid option. Please enter a valid option.")
        self.__second_menu()

    def __register(self):
        name = input("Enter Your Name: ")
        email = input("Enter Your Email: ")
        password = input("Enter Your Password: ")

        response = self.__db.add_data(name, email, password)
        if response:
            print("Registration Successful. Login Now.")
        else:
            print("Email Already Exists.")
        self.__login()

    def __login(self):
        email = input("Enter Your Email: ")
        password = input("Enter Your Password: ")
        response = self.__db.search(email, password)
        if response:
            print("Login Successful.")
            self.__second_menu()
        else:
            print("Incorrect Email/Password.")
            self.__login()

obj = Nlpapp()
