import os
import threading
from gmpy2 import mpz, powmod
from bitcoinlib.encoding import addr_to_pubkeyhash, to_hexstring
from bitcoinlib.keys import HDKey
from ecdsa import SigningKey, SECP256k1

def save_key_to_file(private_hex: str):
    with open(f"{private_hex}.txt", "w") as f:
        f.write(private_hex)

def search_for_key(start_key_int, stop_key_int, target_address):
    for _ in range(attempts_per_thread):
        current_key_int = mpz(powmod(int.from_bytes(os.urandom(32), 'big'), 1, stop_key_int - start_key_int)) + start_key_int
        ecdsa_private_key = SigningKey.from_secret_exponent(int(current_key_int), curve=SECP256k1)
        key = HDKey(key=ecdsa_private_key.to_string())

        #print(f"Testing private key: {key.private_hex}")

        if key.address() == target_address:
            save_key_to_file(key.private_hex)
            print(f"Private key found: {key.private_hex}")
            return key
    return None

address = '1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF'

start_key = '0000000000000000000000000000000000000000000000040000000000000000'
stop_key = '000000000000000000000000000000000000000000000007ffffffffffffffff'
start_key_int = mpz(start_key, 16)
stop_key_int = mpz(stop_key, 16)

attempts_per_thread = 16000000

threads = []
for _ in range(8):
    thread_start_key_int = mpz(powmod(int.from_bytes(os.urandom(32), 'big'), 1, stop_key_int - start_key_int)) + start_key_int
    thread_stop_key_int = (thread_start_key_int + attempts_per_thread) % stop_key_int
    thread = threading.Thread(target=search_for_key, args=(thread_start_key_int, thread_stop_key_int, address))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Private key not found in the given range after {8 * attempts_per_thread} attempts.")
