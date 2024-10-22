import socket
import pyautogui
import pickle
import struct
import numpy as np

# Server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
port = 9999
socket_address = (host_ip, port)

server_socket.bind(socket_address)
server_socket.listen(5)
print(f"Listening at {socket_address}")

# Accept client connection
client_socket, addr = server_socket.accept()
print(f"Got connection from {addr}")

while True:
    # Capture screen
    screenshot = pyautogui.screenshot()
    
    # Convert to numpy array (required for OpenCV)
    frame = np.array(screenshot)
    
    # Convert to bytes for streaming
    data = pickle.dumps(frame)
    message_size = struct.pack("Q", len(data))
    
    # Send frame size and frame data
    client_socket.sendall(message_size + data)

client_socket.close()
