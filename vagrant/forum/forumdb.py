# "Database code" for the DB Forum.

import datetime
import psycopg2

POSTS = [("This is the first post.", datetime.datetime.now())]
DBNAME = "forum"
def get_posts():
    """Return all posts from the 'database', most recent first."""
    db = psycopg2.connect(database=DBNAME)
    query = "SELECT content, time FROM posts ORDER BY time DESC"
    cursor = db.cursor()
    cursor.execute(query)
    posts = cursor.fetchall()
    db.close()
    return posts

def add_post(content):
    """Add a post to the 'database' with the current timestamp."""
    db = psycopg2.connect(database=DBNAME)
    query = "INSERT INTO posts (content) VALUES (%s)"
    cursor = db.cursor()
    cursor.execute(query,(content,))
    db.commit()
    db.close()


