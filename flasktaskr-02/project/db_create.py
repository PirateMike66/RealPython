# project/db_create.py

from views import db
from models import Task
from datetime import date

# create the database
db.create_all()

# insert dummy data
# db.session.add(Task("Finish this tutorial", date(2020, 6, 15), 10, 1))

# commit the changes
db.session.commit()
