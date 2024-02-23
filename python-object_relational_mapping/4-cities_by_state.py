if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )


    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to retrieve all cities
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
                    INNER JOIN states ON cities.state_id=states.id\
                    ORDER BY cities.id ASC")

    # Fetch all the rows
    cities = cursor.fetchall()

    # Display the results
    for city in cities:
        print(city)


    # Close the cursor and connection
    cursor.close()
    db.close()