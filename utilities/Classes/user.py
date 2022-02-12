from utilities.db.db_manager import dbManager

class User:
    __Name = None
    __BirthDate = None
    __Email = None
    __Phone_number = None
    __Password = None

    def __init__(self,Name, BirthDate ,Email,Phone_number, Password):
        self.__Name = Name
        self.__BirthDate = BirthDate
        self.__Email = Email
        self.__PhoneNumber = Phone_number
        self.__password = Password

    def insert_user(self):
        query = "INSERT INTO web_project_g8.users (Name, BirthDate ,Email,Phone_Number, Password) VALUES ('%s','%s','%s', '%s','%s')" % (self.__Name, self.__BirthDate, self.__Email, self.__PhoneNumber, self.__password)
        dbManager.commit(query)


    def get_name(self, Email, Password):
        query = "SELECT Name, Password FROM web_project_g8.users WHERE Email = '%s'" %(Email)
        result = dbManager.fetch(query)
        if result:
            if Password == result[0][1]:
                return result[0][0]
            else:
                return "wrong_psw"
        else:
            return ""

    def get_user_id(self, Email):
        query = "SELECT User_id FROM web_project_g8.users WHERE Email = '%s';" %(Email)
        result = dbManager.fetch(query)
        if result:
            return result[0][0]
        else:
            return ""

    def get_email(self, Email):
        query = "SELECT Email FROM web_project_g8.users WHERE Email = '%s'" %(Email)
        result = dbManager.fetch(query)
        if result:
            return False
        else:
            return True

    def update_userName(self, User_id, Name):
        query = "UPDATE web_project_g8.users SET Name='%s' WHERE User_id='%s';" % (Name, User_id)
        dbManager.commit(query)

    def update_userEmail(self, User_id, Email):
        query = "UPDATE web_project_g8.users SET Email='%s' WHERE User_id='%s';" % (Email, User_id)
        dbManager.commit(query)

    def update_userPhone(self, User_id, Phone_number):
        query = "UPDATE web_project_g8.users SET Phone_number='%s' WHERE User_id='%s';" % (Phone_number, User_id)
        dbManager.commit(query)

    def update_userPass(self, User_id, Password):
        query = "UPDATE web_project_g8.users SET Password='%s' WHERE User_id='%s';" % (Password, User_id)
        dbManager.commit(query)

