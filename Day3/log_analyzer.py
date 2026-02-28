def read_logs():
    with open("app.log","r") as file:
        print(file.readline())

read_logs()
