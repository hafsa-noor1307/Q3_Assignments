class Logger:
    def __init__(self):
        print("Logger Created!")

    def __del__(self):
        print("Logger Destroyed!")


logger = Logger()
