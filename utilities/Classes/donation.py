from utilities.db.db_manager import dbManager

class donation:
    __product_id = None
    __user_id = None
    __Quantity = None
    __Ordered= None

    def __init__(self, Product_id, User_id, Quantity, Ordered):
        self.__product_id = Product_id
        self.__user_id = User_id
        self.__Quantity = Quantity
        self.__Quantity = Ordered

    def insert_to_donations(self, product_id, user_id, quantity, ordered):
        query = "INSERT INTO web_project_g8.donations (Product_id, User_id, Quantity, Ordered) VALUES ('%s','%s','%s','%s')" % (product_id, user_id, quantity, ordered)
        dbManager.commit(query)

    def delete_choices(self, user_id):
        query = " DELETE FROM web_project_g8.donations WHERE ordered=0 AND User_id= ('%s');" %(user_id)
        dbManager.commit(query)

    def open_donations(self,user_id):
        query = "SELECT * FROM web_project_g8.donations WHERE Ordered=0 AND User_id=%s;" %(user_id)
        answer = dbManager.fetch(query)
        if answer:
            return True
        else:
            return False

    def donations_history(self, user_id):
        query = "SELECT * FROM web_project_g8.donations WHERE Ordered=1 AND User_id=%s;" % (user_id)
        answer = dbManager.fetch(query)
        if answer:
            return True
        else:
            return False

    def user_total_donation(self, user_id):
        query = "SELECT (SUM(d.Quantity * p.Price)) as Total FROM web_project_g8.users as u JOIN web_project_g8.donations as d ON u.User_id=d.User_id JOIN web_project_g8.products as p ON p.Product_id = d.Product_id WHERE u.User_id = '%s' AND d.Ordered=1 " % (
            user_id)
        totalDonation = dbManager.fetch(query)
        return totalDonation[0][0]

    def open_donations_by_product(self, user_id, product_id):
        query = "SELECT * FROM web_project_g8.donations WHERE Ordered=0 AND User_id='%s' AND Product_id ='%s';" % (user_id, product_id)
        answer = dbManager.fetch(query)
        if answer:
            return True
        else:
            return False

    def get_quntity(self, user_id, product_id):
        query = "SELECT Quantity FROM web_project_g8.donations WHERE Ordered=0 AND User_id='%s' AND Product_id ='%s';" %(user_id, product_id)
        quantity = dbManager.fetch(query)
        return quantity[0][0]

    def update_product_quantity(self, user_id, product_id, quantity):
        query = "UPDATE web_project_g8.donations SET Quantity='%s' WHERE Ordered=0 AND User_id= '%s' AND Product_id ='%s';" % (quantity, user_id, product_id)
        dbManager.commit(query)