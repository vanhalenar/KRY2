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

raise NotImplementedError("TODO: Implement the server in this file.")
