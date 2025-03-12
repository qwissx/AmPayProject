from fastapi import HTTPException, status


class AuthExc:
    UserExist = HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User is already exist")
    UserDoesNotExist = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not exist")
    UserNotAuthorized = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not authorized")

    InfoExist = HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Info is already exist")

    NotValidPass = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Password is not valid")

    TokenTimeNotValid = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token time is not valid")
    TokenKeyNotValid = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token access key is not valid")
    TokenRoleNotValid = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token role is not valid")
