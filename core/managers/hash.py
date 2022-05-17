import bcrypt


class Hash:
    def crypt(self, password: str, complexity: int = 12):
        """
        The crypt function takes a password and hashes it with a random salt.
        The result is stored in the database so that user can login using the same password.

        :param self: Reference the class itself
        :param password:str: Pass the password that needs to be hashed
        :param complexity:int=12: Determine the number of rounds that bcrypt will use to hash the password
        :return: The hashed password
        """

        salt = bcrypt.gensalt(rounds=complexity)
        hashed_password = bcrypt.hashpw(password.encode('ascii'), salt)
        return hashed_password

    def check(self, password: str, hash: str):
        """
        The check function checks a password against a hash.



        :param self: Reference the class instance
        :param password:str: Store the password that is entered by the user
        :param hash:str: Check if the password entered matches the hash
        :return: A boolean value, which is the result of comparing the hash of a given password with a hash that has been stored in the database
        """
        result = bcrypt.checkpw(password.encode('ascii'), hash.encode('ascii'))
        return result
