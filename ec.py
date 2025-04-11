#!/usr/bin/env python3
"""Module for Elliptic Curve (EC) operations from scratch."""


from typing import Tuple, Union


class Curve:
    """
    Class representing Elliptic curves. The curves are defined by the parameters:
    - p: The prime number that defines the field.
    - a, b: The coefficients of the curve.
    - G: The base (generator) point of the curve.
    - n: The order of the curve.
    - h: The cofactor of the curve.

    The class implements the following methods:
    - point_add(p, q): Add two points on the curve.
    - point_mul(k, p): Multiply a point by a scalar.
    - generate_keys(): Generate a private key and a public key for the Elliptic Curve Diffie-Hellman (ECDH) key exchange.
    """

    def __init__(self, p, a, b, G, n, h):
        """
        Inintialize the Elliptic Curve with the given parameters.
        """
        self.p = p
        self.a = a
        self.b = b
        self.G = G
        self.n = n
        self.h = h

    def point_add(self, p, q) -> Union[None, Tuple[int, int]]:
        """
        Add two points on the curve.

        Args:
            p (tuple[int, int]): The first point.
            q (tuple[int, int]): The second point.

        Returns:
            None | tuple[int, int]: The result of the addition of the two points over the curve.
        """

        raise NotImplementedError("TODO: Implement this method")

    def point_mul(self, k, p) -> Tuple[int, int]:
        """
        Multiply a point by a scalar.

        Args:
            k (int): The scalar.
            p (tuple[int, int]): The point.

        Returns:
            tuple[int, int]: The result of the multiplication of the point by the scalar over the curve.
        """

        raise NotImplementedError("TODO: Implement this method")

    def generate_keys(self) -> Tuple[int, Tuple[int, int]]:
        """
        Generate a private key and a public key for the Elliptic Curve Diffie-Hellman (ECDH) key exchange.

        Returns:
            tuple[int, tuple[int, int]]: The private key and the public key.
        """

        raise NotImplementedError("TODO: Implement this method")

    def __repr__(self):
        """
        Return the string representation of the Elliptic Curve.
        """
        return f"""Elliptic Curve(
    p={self.p}
    a={self.a}
    b={self.b}
    G={self.G}
    n={self.n}
    h={self.h}
)"""


curve_secp256r1 = Curve(
    p=0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff,
    a=0xffffffff00000001000000000000000000000000fffffffffffffffffffffffc,
    b=0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b,
    G=(
        0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296,
        0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5,
    ),
    n=0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551,
    h=0x01,
)
