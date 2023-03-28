#
#
# def get_db():
#     if 'db' not in g:
#         g.db = sqlite3.connect('data.sqlite')
#         g.db.row_factory = sqlite3.Row
#     return g.db
#
#
#


# import sqlite3
#
#
# def get_posts():
#     conn = sqlite3.connect('sqlite:////Users/arturkryzanovskij/PycharmProjects/newflask/website/models/data.sqlite')
#     c = conn.cursor()
#     c.execute("SELECT * FROM Posts")
#     posts = [{"pavadinimas": row[0], "autorius": row[1], "data": row[2], "tekstas": row[3]} for row in c.fetchall()]
#     conn.close()
#     return posts

# POSTS =[{
#     'data':'2020 01 01',
#     'autorius': 'Autorius 1',
#     'pavadinimas': 'Apie nieką',
#     'tekstas': 'Zombie ipsum reversus ab viral inferno, nam rick grimes malum cerebro. De carne lumbering animata corpora quaeritis. Summus brains sit​​, morbo vel maleficia? De apocalypsi gorger omero undead survivor dictum mauris.'
# },
# {
#     'data':'2020 02 01',
#     'autorius': 'KITAS AUTORIUS',
#     'pavadinimas': 'Apie zombius',
#     'tekstas': 'Zombie ipsum reversus ab viral inferno, nam rick grimes malum cerebro. De carne lumbering animata corpora quaeritis. Summus brains sit​​, morbo vel maleficia? De apocalypsi gorger omero undead survivor dictum mauris. '
# },
# {
#     'data':'2020 03 01',
#     'autorius': 'Dar kažkas',
#     'pavadinimas': 'Braiiins!',
#     'tekstas': 'Zombie ipsum reversus ab viral inferno, nam rick grimes malum cerebro. De carne lumbering animata corpora quaeritis. Summus brains sit​​, morbo vel maleficia? De apocalypsi gorger omero undead survivor dictum mauris.Zombie ipsum reversus ab viral inferno, nam rick grimes malum cerebro. De carne lumbering animata corpora quaeritis. Summus brains sit​​, morbo vel maleficia? De apocalypsi gorger omero undead survivor dictum mauris.'
# }]

