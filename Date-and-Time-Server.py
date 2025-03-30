# -*- coding: utf-8 -*-
"""
Created on Sun March  20 08:345:47 2025

@author: IAN CARTER KULANI

"""

from colorama import Fore
import pyfiglet
import os
font=pyfiglet.figlet_format("Date and Time Server")
print(Fore.GREEN+font)

import socket
import datetime

def start_server():
    # Prompt for the host and port information
    host = input("Enter the server's host:")
    port = int(input("Enter the port number:"))
    
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the address and port
    server_socket.bind((host, port))
    server_socket.listen(1)
    
    print(f"Server started on {host}:{port}, waiting for a connection...")
    
    while True:
        # Wait for a connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")
        
        # Send the current date and time
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        client_socket.send(current_time.encode())
        
        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    start_server()
