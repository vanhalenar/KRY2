#!/usr/bin/env python3
"""
Implementation of a simple client for the key-exchange.

Supports both Elliptic Curve (ECDH) and Ordinary Diffie-Hellman (DH).
The client should connect to the server and perform the key-exchange.

The client writes the used keys to specific files:
- private key to "client.priv"
- public key to "client.pub"
- shared key (the SHA-256 hash) to "client.shared"

The shared key is the *SHA-256 hash of the shared value*:
- In case of ECDH: Hash of the x-coordinate (first coord.) of the shared point
- In case of DH: Hash of the hexadecimal notation (without the '0x' prefix!) of shared value

The client accepts the following command-line arguments:
- --ec: Use Elliptic Curve Diffie-Hellman (ECDH) instead of Ordinary Diffie-Hellman (DH).
- --port: The port to connect to the server.

Example:
$ python3 client.py --ec --port 12345

The client should *not* output anything to the standard output, only to the aforementioned files.
"""

import socket
import argparse

parser = argparse.ArgumentParser(prog="server.py", description="server for DH/ECDH key exchange")
parser.add_argument("-p", "--port", required=True)
parser.add_argument("-e", "--ec", action="store_true")

args = parser.parse_args()

HOST = "127.0.0.1"

PORT = int(args.port)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Received {data!r}")
