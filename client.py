import socket
import threading

class Main:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def sendm(self):
        while True:
            self.s.send(input("").encode("utf-8"))

    def __init__(self):
        self.s.connect(("104.39.229.134", 5050))
        iThead = threading.Thread(target=self.sendm)
        iThead.daemon = True
        iThead.start()
        while True:
            data = self.s.recv(1024)
            if not data:
                break
            print(data.decode("utf-8"))


if __name__ == "__main__":
    main = Main()
