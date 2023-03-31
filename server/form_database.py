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
create_table = "CREATE TABLE IF NOT EXISTS surveytable (Tag INTEGER PRIMARY KEY NOT NULL, Name TEXT NOT NULL, Age INT NOT NULL, Email TEXT, Gender TEXT NOT NULL, Ethnicity TEXT NOT NULL, Disability TEXT NOT NULL, Enjoyed TEXT, Curious TEXT, Science TEXT, Future TEXT)"
# Add Record
insert_data = "INSERT INTO surveytable VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
# Display Records
display_data = "SELECT * FROM surveytable"
# Select Record
select_data = "SELECT * FROM surveytable WHERE Age BETWEEN ? AND ? AND Gender=? AND Ethnicity=? AND DISABILITY=?"
# Update Record - Column Should Only be Updated as Required
update_data = "UPDATE surveytable SET Gender=? WHERE Tag=?"
# Delete Record
delete_data = "DELETE * FROM surveytable WHERE Tag=?"


def createtable():
    """
        Creates table in database
    """
    with Connection('surveydb.db') as connection:
        connection.execute(create_table)


def addrecord(tag, name, age, email, gender,
              ethnicity, disability, enjoyed, curious, science, future):
    """
        Adds record to table in database
    """
    with Connection('surveydb.db') as connection:
        connection.execute(insert_data, (tag, name, age, email, gender,
                           ethnicity, disability, enjoyed, curious, science, future))


def displayrecord():
    """
        Displays all record(s) in table
    """
    with Connection('surveydb.db') as connection:
        rows = connection.execute(display_data)
        records = rows.fetchall()
        return records


def selectrecord(lower_range_value=" ", upper_range_value=" ", gender=" ", ethnicity=" ", disability=" "):
    """
        Selects record(s) from table
    """
    with Connection('surveydb.db') as connection:
        values = (lower_range_value, upper_range_value,
                  gender, ethnicity, disability)
        rows = connection.execute(
            select_data, values)
        records = rows.fetchall()
        return records


def updaterecord(column=" ", tag=" "):
    """
        Updates student record in table
    """
    with Connection('surveydb.db') as connection:
        values = (column, tag)
        connection.execute(update_data, values)


def deleterecord(tag=" "):
    """
        Deletes selected record from database
    """
    with Connection('surveydb.db') as connection:
        connection.execute(delete_data, tag)


def total_num():
    """
        returns total number of rows/records in the table
    """
    totalno = "SELECT COUNT(*) FROM surveytable"
    with Connection('surveydb.db') as connection:
        totalval1 = connection.execute(totalno)
        totalval2 = totalval1.fetchone()
        totalcount = totalval2[0]
        return totalcount


def womenpercent():
    """
        returns percentage of 'female' women in the table
    """
    women_per = "SELECT COUNT(*) FROM surveytable WHERE Gender=?"
    with Connection('surveydb.db') as connection:
        total_women1 = connection.execute(women_per, ("Female",))
        total_women2 = total_women1.fetchone()
        total_women3 = total_women2[0]
        total_women = total_women3

    totalno = "SELECT COUNT(*) FROM surveytable"
    with Connection('surveydb.db') as connection:
        totalval1 = connection.execute(totalno)
        totalval2 = totalval1.fetchone()
        totalval3 = totalval2[0]
        totalval = totalval3

    return round((total_women/totalval)*100, 2)


def enjoytour():
    """
        returns average number of people who enjoyed the tour
    """
    aver_enj = "SELECT COUNT(*) FROM surveytable WHERE Enjoyed=?"
    with Connection('surveydb.db') as connection:
        enjoy1 = connection.execute(aver_enj, ("Yes",))
        enjoy2 = enjoy1.fetchone()
        enjoy = enjoy2[0]
        return enjoy


def curious():
    """
        returns average number of people curious about the singing sculpture
    """
    aver_cur = "SELECT COUNT(*) FROM surveytable WHERE Curious=?"
    with Connection('surveydb.db') as connection:
        curious1 = connection.execute(aver_cur, ("Yes",))
        curious2 = curious1.fetchone()
        curious = curious2[0]
        return curious


def science():
    """
        returns total number of people who will like to learn more about the science of acoustics
    """
    aver_sci = "SELECT COUNT(*) FROM surveytable WHERE Science=?"
    with Connection('surveydb.db') as connection:
        science1 = connection.execute(aver_sci, ("Yes",))
        science2 = science1.fetchone()
        science = science2[0]
        return science


def future():
    """
        returns total number of people who will like to attend future events
    """
    future_eve = "SELECT COUNT(*) FROM surveytable WHERE Future=?"
    with Connection('surveydb.db') as connection:
        future1 = connection.execute(future_eve, ("Yes",))
        future2 = future1.fetchone()
        future = future2[0]
        return future


if __name__ == "__main__":
    createtable()
    # print(total_num())
    # print(womenpercent())
    # print(enjoytour())
    # print(curious())
    # print(science())
    # print(future())
