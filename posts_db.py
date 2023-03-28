from website.models.db_models import Posts, db, app
from website.constans.posts import POSTS

app.app_context().push()

for post in POSTS:
    new_post = Posts(
        data=post['data'],
        autor=post['autorius'],
        book_name=post['pavadinimas'],
        comment=post['tekstas'],
    )

    db.session.add(new_post)
    db.session.commit()
