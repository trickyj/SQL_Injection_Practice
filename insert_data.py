import sqlite3
connection = sqlite3.connect('sample.db')
cursor = connection.cursor()
insert_data_sql = '''
INSERT INTO users (ID, username, password, Date, Ranking, Pincode)
VALUES
    (1, 'admin', 'password123', '2024-01-01', 1, '123456'),
    (2, 'user1', 'password456', '2024-02-15', 2, '234567'),
    (3, 'user2', 'password789', '2024-03-10', 3, '345678'),
    (4, 'user3', 'password321', '2024-04-20', 4, '456789'),
    (5, 'user4', 'password654', '2024-05-25', 5, '567890'),
    (6, 'user5', 'password987', '2024-06-30', 6, '678901'),
    (7, 'user6', 'password654', '2024-07-15', 7, '789012'),
    (8, 'user7', 'password321', '2024-08-22', 8, '890123'),
    (9, 'user8', 'password789', '2024-09-10', 9, '901234'),
    (10, 'user9', 'password123', '2024-10-05', 10, '012345');
'''

# Execute the SQL statement to insert data
cursor.execute(insert_data_sql)

# Commit the transaction to save changes
connection.commit()

# Close the connection
connection.close()
