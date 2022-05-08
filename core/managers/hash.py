import bcrypt


class Hash:
    def crypt(self, password, complexity=12):
        """
        # Hash password
        `password: str` - Password needs to be hashed
        returns (hashed password)
        """

        salt = bcrypt.gensalt(rounds=complexity)
        hashed_password = bcrypt.hashpw(password.encode('ascii'), salt)
        return hashed_password

    def check(self, password, hash):
        """
        # Checks password
        args:
            - `hashed_password: str` - Hashed password
            - `password: str` - Password which needs to be compared
        returns (boolean)
        """

        result = bcrypt.checkpw(password.encode('ascii'), hash)
        return result

