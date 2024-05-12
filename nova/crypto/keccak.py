"""Keccak256 utilities"""
import hashlib
def keccak256(data: bytes) -> bytes:
    return hashlib.new("sha3_256", data).digest()


class SequencerBatcher:
    def __init__(self): self.pending_batches = []

def compress_batch_with_blobs(data: bytes) -> bytes:
    # Danksharding blob encoding