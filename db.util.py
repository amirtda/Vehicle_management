import pyodbc

class DBConnection:
    @staticmethod
    def get_connection_string():
        driver_name = "ODBC Driver 17 for SQL Server"
        server = r".\SQLEXPRESS"  # Local instance
        database = "test"         # Your current database
        conn_str = f"DRIVER={{{driver_name}}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"
        return conn_str

    @staticmethod
    def get_connection():
        try:
            conn_str = DBConnection.get_connection_string()
            connection = pyodbc.connect(conn_str)
            return connection
        except pyodbc.Error as e:
            print("Database connection failed:", e)
            return None

    @staticmethod
    def get_cursor():
        connection = DBConnection.get_connection()
        if connection:
            return connection.cursor()
        else:
            raise ConnectionError("Failed to obtain database connection.")
