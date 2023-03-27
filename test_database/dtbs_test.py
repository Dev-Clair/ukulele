import sqlite3

# Build a context manager for resource allocation - network connection- management


class Connection:
    def __init__(self, filename):
        self.filename = filename
        self.connection = sqlite3.connect(self.filename)

    def __enter__(self):
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_typ, exc_val, exc_tb):
        if self.cursor:
            self.connection.commit()
            self.connection.close()


def createtable():
    with Connection("tryrdb.db") as connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS surveytable (Id INTEGER PRIMARY KEY, Tag TEXT, Name TEXT, Age TEXT, Email TEXT, Gender TEXT, Ethnicity TEXT, Disability TEXT, Enjoyed TEXT, Curious TEXT, Science TEXT, Future TEXT)")


def addrecord(tag, name, age, email, gender, ethnicity, disability, enjoyed, curious, science, future):
    """
        Adds record to database
    """
    with Connection("tryrdb.db") as connection:
        connection.execute(
            "INSERT INTO surveytable VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (tag, name, age, email, gender, ethnicity, disability, enjoyed, curious, science, future))


def selectrecord(age, gender, ethnicity, disability):
    """
        Selects record(s) from database
    """
    # Variables have been assigned a default argument, if no selection is made for each argument at function call
    with Connection("tryrdb.db") as connection:
        result = connection.execute(
            "SELECT * FROM surveytable WHERE (Age=? AND Gender=? AND Ethnicity=? AND Disability=?)", (age, gender, ethnicity, disability))
        row = result.fetchall()
        print(row)


def main():
    createtable()
    while True:
        addrecord(tag=(input("Tag: \n")),
                  name=(input("Name: \n")),
                  age=(input("Age: \n")),
                  email=(input("Email: \n")),
                  gender=(input("Gender: \n")),
                  ethnicity=(input("Ethnicity: \n")),
                  disability=(input("Disability: \n")),
                  enjoyed=(input("Enjoyed: \n")),
                  curious=(input("Curious: \n")),
                  science=(input("Science: \n")),
                  future=(input("Future: \n")))
        print("\nWill you like to add another record? Yes or No")
        choice = input("\nChoice? ")
        if choice == "No":
            break
    selectrecord(age=(input("Age: \n")),
                 gender=(input("Gender: \n")),
                 ethnicity=(input("Ethnicity: \n")),
                 disability=(input("Disability: \n")))


main()
