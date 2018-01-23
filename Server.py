import socket
import threading

class Main:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []
    def __init__(self):
        self.s.bind(("", 5050))
        self.s.listen(3)
    def handler(self, c, addr):
        while True:
            data = c.recv(1024).decode("utf-8")
            for connection in self.connections:
                connection.send(data.encode("utf-8"))
            if not data:
                print(str(addr[0]) + ":" + str(addr[1]), "Dis-connected")
                self.connections.remove(c)
                c.close()
                break

    def run(self):
        while True:
            (c, addr) = self.s.accept()
            cThread = threading.Thread(target=self.handler, args=(c, addr))
            cThread.daemon = True
            cThread.start()
            self.connections.append(c)
            print(str(addr[0]) + ":" + str(addr[1]), "Connected")
if __name__ == "__main__":
    main = Main()
    main.run()
