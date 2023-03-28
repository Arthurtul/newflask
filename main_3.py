from website.models.db_models import Message, db, app

app.app_context().push()

all_messages = Message.query.all()

print(all_messages)

message = db.session.get(Message, 1)
print(message)
print(message.name)
print(message.email)


antanas = db.session.get(Message, 2)
antanas.email = 'vienas5@vienas.lt'
db.session.add(antanas)
db.session.commit()
