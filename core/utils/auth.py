from typing import Dict, List, Union


def has_token(headers: Dict[str, str]) -> bool:
    """
    ## Has token

    Checking if there is token in request headers

    Args:
        headers (Dict[str, str]): _description_

    Returns:
        bool: _description_
    """
    token = headers.get("Authorization", None)

    # If there is no header called "Authorization" which is required, because it contains token that identificates user
    if not token:
        return False
    
    # If the token content starts with Bearer, because this is OAuth2 Auth type, that means token type should be bearer.
    if not token.startswith("Bearer"):
        return False
    
    return True

def get_token(headers: Dict[str, str]) -> Union[str, None]:
    """
    ## Get token

    This method parses user token and clears it from non important values, such as `Bearer` prefix

    Args:
        headers (Dict[str, str]): Authentication headers which are in `request.headers`

    Returns:
        str: Parsed & clear token, without non important values
        None: Token was not found
    """
    # If there is no Authorization token
    if not has_token(headers):
        return None
    
    token = headers["Authorization"]

    token = token.split(" ")

    return token[1]