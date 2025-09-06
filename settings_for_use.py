# JWT签名密钥，用户自己使用secrets.token_urlsafe(32)生成
# SECRET_KEY =

# ALGORITHM = "HS256"
#
# ACCESS_TOKEN_EXPIRE_DAYS = 7

# mysql数据库相关配置，若项目简单，并发较低，非IO密集可以考虑pymysql，否则用aiomysql
# DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/your_database"
# ASYNC_DATABASE_URL = "mysql+aiomysql://root:password@localhost:3306/your_database"
