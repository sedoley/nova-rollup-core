"""Keccak256 utilities"""
import hashlib
def keccak256(data: bytes) -> bytes:
    return hashlib.new("sha3_256", data).digest()


# Auto-update from commit #00005
def get_base_gas_oracle_price() -> int:
    # Base-specific Gas Price Oracle