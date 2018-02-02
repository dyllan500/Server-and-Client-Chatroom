import socket
import threading

class Client():
    def __init__(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("Put server ip here", 5051))
        self.user = input("Enter username: ")
        s.send("USER {}".format(self.user).encode("utf-8"))
        sthead = threading.Thread(target=self.sendm, args=(s,))
        rthread = threading.Thread(target=self.recievem, args=(s,))
        sthead.daemon = True
        sthead.start()
        rthread.start()

    def recievem(self, s):
        while True:
            data = s.recv(1024)
            if not data:
                break
            print("\n"+data.decode("utf-8"))

    def sendm(self, s):
        while True:
            s.send((self.user + "|" + input("")).encode("utf-8"))

def main():
    client = Client
    client()


if __name__ == "__main__":
    main()
