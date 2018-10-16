import bcrypt


def encrypt_password(password: str, rounds: int) -> str:
    salt = bcrypt.gensalt(rounds)
    return bcrypt.hashpw(password.encode(), salt).decode()


def is_valid_password(hashd_password, password: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashd_password.encode())
