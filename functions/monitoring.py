import datetime


def TimeTagMessage(string):
    print(datetime.datetime.now().__str__() + " " + string)