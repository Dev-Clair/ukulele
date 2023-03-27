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

    def __exit__(self, exc_typ, exc_val, exc_tb):
        if self.cursor:
            self.connection.commit()
            self.connection.close()


# Define Query Variables
# Create Table
create_table = "CREATE TABLE IF NOT EXISTS surveytable (Tag INTEGER PRIMARY KEY NOT NULL, Name TEXT NOT NULL, Age TEXT NOT NULL, Email TEXT, Gender TEXT NOT NULL, Ethnicity TEXT NOT NULL, Disability TEXT NOT NULL, Enjoyed TEXT, Curious TEXT, Science TEXT, Future TEXT)"
# Add Record
insert_data = "INSERT INTO surveytable VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
# Display Records
display_data = "SELECT * FROM surveytable"
# Select Record
select_data = "SELECT * FROM surveytable WHERE (Age=?) AND (Gender=?) AND (Ethnicity=?) AND (DISABILITY=?)"


def createtable():
    """
        Creates table in database
    """
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


def displayrecord():
    """
        displays all record(s) in database
    """
    with Connection('surveydb.db') as connection:
        rows = connection.execute(display_data)
        records = rows.fetchall()
        return records


def selectrecord(age, gender, ethnicity, disability):
    """
        Selects record(s) from database
    """
    # Variables have been assigned a default argument, if no selection is made for any argument at function call
    with Connection('surveydb.db') as connection:
        rows = connection.execute(
            select_data, (age, gender, ethnicity, disability))
        records = rows.fetchall()
        return records


if __name__ == "__main__":
    createtable()
    displayrecord()
