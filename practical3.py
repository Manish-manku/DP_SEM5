import hashlib

def hash_password(password):
    """
    Hashes a password string using SHA-256 and returns its hexadecimal representation.
    :param password: The password string to be hashed
    :return: SHA-256 hashed hexadecimal string
    """
    # Encode the password to bytes
    password_bytes = password.encode('utf-8')
    # Create a SHA-256 hash object
    hash_object = hashlib.sha256(password_bytes)
    # Return the hexadecimal digest
    return hash_object.hexdigest()

# Example usage
if __name__ == "__main__":
    password = input("Enter the password: ")
    hashed_password = hash_password(password)
    print(f"SHA-256 Hashed Password: {hashed_password}")
