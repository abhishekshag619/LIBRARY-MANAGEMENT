from flask import jsonify,request,render_template,redirect, url_for
from datetime import date,timedelta 
from flask_login import current_user
from app.models.usermodel import User
from app.models.bookdetails import bookDetails
from bson.objectid import ObjectId

def tasktem():
    #if request.method == 'POST':
     #return render_template('task.html')
    return render_template('task.html')
      
def addbook():
    #to add books to library
    if request.method == 'POST':
        if (current_user.userrole == "admin"):
         bookname = request.form["bookname"]
         authorname = request.form["authorname"]
         booksno = request.form["booksno"]
         bookDetails.objects.create(bookname=bookname,authorname=authorname,
         booksno=booksno)
         
        return render_template("add.html")      
    return render_template('add.html')

def updatebook():
    #to update book details
    if request.method == 'POST':
       if (current_user.userrole=="admin"):
        bookid = request.form["bookid"]
        book = bookDetails.objects.get(id=bookid)
        booksno = request.form["booksno"]
        nbname = request.form["nbname"]
        nauthor = request.form["nauthor"]
        book.bookname = nbname
        book.authorname = nauthor
        book.booksno = booksno
        
        book.save() 
       return render_template("update.html")
    return render_template("update.html")

def deletebook():
   #to delete a book from library
   if request.method == 'POST':
      if (current_user.userrole=="admin"):
       bookid = request.form["bookid"]
       book = bookDetails.objects.get(id=bookid)
       book.delete()
      return render_template("delete.html")
   return render_template("delete.html")
    
def searchbook():
   #to search a book using bookname
   if request.method == 'POST':
    bookname = request.form["bookname"]
    book = bookDetails.objects(bookname=bookname).to_json()
    return render_template("search.html", book=book)
   return render_template("search.html")



def allbooks():
   #to display all the details
   if request.method == 'GET':
    books = bookDetails.objects()
    
    return render_template("allbooks.html",books=books)
   return render_template("allbooks.html")

def userbooks():
   #to display all books borrowed by the user
   if request.method == 'GET':
       if (current_user.userrole=="user"):
        b1 = bookDetails.objects(issueduser=current_user.id)
       return render_template("userbooks.html",b1=b1)
   return render_template("userbooks.html")

def borrow():
  #user can borrow books
   if request.method == 'GET':
    bk = bookDetails.objects().to_json()
    return render_template("borrow.html",bk=bk)
   if request.method == 'POST':
      if (current_user.userrole=="user"):
         bookid = request.form["bookid"]
         book = bookDetails.objects.get(id=bookid)
         issuser = current_user.id
         today = date.today().isoformat()
         
         retday = (date.today()+timedelta(days=14)).isoformat() 
         book.issueduser = issuser
         book.issuedon = today
         book.dayofreturn = retday
         book.save()
         return render_template("borrow.html")
   return render_template("borrow.html")
