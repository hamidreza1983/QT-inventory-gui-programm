from mysql import connector


class Database:
    def __init__(self,username=None,password=None,host=None):
        self.username = username
        self.password = password
        self.host = host

    def connect(self):
        try:
            self.connection = connector.connect(
                username=self.username, 
                password=self.password, 
                host=self.host, 
                )
            self.connection.close()
            return True
        except:
            return False    

class DatabaseUserManager:
    def __init__(self,username=None,password=None,host=None,newuser=None,newpassword=None,newhost=None):
        self.username = username
        self.password = password
        self.host = host
        self.newuser = newuser
        self.newpassword = newpassword
        self.newhost = newhost

    def create_admin_user(self):
        try:
            self.connection = connector.connect(
                username=self.username, 
                password=self.password, 
                host=self.host, 
                )
            self.cur = self.connection.cursor()
            self.cur.execute("CREATE USER '%s'@'%s' IDENTIFIED BY '%s';" % (self.newuser,self.newhost,self.newpassword))
            self.cur.execute(
                        "GRANT ALL PRIVILEGES ON *.* TO '%s'@'%s' WITH GRANT OPTION;"%(self.newuser,self.newhost)
                        )
            self.cur.execute(
                        "FLUSH PRIVILEGES;"
                        )
            self.connection.commit()
            self.connection.close()
            return True
        
        except:
            return False

    def create_inventor_user(self):
        try:
            self.connection = connector.connect(
                username=self.username, 
                password=self.password, 
                host=self.host, 
                )
            self.cur = self.connection.cursor()
            self.cur.execute(
                "CREATE USER '%s'@'%s' IDENTIFIED BY '%s';" % (self.newuser,self.newhost,self.newpassword)
                )
            self.cur.execute(
                "GRANT INSERT,UPDATE,SELECT,DELETE ON *.* TO '%s'@'%s' WITH GRANT OPTION;"%(self.newuser,self.newhost)
                )
            self.cur.execute(
                "FLUSH PRIVILEGES;"
                )
            self.connection.commit()
            self.connection.close()
            return True
        except:
            return False
    
    def create_seller_user(self):
        try:
            self.connection = connector.connect(
                username=self.username, 
                password=self.password, 
                host=self.host, 
                )
            self.cur = self.connection.cursor()
            self.cur.execute(
                "CREATE USER '%s'@'%s' IDENTIFIED BY '%s';" % (self.newuser,self.newhost,self.newpassword)
                )
            self.cur.execute(
                "GRANT UPDATE ON *.* TO '%s'@'%s' WITH GRANT OPTION;"%(self.newuser,self.newhost)
                )
            self.cur.execute(
                "FLUSH PRIVILEGES;"
                )
            self.connection.commit()
            self.connection.close()
            return True
        except:
            return False
    
    def delete_user(self):
        try:
            self.connection = connector.connect(
                username=self.username, 
                password=self.password, 
                host=self.host, 
                )
            self.cur = self.connection.cursor()
            self.cur.execute(
                "DROP USER '%s'@'%s';"%(self.newuser,self.newhost)
                )
            self.cur.execute(
                "FLUSH PRIVILEGES;"
                )
            self.connection.commit()
            self.connection.close()
            return True
        except:
            return False



