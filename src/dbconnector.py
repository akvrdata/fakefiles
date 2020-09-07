import pyodbc
import configparser
import os


class SQLExecutor:
    """Simple class implementing vertica database connection,execution and saving the file to an output folder"""

    def __init__(self):
        try:
            odbc_path = os.path.join(os.getcwd(), "configs", "db_configs", "odbc.ini")

            db_credentials_pth = os.path.join(
                os.getcwd(), "configs", "db_configs", "vertica_loader.ini"
            )

            # fetch vertica host names
            db_config = configparser.ConfigParser()
            db_config.read(odbc_path)
            # assign vertica variables
            self.driver = db_config.get("vertica", "Driver")
            self.server = db_config.get("vertica", "Servername")
            self.database = db_config.get("vertica", "Database")
            # fetch vertica creds
            cred_config = configparser.ConfigParser()
            cred_config.read(db_credentials_pth)
            # print(db_credentials_pth)
            # assign vertica cred variables
            self.username = cred_config.get("vertica_db", "username")
            self.password = cred_config.get("vertica_db", "password")
        except Exception as err:
            print(err)

    def get_connection(self):
        try:
            # use the variables in constructor and get connection
            conn_dsn_string = "DRIVER={};SERVER={};DATABASE={};UID={};PWD={}"
            conn_info = conn_dsn_string.format(
                self.driver, self.server, self.database, self.username, self.password
            )
            conn = pyodbc.connect(conn_info)
            # encoding for pyodbc4.x to handle unicode column with headers
            # this may vary when moving to redshift (refer pyodbc wiki)
            conn.setdecoding(pyodbc.SQL_CHAR, encoding="utf-8")
            conn.setdecoding(pyodbc.SQL_WCHAR, encoding="utf-8")
            conn.setdecoding(pyodbc.SQL_WMETADATA, encoding="utf-32le")
            conn.setencoding(encoding="utf-8")
            # end of encoding settings
            self.cur = conn.cursor()
        except Exception as err:
            print(err)
            exit()

    def run_command(self):
        try:
            self.get_connection()
            sql = "COPY backup_schema.copy_test FROM '/Users/avr/Documents/github_others/fakefiles/test_file.csv' DELIMITER ',';"
            print(self.cur.execute(sql))            
        except Exception as err:
            print(err)
            exit()


sql_obj = SQLExecutor()
sql_obj.run_command()


# print(db_credentials_pth)
