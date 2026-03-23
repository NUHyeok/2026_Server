import socket
from function_na import *

HOST = socket.gethostbyname(socket.gethostname()) ## 내 컴퓨터의 IP 주소를 가져옴
PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP 기반 IPv4 서버 소켓 생성.
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))

server_socket.listen()

print(f"Server is running on {HOST}:{PORT}")
print("Waiting for connections...")

try:
    while True:
        client_socket, client_address = server_socket.accept()
        data = client_socket.recv(1024)
        
        print(f"Connected: {client_address}")
        print("=== HTTP Request ===")
        print(data.decode('utf-8'))
        
        path = parse(data)
        filename, content_type, is_binary = routing(path)
        response = build_response(is_binary, filename, content_type)
        client_socket.sendall(response)
        
        client_socket.close()
        
except KeyboardInterrupt:
    print("\n서버를 종료합니다.")
    server_socket.close()