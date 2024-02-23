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

    # Execute the SQL query to retrieve all cities by state
    cursor.execute("SELECT cities.name FROM cities\
                    INNER JOIN states ON cities.state_id=states.id\
                    WHERE states.name=%s\
                    ORDER BY cities.id ASC", (argv[4],))

    # Fetch all the rows counting from 0
    cities_state = cursor.fetchall()
    first = 0

    # Display the results
    for city in cities_state:
        
        if first != 0:
            print(", ", end="")
        print("%s" % city, end="")
        first += 1
    
    print("")


    # Close the cursor and connection
    cursor.close()
    db.close()