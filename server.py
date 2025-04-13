#!/usr/bin/env python3
"""
Implementation of a simple server for the key-exchange.

Supports both Elliptic Curve (ECDH) and Ordinary Diffie-Hellman (DH).
The server should wait for client connection, perform the key-exchange, close the connection and exit.

The server writes the used keys to specific files:
- private key to "server.priv"
- public key to "server.pub"
- shared key (the SHA-256 hash) to "server.shared"

The shared key is the *SHA-256 hash of the shared value*:
- In case of ECDH: Hash of the x-coordinate (first coord.) of the shared point
- In case of DH: Hash of the hexadecimal notation (without the '0x' prefix!) of shared value

The server accepts the following command-line arguments:
- --ec: Use Elliptic Curve Diffie-Hellman (ECDH) instead of Ordinary Diffie-Hellman (DH).
- --port: The port to listen on.

Example:
$ python3 server.py --ec --port 12345

The server should *not* output anything to the standard output, only to the aforementioned files.
"""

import socket
import argparse
from ec import curve_secp256r1
from common import p, g, dh_hash_pub, debug_log, HOST, dh_gen_priv

parser = argparse.ArgumentParser(prog="server.py", description="server for DH/ECDH key exchange")
parser.add_argument("-p", "--port", required=True)
parser.add_argument("-e", "--ec", action="store_true")
parser.add_argument("-d", "--debug", action="store_true")

args = parser.parse_args()

PORT = int(args.port)

def ecdh(conn: socket.socket):
    with conn:
        s_priv, s_pub = curve_secp256r1.generate_keys()
        data = conn.recv(1024)
        c_pub = curve_secp256r1.decode_pub(data)
        pub_enc = curve_secp256r1.encode_pub(s_pub)
        conn.sendall(pub_enc)
        shared = curve_secp256r1.point_mul(s_priv, c_pub)
        debug_log(args, curve_secp256r1.hash_pub(shared))
        with open("server.priv", "w") as f:
            f.write(str(s_priv))
        with open("server.pub", "w") as f:
            pub_dict = dict(x = s_pub[0], y = s_pub[1])
            f.write(str(pub_dict))
        with open("server.shared", "w") as f:
            f.write(curve_secp256r1.hash_pub(shared))

def dh(conn: socket.socket):
    with conn:
        s_priv = dh_gen_priv() #random.getrandbits(4096)
        s_pub = pow(g, s_priv, p)
        data = conn.recv(8192)
        conn.sendall(s_pub.to_bytes(8192, "big"))
        c_pub = int.from_bytes(data, "big")
        shared = pow(c_pub, s_priv, p)
        debug_log(args, dh_hash_pub(shared))
        with open("server.priv", "w") as f:
            f.write(str(s_priv))
        with open("server.pub", "w") as f:
            f.write(str(s_pub))
        with open("server.shared", "w") as f:
            f.write(dh_hash_pub(shared))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    if args.ec:
        ecdh(conn)
    else:
        dh(conn)
            