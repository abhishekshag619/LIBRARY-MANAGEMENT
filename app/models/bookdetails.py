#book details model
from app.app import db
from app.models.usermodel import User

class bookDetails(db.Document):
	bookname = db.StringField(required=True)
	authorname = db.StringField(required=True)
	issueduser = db.ReferenceField(User)
	issuedon = db.StringField()
	dayofreturn = db.StringField()
	booksno = db.StringField(required=True)
