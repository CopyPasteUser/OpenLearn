import sqlite3



def showAll(table):
    conn = sqlite3.connect("databank.db")
    c = conn.cursor()
    
    c.execute(f"SELECT rowid, * FROM {table}")
    items = c.fetchall()
    
    conn.close()
    
    return items

def showTables():
    """
    Display all tables in the database.
    """
    conn = sqlite3.connect("databank.db")
    c = conn.cursor()

    # Execute query to get table names from sqlite_master table
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = c.fetchall()

    conn.close()

    return [table[0] for table in tables]

def showFirst(table_name, count):
    """
    Display the first x rows of a table.

    Args:
        table_name (str): Name of the table.
        count (int): Number of rows to display.
    """
    conn = sqlite3.connect("databank.db")
    c = conn.cursor()
    
    c.execute(f"SELECT * FROM {table_name} LIMIT ?", (count,))
    items = c.fetchall()
    
    conn.close()

    return items

def showLast(table_name, count):
    """
    Display the last x rows of a table in descending order.

    Args:
        table_name (str): Name of the table.
        count (int): Number of rows to display.
    """
    conn = sqlite3.connect("databank.db")
    c = conn.cursor()
    
    # Get the total number of rows in the table
    c.execute(f"SELECT COUNT(*) FROM {table_name}")
    total_rows = c.fetchone()[0]

    # Calculate the starting row number for the last x rows
    start_row = max(0, total_rows - count)

    # Fetch the last x rows in descending order
    c.execute(f"SELECT * FROM {table_name} ORDER BY rowid ASC LIMIT ?, ?", (start_row, count))
    items = c.fetchall()

    # Reverse the list to display the rows in ascending order
    items.reverse()
    
    conn.close()

    return items

def addOne(data, databasename):
    """
    Add a new record to the database.

    Args:
        data (dict): Dictionary containing column names and their corresponding values.
                     Example: {"first": "John", "second": "Doe", "last": "john@example.com"}
        databasename (str): Name of the database table.
    """
    conn = sqlite3.connect("databank.db")
    c = conn.cursor()

    # Construct the INSERT INTO SQL statement dynamically
    columns = ', '.join(data.keys())
    placeholders = ', '.join(['?' for _ in data])
    insert_sql = f"INSERT INTO {databasename} ({columns}) VALUES ({placeholders})"
    
    # Extract values from the dictionary and execute the SQL statement
    values = tuple(data.values())
    c.execute(insert_sql, values)
    
    # Commit the transaction and close the connection
    conn.commit()
    print(f"Added record to {databasename}")
    conn.close()

def deleteOne(rowid, databasename):
    """
    Delete a record from the database.

    Args:
        rowid (str): Row id of the record to delete.
                     Example: "1"
        databasename (str): Name of the database table.
    """
    conn = sqlite3.connect("databank.db")
    c = conn.cursor()

    # Construct the DELETE FROM SQL statement dynamically
    delete_sql = f"DELETE FROM {databasename} WHERE rowid = ?"

    # Execute the SQL statement with the rowid
    c.execute(delete_sql, (rowid,))
    
    # Commit the transaction and close the connection
    conn.commit()
    print(f"Deleted record with rowid {rowid} from {databasename}")
    conn.close()

def updateOne(rowid, data, databasename):
    """
    Update a record in the database.

    Args:
        rowid (str): Row id of the record to update.
                     Example: "1"
        data (dict): Dictionary containing column names and their new values.
                     Example: {"first": "Jane", "second": "Doe", "last": "jane@example.com"}
        databasename (str): Name of the database table.
    """
    conn = sqlite3.connect("databank.db")
    c = conn.cursor()

    # Construct the UPDATE SQL statement dynamically
    set_values = ', '.join([f"{key} = ?" for key in data])
    update_sql = f"UPDATE {databasename} SET {set_values} WHERE rowid = ?"
    
    # Extract values from the dictionary and execute the SQL statement
    values = tuple(data.values()) + (rowid,)
    c.execute(update_sql, values)
    
    # Commit the transaction and close the connection
    conn.commit()
    print(f"Updated record with rowid {rowid} in {databasename}")
    conn.close()


def createTable(table_name, columns):
    """
    Create a new table in the database.

    Args:
        table_name (str): Name of the table to create.
        columns (list of tuples): List of tuples containing column name and data type.
                                   Example: [("id", "INTEGER PRIMARY KEY"), ("name", "TEXT"), ("email", "TEXT UNIQUE")]
    """
    conn = sqlite3.connect("databank.db")
    c = conn.cursor()

    # Construct the CREATE TABLE SQL statement
    create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join([f'{col[0]} {col[1]}' for col in columns])})"

    # Execute the SQL statement to create the table
    c.execute(create_table_sql)

    # Commit the transaction to save the changes
    conn.commit()
    print(f"table:{table_name} has been created")
    # Close the database connection
    conn.close()

def deleteTable(table_name):
    """
    Delete a table from the database.

    Args:
        table_name (str): Name of the table to delete.
    """
    conn = sqlite3.connect("databank.db")
    c = conn.cursor()

    # Construct the DROP TABLE SQL statement
    drop_table_sql = f"DROP TABLE IF EXISTS {table_name}"

    # Execute the SQL statement to drop the table
    c.execute(drop_table_sql)

    # Commit the transaction to save the changes
    conn.commit()
    print(f"table:{table_name} has been deleted")

    # Close the database connection
    conn.close()
    
def find(value, column, table):
    """
    Find a value in a specific column of a table.

    Args:
        value: The value to search for.
        column: The name of the column to search in.
        table: The name of the table to search in.

    Returns:
        bool: True if the value is found, False otherwise.
    """
    conn = sqlite3.connect("databank.db")
    c = conn.cursor()

    # Construct the SELECT SQL statement dynamically
    select_sql = f"SELECT EXISTS(SELECT 1 FROM {table} WHERE {column} = ?)"

    # Execute the SQL statement with the value
    c.execute(select_sql, (value,))
    result = c.fetchone()[0]

    # Close the connection
    conn.close()

    # Return True if the value is found, False otherwise
    return bool(result)
   

def contains(pattern, column, table):
    """
    Search for entries in a specific column of a table that are similar to the input pattern.

    Args:
        pattern (str): The pattern to search for.
        column (str): The name of the column to search in.
        table (str): The name of the table to search in.

    Returns:
        bool: True if entries similar to the pattern are found, False otherwise.
    """
    conn = sqlite3.connect("databank.db")
    c = conn.cursor()

    # Construct the SELECT SQL statement dynamically
    select_sql = f"SELECT EXISTS(SELECT 1 FROM {table} WHERE {column} LIKE ?)"

    # Execute the SQL statement with the pattern
    c.execute(select_sql, (f'%{pattern}%',))
    result = c.fetchone()[0]

    # Close the connection
    conn.close()

    # Return True if entries similar to the pattern are found, False otherwise
    return bool(result)


def prepareNews():
    # Get the total number of articles
    items = showAll("News")
    total_articles = len(items)

    # Retrieve the last x articles
    allArticles = showLast("News", total_articles)

    articles = []  # Initialize an empty list to store articles
    for article in allArticles:
        articles.append(article)

    return articles