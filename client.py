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
from typing import Tuple
from ec import curve_secp256r1
import random
from common import p, g, dh_hash_pub, debug_log, HOST

parser = argparse.ArgumentParser(prog="server.py", description="server for DH/ECDH key exchange")
parser.add_argument("-p", "--port", required=True)
parser.add_argument("-e", "--ec", action="store_true")
parser.add_argument("-d", "--debug", action="store_true")

args = parser.parse_args()

PORT = int(args.port)

def pub_to_str(pub: Tuple[int, int]) -> str:
    x, y = pub
    return (f"{{'x': {x}, 'y': {y}}}")

def ecdh(s: socket.socket):
    c_priv, c_pub = curve_secp256r1.generate_keys()
    pub_enc = curve_secp256r1.encode_pub(c_pub)
    s.sendall(pub_enc)
    data = s.recv(1024)
    s_pub = curve_secp256r1.decode_pub(data)
    shared = curve_secp256r1.point_mul(c_priv, s_pub)
    debug_log(curve_secp256r1.hash_pub(shared))
    with open("client.priv", "w") as f:
        f.write(str(c_priv))
    with open("client.pub", "w") as f:
        pub_dict = dict(x = c_pub[0], y = c_pub[1])
        f.write(str(pub_dict))
    with open("client.shared", "w") as f:
        f.write(curve_secp256r1.hash_pub(shared))

def dh(conn: socket.socket):
    with conn:
        c_priv = random.getrandbits(4096)
        c_pub = pow(g, c_priv, p)
        conn.sendall(c_pub.to_bytes(8192, 'big'))
        data = conn.recv(8192)
        s_pub = int.from_bytes(data, 'big')
        shared = pow(s_pub, c_priv, p)
        debug_log(args, dh_hash_pub(shared))
        with open("client.priv", "w") as f:
            f.write(str(c_priv))
        with open("client.pub", "w") as f:
            f.write(str(c_pub))
        with open("client.shared", "w") as f:
            f.write(dh_hash_pub(shared))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    if args.ec:
        ecdh(s)
    else:
        dh(s)

