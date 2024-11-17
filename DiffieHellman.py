# Given values for Diffie-Hellman Key Exchange
p = 47  # prime number
g = 5   # primitive root

# Private keys for Alice and Bob
a = 9   # Alice's private key
b = 12  # Bob's private key

# Calculating public keys for Alice and Bob
A = pow(g, a, p)  # Alice's public key
B = pow(g, b, p)  # Bob's public key

# Calculating the shared secret keys
shared_secret_alice = pow(B, a, p)  # Alice's shared secret key
shared_secret_bob = pow(A, b, p)    # Bob's shared secret key

# Verify that both shared secrets are the same
shared_secret_match = shared_secret_alice == shared_secret_bob

A, B, shared_secret_alice, shared_secret_bob, shared_secret_match