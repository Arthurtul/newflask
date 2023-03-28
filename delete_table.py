from website.models.db_models import db, app
from sqlalchemy import text

app.app_context().push()

with app.app_context():
    db.session.execute(text('DROP TABLE IF EXISTS Posts'))
    db.session.commit()

