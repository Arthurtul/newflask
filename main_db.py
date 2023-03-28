from website.models.db_models import Message, db, app

app.app_context().push()
db.create_all()

# jonas = Message('Jonas', 'jonas@mail.com', "86449948", "Kažkoks labai rimtas atsiliepimas", "2")
antanas = Message('Antanas', 'antanas@mail.lt', "863423948", 'Antano nuomonė labai svarbi.', "one")
juozas = Message('Juozas', 'juozukas@friends.lt', "863249978", 'Aš labai piktas, nes blogai.', "twp")
bronius = Message('Bronius', 'bronka@yahoo.com', "86986574", 'Aš tai linksmas esu, man patinka.', "wr")
petras = Message('Petras', 'petro@yahoo.com', "4456656", 'Hello this is Petras', "Wrum wrum")
jonas = Message.query.filter_by(name="Jonas").first()
jonas.phone = "86449948"
# db.session.add_all([jonas, antanas, juozas, bronius, petras])
# db.session.add(bronius)
# db.session.add(jonas)
db.session.commit()

print(jonas.message)
print(antanas.message)
print(juozas.message)
print(bronius.message)
