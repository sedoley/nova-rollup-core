"""Keccak256 utilities"""
import hashlib
def keccak256(data: bytes) -> bytes:
    return hashlib.new("sha3_256", data).digest()
