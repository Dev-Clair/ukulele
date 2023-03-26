import sqlite3


class Connection:
    def __init__(self, filename: str):
        """
            Create a context manager for better resource (database connection) management
        """
        self.filename = filename
        self.connection = sqlite3.connect(self.filename)

    def __enter__(self):
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self):
        if self.cursor:
            self.connection.commit()
            self.connection.close()


# Define Query Variables
# Create Table
create_table = "CREATE TABLE IF NOT EXISTS surveytable (Id Integer PRIMARY KEY, Tag Text, Name Text, Age Text, Email Text, Gender Text, Ethnicity Text, Disability Text, Enjoyed Text, Curious Text, Science Text, Future Text)"
# Add Record
insert_data = "INSERT INTO surveytable VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
# Select Record
select_data = "SELECT * FROM surveytable WHERE (Age=? AND Gender=? AND Ethnicity=? AND DISABILITY=?)"


def createtable():
    with Connection('surveydb.db') as connection:
        connection.execute(create_table)


def addrecord(tag, name, age, email, gender,
              ethnicity, disability, enjoyed, curious, science, future):
    """
        Adds record to database
    """
    with Connection('surveydb.db') as connection:
        connection.execute(insert_data, (tag, name, age, email, gender,
                                         ethnicity, disability, enjoyed, curious, science, future))
    # Submits to Database


def selectrecord(age="*", gender="*", ethnicity="*", disability="*"):
    """
        Selects record(s) from database
    """
    # Variables have been assigned a default argument, if no selection is made for each argument at function call
    with Connection('surveydb.db') as connection:
        connection.execute(
            select_data, (age, gender, ethnicity, disability))
    # Retrieves From Database and Display on Treeview Table


if __name__ == "__main__":
    createtable()
