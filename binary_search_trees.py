"""QUESTION: As a senior backend engineer, you are tasked with developing a fast in-memory data structure to manage
profile information (username, name and email) for 100 million users. It should allow the following operations to be
performed efficiently:
- Insert the profile information for a new user.
- Find the profile information of a user, given their username.
- Update the profile information of a user, given their username.
- List all the users of the platform, sorted by username.
You can assume that usernames are unique."""

from linked_list import LinkedList


class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def introduce(self, guest_name):
        print("Hi {}, I'm {}! Contact me at {}.".format(guest_name, self.name, self.email))

    def __str__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)


class UserDatabaseLinkedList:
    def __init__(self):
        self.users = LinkedList()

    def insert(self, user):
        self.users.append(user)

    def find(self, username):
        index = 0
        current = self.users.head
        while current is not None:
            if current.value.username == username:
                return index
            current = current.next
            index += 1
        return -1

    def update(self, user):
        pass

    def list_all(self):
        self.users.print_list()


# Create random users
users_list = [
    User('john_doe', 'John Doe', 'john.doe@example.com'),
    User('alice_smith', 'Alice Smith', 'alice.smith@example.com'),
    User('bob_jackson', 'Bob Jackson', 'bob.jackson@example.com'),
    User('emily_wilson', 'Emily Wilson', 'emily.wilson@example.com'),
    User('david_miller', 'David Miller', 'david.miller@example.com'),
    User('olivia_jones', 'Olivia Jones', 'olivia.jones@example.com'),
    User('michael_brown', 'Michael Brown', 'michael.brown@example.com'),
    User('sophia_clark', 'Sophia Clark', 'sophia.clark@example.com'),
    User('logan_wright', 'Logan Wright', 'logan.wright@example.com'),
    User('eva_martin', 'Eva Martin', 'eva.martin@example.com'),
    User('luke_anderson', 'Luke Anderson', 'luke.anderson@example.com'),
    User('ava_hill', 'Ava Hill', 'ava.hill@example.com'),
    User('nathan_green', 'Nathan Green', 'nathan.green@example.com'),
    User('chloe_kelly', 'Chloe Kelly', 'chloe.kelly@example.com')
]

userdblinkedlist = UserDatabaseLinkedList()  # Create new database using linkedlist
for user in users_list:  # Add users to db
    userdblinkedlist.insert(user)
userdblinkedlist.list_all()