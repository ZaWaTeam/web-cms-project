import bcrypt


class PasswordHash:
    def __init__(self, iter_count=14):
        self.iter_count = iter_count

    def create(self, password: str):
        """
        ## Hash password

        `password: str` - Password needs to be hashed

        returns (hashed password)
        """
        salt = bcrypt.gensalt(rounds=self.iter_count)
        hashed_password = bcrypt.hashpw(password.encode('ascii'), salt)

        return hashed_password

    def check_password(self, hashed_password: str, password: str):
        """
        ## Checks password

        args:
            - `hashed_password: str` - Hashed password
            - `password: str` - Password which needs to be compared

        returns (boolean)
        """
        result = bcrypt.checkpw(
            hashed_password=hashed_password, password=password)

        return bool(result)
