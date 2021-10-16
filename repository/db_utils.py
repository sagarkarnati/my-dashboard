import mysql.connector


class DBUtils:
    def get_connection(self):
        try:
            cnx = mysql.connector.connect(user='root',
                                          password='rdskpS4ZEQxeHVdZ',
                                          host='34.73.60.55',
                                          port=3306,
                                          database='FINANCE')
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == mysql.connector.errorcode.ER_BAD_DV_ERROR:
                print("Database does not exist")
            else:
                print(err)

        return cnx
