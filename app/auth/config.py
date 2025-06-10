from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
SECRET_KEY = 'my_secret_key'
ALGORITHM = 'HS256'