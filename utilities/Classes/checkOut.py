from utilities.db.db_manager import dbManager

class Check_out:
    __user_id = None
    __CC_Number = None
    __CC_Holder_id = None
    __Expire_month = None
    __Expire_year = None
    __CVC = None

    def __init__(self, User_id, CC_Number, CC_Holder_id, Expire_month, Expire_year, CVC):
        self.__user_id = User_id
        self.__CC_Number = CC_Number
        self. __CC_Holder_id = CC_Holder_id
        self.__Expire_month = Expire_month
        self.__Expire_year = Expire_year
        self.__CVC = CVC

    def check_if_CC_exists(self,CC_Number):
        query= "SELECT * FROM web_project_g8.credit_cards WHERE CC_Number = '%s';" %(CC_Number)
        result = dbManager.fetch(query)
        if result:
            return True
        else:
            return False

    def insert_credit_card(self, CC_Number,User_id, CC_Holder_id, Expire_month, Expire_year, CVC):
        query = "INSERT INTO web_project_g8.credit_cards(CC_Number,User_id, CC_Holder_id, Expire_month, Expire_year, CVC) VALUES ('%s','%s','%s','%s','%s','%s')" % (CC_Number,User_id, CC_Holder_id, Expire_month, Expire_year, CVC)
        dbManager.commit(query)

    def update_ordered(self, User_id):
        query = "UPDATE web_project_g8.donations SET Ordered=1 WHERE Ordered =0 AND User_id= '%s';" %(User_id)
        dbManager.commit(query)

    # What to do with the pictures ???
    def user_choices(self, User_id):
        query = "SELECT p.Name, d.Quantity, p.Price, p.Photo FROM web_project_g8.users as u JOIN web_project_g8.donations as d ON u.User_id=d.User_id JOIN web_project_g8.products as p ON p.Product_id = d.Product_id WHERE u.User_id = '%s' AND d.Ordered=0 " % (User_id)
        choices = dbManager.fetch(query)
        return choices

    def user_total_price(self, User_id):
        query = "SELECT (SUM(d.Quantity * p.Price)) as Total FROM web_project_g8.users as u JOIN web_project_g8.donations as d ON u.User_id=d.User_id JOIN web_project_g8.products as p ON p.Product_id = d.Product_id WHERE u.User_id = '%s' AND d.Ordered=0 " % (User_id)
        price = dbManager.fetch(query)
        return price[0][0]

