import socket
import threading

class Server:
    connections = []
    peers = {}
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 5051))
    s.listen(3)

    def handler(self, c, addr):
        while True:
            data = c.recv(1024).decode("utf-8")
            if data[0:4] == "USER":
                data = data.split()
                print(data[1] + " connected")
                self.peers.update({data[1]:c})

            else:
                for d in data:
                    for i in "|":
                        if d == "|":
                            split = data.split("|")
                            user = split[0]
                            data = split[1]
                            for peer in self.peers:
                                if user != peer:
                                    self.peers[peer].send((user + ": " + data).encode("utf-8"))
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

def main():
    server = Server()
    server.run()
if __name__ == "__main__":
    main()
