import pymongo
import datetime
from bottle import route, template, request, get, post, redirect, run
from bson.objectid import ObjectId
from pymongo import MongoClient


@route('/')
def rootDirectory():
    return template('menu')


@route('/list/')
@route('/list')
def listAllPosts():
    # Get data from MongoDB
    myData = []
    client = MongoClient('localhost', 27017)
    db = client.LXF
    cursor = db.blogposts.find()

    for myDoc in cursor:
        myData.append(myDoc)
    return template('listPosts', data=myData)


@get('/write/')
@get('/write')
def writeNewPost():
    return template('write', dict(subject="", body="", tags=""))


@post('/presentnewpost/')
@post('/presentnewpost')
def presentNewPost():
    # Extract the data from write.tpl FROM
    title = request.forms.get("subject")
    post = request.forms.get("body")

    if title == "":
        title = "There is no Title!"
    if post == "":
        post = "This is the text of the post."
    postDocument = {"title": title,
                    "text": post,
                    "date": datetime.datetime.utcnow()}

    client = MongoClient('localhost', 27017)
    db = client.LXF

    # Write them to the database
    db.blogposts.insert_one(postDocument)
    # Get the postID which is the _id field of the document
    postid = str(postDocument['_id'])

    # print(postid)
    # Present the document
    redirect('/post/' + postid)


# Prints an entire post
@get("/post/<postid>")
def showPost(postid):
    client = MongoClient('localhost', 27017)
    db = client.LXF
    query = {'_id': ObjectId(postid)}
    post = db.blogposts.find_one(query)
    return template('showsinglepost', post=post)


@route('/newuser/')
@route('/newuser')
def createNewUser():
    return template('newuser')


@post('/logged/')
@post('/logged')
def listAllPosts():
    # TODO: Verifies that the data read from
    # the form are correct
    return template('logged')


@get('/login/')
@get('/login')
def listAllPosts():
    return template('login')

# Run in terminal -> $python blog.py
run(host='localhost', port=1234)
