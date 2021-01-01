from server import P2P

port = 8000
address = "172.105.95.99"

if __name__ == "__main__":
    P2P(_port=port).create_session(_address=address)
