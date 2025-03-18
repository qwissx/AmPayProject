from fastapi import HTTPException, status


class SQLAlchExc:
    PaymentDoesNotExist = HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Payment already was deleted")


class AuthExc:
    UserExist = HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User is already exist")
    UserDoesNotExist = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not exist")
    UserNotAuthorized = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not authorized")

    InfoExist = HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Info is already exist")

    NotValidPass = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Password is not valid")

    TokenTimeNotValid = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token time is not valid")
    TokenRoleNotValid = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token role is not valid")
    TokenIdNotValid = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token users id is not valid")

    HaveNoRights = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You dont have rights on this action")


class RZExc:
    BadPartnerResponse = HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Partner cannot perform this procedure")
