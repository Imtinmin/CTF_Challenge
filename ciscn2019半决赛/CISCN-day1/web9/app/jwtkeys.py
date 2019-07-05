import jwt
import sqlite3
import random
import string


def username_to_cookie(username):
	key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(64))
	conn.execute("INSERT INTO jwtkeys(jwtkey) VALUES('{}');".format(key))
	kid = str(conn.execute("select kid from jwtkeys where jwtkey='{}'".format(key)).fetchone()[0])

	return jwt.encode(
		headers={
			"alg": "HS256",
			"typ": "JWT",
			"kid": kid
		},
		key=key,
		payload={
			"username": username
		},
		algorithm='HS256'
	)


def cookie_to_username(cookie):
	try:
		header = jwt.get_unverified_header(cookie)
		kid = header['kid']
		key = conn.execute("select jwtkey from jwtkeys where kid={}".format(kid)).fetchall()[0][0]
		print(key)
		username = jwt.decode(cookie, key=key)['username']
	except Exception:
		username = ''
	return username


conn = sqlite3.connect('jwtweb.db', check_same_thread=False)
