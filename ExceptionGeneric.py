class ExceptionGeneric(Exception):
    def __init__(self, message):
        self.message = message
        print("ERROR DETECTED . . .")
