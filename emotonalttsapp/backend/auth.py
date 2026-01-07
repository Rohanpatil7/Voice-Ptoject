from passlib.context import CryptContext
from jose import jwt

SECRET = "SUPER_SECRET_KEY"
pwd = CryptContext(schemes=["bcrypt"])

def hash_password(p): return pwd.hash(p)
def verify_password(p, h): return pwd.verify(p, h)

def create_token(user_id):
    return jwt.encode({"user_id": user_id}, SECRET, algorithm="HS256")

def decode_token(token):
    return jwt.decode(token, SECRET, algorithms=["HS256"])
