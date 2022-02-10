from utilities.db.db_manager import dbManager

def get_events():
    query = "SELECT Event_id FROM web_project_g8.events;"
    result = dbManager.fetch(query)
    if result:
        return True
    else:
        return False

class eventPar:
    __Event_id = None
    __User_id = None
    __Create_date = None

    def __init__(self, Event_id , User_id, Create_date):
        self.__Event_id = Event_id
        self.__User_id = User_id
        self.__Create_date = Create_date

    def insert_par(self):
        query = "INSERT INTO web_project_g8.event_participants (Event_id ,User_id, Create_date) VALUES ('%s','%s', '%s');" % (self.__Event_id, self.__User_id, self.__Create_date)
        dbManager.commit(query)

    def spaceStatus(self, Event_id):
        doesntHavePars = "SELECT * from web_project_g8.event_participants";
        if doesntHavePars:  # for the case where there aren't any participants at all (event_participants is empty)
            return True
        else:
            query = "SELECT e.Event_id, count(ep.User_id) as numOfPars FROM web_project_g8.event_participants as ep join web_project_g8.events as e " \
                    "on ep.Event_id = e.Event_id where e.Event_id='%s';" %(Event_id)
            numOfPars = dbManager.fetch(query)
            return self.checkForSpace(numOfPars, Event_id)

    def checkForSpace(self, numOfPars, Event_id):
        query = "SELECT Capacity FROM web_project_g8.events where Event_id='%s'" %(Event_id)
        Capacity = dbManager.fetch(query)
        if numOfPars[0][1] < Capacity[0][0]:
            return True
        else:
            return False


    def delete_ParFromEvent(self, User_id, Event_id):
        query = "DELETE FROM web_project_g8.event_participants WHERE Event_id=('%s') AND User_id= ('%s');" % (Event_id, User_id)
        ans = dbManager.commit(query)
        print(ans)
        if ans:
            return True
        else:
            return False

    def checkEvents(self, User_id):
        query = "SELECT e.Event_id, e.Event_name  FROM web_project_g8.event_participants as ep join web_project_g8.events as e on ep.Event_id = e.Event_id WHERE ep.User_id=('%s');" % (User_id)
        return dbManager.fetch(query)
