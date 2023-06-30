from utils.config import read_config
from model.baby_names import get_popularity_by_name
from model.connection import get_connection, get_collection

def main():
    config = read_config()
    conn = get_connection(config)
    collection = get_collection(conn, config)

    while(True):
        cmd = input('>>> ')
        if cmd == ":q":
            print("Program finished")
            conn.close()
            exit(0)
        elif cmd == ':h':
            print("Type a name after the promt (>>>)")
            print(":h Help")
            print(":q Quit")
        else:
            name = cmd
            baby_names = get_popularity_by_name(collection, name)
            for baby_name in baby_names:
                print(("Ransk: %s Year: %s") % (baby_name['rank'], baby_name['year']))

if __name__ == "__main__":
    main()
