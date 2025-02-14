import pymysql.cursors

# Replace with your MySQL server details
config = {
    'user': 'root',
    'password': 'Pak@123',
    'host': '127.0.0.1',
    'database': 'ASM',
    'cursorclass': pymysql.cursors.DictCursor
}

# Connect to MySQL server
try:
    connection = pymysql.connect(host=config['host'],
                                 user=config['user'],
                                 password=config['password'],
                                 cursorclass=config['cursorclass'])

    with connection:
        with connection.cursor() as cursor:
            # Create database if it doesn't exist
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {config['database']}")
            print(f"Database {config['database']} created or already exists.")

        # Connect to the newly created database
        connection.select_db(config['database'])

        with connection.cursor() as cursor:
            # Create a new table if it doesn't exist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255),
                    emp_id VARCHAR(255),
                    password VARCHAR(255) NOT NULL,
                    branch VARCHAR(255),
                    department VARCHAR(255),
                    can_login BOOLEAN
                )
            """)
            print("Table 'users' created or already exists.")

        # Commit the changes
        connection.commit()

except pymysql.MySQLError as err:
    print(f"Error: {err}")
    exit(1)