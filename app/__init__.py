#routers
from app.app import app, login_manager
from app.models.usermodel import User
from app.views.userregistration import userregister,userlogin,logout
from app.views.bookfunc import tasktem,allbooks,searchbook,addbook,updatebook,deletebook,borrow,userbooks
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user):
    """current user details"""
    return User.objects.get(id=user)
#for login
app.add_url_rule("/", view_func=userlogin, methods=["GET","POST"])
#for task menu
app.add_url_rule("/task", view_func=tasktem, methods=["GET","POST"])
#for user register
app.add_url_rule("/register",view_func=userregister,methods=["GET","POST"])
#logout
app.add_url_rule("/logout",view_func=logout,methods=["GET","POST"])
#for borrowing
app.add_url_rule("/borrow",view_func=borrow,methods=["GET","POST"])
#display all books
app.add_url_rule("/allbooks",view_func=allbooks,methods=["GET","POST"])
#display all books borrowed by user
app.add_url_rule("/userbooks",view_func=userbooks,methods=["GET","POST"])
#search whether particular book is available in library
app.add_url_rule("/search",view_func=searchbook,methods=["GET","POST"])
#add new book
app.add_url_rule("/add",view_func=addbook,methods=["GET","POST"])
#update details 
app.add_url_rule("/update",view_func=updatebook,methods=["GET","POST"])
#delete details 
app.add_url_rule("/delete",view_func=deletebook,methods=["GET","POST"])