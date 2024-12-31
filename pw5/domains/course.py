class course:
    def __init__(self, id, name, credits):
        self.id = id
        self.name = name
        self.credits = credits

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Credits: {self.credits}"
