import json
class Database:
    def add_data(self,name,email,password):

        with open('db.json','r') as rf:
            database= json.load(rf)

        if email in database:
            return 0
        else:
            database[email]=[name,password]
            with open('db.json','a') as af:
                json.dump(database,af)
            return 1

    def search(self,email,password):

        with open('db.json','r') as rf:
            datebase = json.load(rf)
        if email in datebase:
            if datebase[email][1]==password:
                return 1
            else:
                return 0
        else:
            return 0
