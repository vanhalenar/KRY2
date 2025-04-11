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

raise NotImplementedError("TODO: Implement the client in this file.")
