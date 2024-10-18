from sqlalchemy import create_engine

# 1111 это мой пароль для пользователя postgres
engine = create_engine("postgresql+psycopg2://pg:qwerty@localhost/social_net")
engine.connect()

print(engine)
