# from pydantic import BaseSettings

from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_HOSTNAME: str
    DB_PORT: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_USERNAME: str
    SECRETE_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"

settings = Settings()

# Retrieve the value of DB_PORT from the settings object
db_port = settings.DB_PORT

# Use the actual value of DB_PORT in the SQLAlchemy URL configuration



# class Settings(BaseSettings):
#     DB_HOSTNAME: str
#     DB_PORT: str  # Fix the variable definition by using a colon
#     DB_PASSWORD: str
#     DB_NAME: str
#     DB_USERNAME: str
#     SECRETE_KEY: str
#     ALGORITHM: str
#     ACCESS_TOKEN_EXPIRE_MINUTES: int

#     class Config:
#         env_file = ".env"

# settings = Settings()
