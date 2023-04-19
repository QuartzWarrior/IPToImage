from src import loader

if __name__ == '__main__':
    serverip = input("Server IP\n-> ")
    if serverip:
        servername = input("Server Name\n-> ")
        if servername:
            loader.loadandrun(servername, serverip)
        else:
            loader.loadandrun(serverip, serverip)
    else:
        print("No Server IP found")
