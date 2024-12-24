import base64
import hashlib

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def generate_hash(string: str, salt: str) -> str:
    salted = string + salt
    return hashlib.sha256(salted.encode()).hexdigest()


def generate_key_from_password(password: str, salt: str) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt.encode(),
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key


def encrypt_text(text: str, password: str, salt: str) -> str:
    key = generate_key_from_password(password, salt)
    f = Fernet(key)
    encrypted = f.encrypt(text.encode())
    return encrypted.decode()


def decrypt_text(encrypted_text: str, password: str, salt: str) -> str:
    key = generate_key_from_password(password, salt)
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_text.encode())
    return decrypted.decode()
