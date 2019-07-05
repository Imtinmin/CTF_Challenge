from hashlib import sha256
import re
import jwtkeys


def is_username_legal(string: str):
	return re.fullmatch(r'[0-9A-Za-z_]{6,}', string) is not None


def is_password_legal(string: str):
	return re.fullmatch(r'[0-9A-Za-z_]{6,}', string) is not None


def hash_password(plaintext: str):
	return sha256(plaintext.encode('utf-8')).hexdigest()


def username_to_cookie(username):
	return jwtkeys.username_to_cookie(username)


def cookie_to_username(cookie):
	return jwtkeys.cookie_to_username(cookie)
