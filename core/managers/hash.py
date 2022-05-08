import bcrypt


class Hash:
    def crypt(self, password: str, complexity: int = 12):
        """
        # Hash password
        `password: str` - Password needs to be hashed
        `complexity: int` - Password rounds
        returns (hashed password)
        """

        salt = bcrypt.gensalt(rounds=complexity)
        hashed_password = bcrypt.hashpw(password.encode('ascii'), salt)
        return hashed_password

    def check(self, password: str, hash: str):
        """
        # Checks password
        args:
            - `password: str` - Password which needs to be compared
            - `hash: str` - Hashed passwords
        returns (boolean)
        """

        result = bcrypt.checkpw(password.encode('ascii'), hash)
        return result
