import bcrypt


class Hash:
    def crypt(self, password, complexity=12):
        salt = bcrypt.gensalt(rounds=complexity)
        hashed_password = bcrypt.hashpw(password.encode('ascii'), salt)
        return hashed_password

    def check(self, password, hash):
        result = bcrypt.checkpw(password.encode('ascii'), hash)
        return result
pass