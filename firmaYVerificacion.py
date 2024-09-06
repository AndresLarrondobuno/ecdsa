from ecpoint import ECPOINT

hash_bytearray = ECPOINT.generate_hash("abc")
hash_int = int.from_bytes(hash_bytearray, 'big')

print(hash_int)