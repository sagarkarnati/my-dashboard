import mysql.connector
import config


class DBUtils:
    def get_connection(self):
        try:
            cnx = mysql.connector.connect(user=config.DB_USER,
                                          password=config.DB_PWD,
                                          host=config.DB_HOST,
                                          port=config.DB_PORT,
                                          database=config.DB_DATABASE)
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == mysql.connector.errorcode.ER_BAD_DV_ERROR:
                print("Database does not exist")
            else:
                print(err)

        return cnx
