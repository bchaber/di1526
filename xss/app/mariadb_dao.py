import flask
import mysql.connector as mariadb
class MariaDBDAO:
  def __init__(self, hostname):
    self.db = mariadb.connect(host=hostname,user="root",password="root")
    self.sql = self.db.cursor(buffered=True)
    self.sql.execute("USE db")

  def get_username(self, sid):
    try:
      self.sql.execute(f"SELECT username FROM session WHERE sid = '{sid}'")
      username, = self.sql.fetchone() or (None,)
      return username
    except mariadb.Error as err:
      flask.flash(f"Database error: {err}")
      return None

  def get_password(self, username):
    try:
      self.sql.execute(f"SELECT password FROM user WHERE username = '{username}'")
      password, = self.sql.fetchone() or (None,)
      return password
    except mariadb.Error as err:
      flask.flash(f"Database error: {err}")
      return None

  def set_session(self, sid, username):
    try:
      self.sql.execute(f"INSERT INTO session (sid, username) VALUES ('{sid}', '{username}')")
      self.db.commit()
    except mariadb.Error as err:
      flask.flash(f"Database error: {err}")

  def add_post(self, username, post):
    try:
      self.sql.execute(f"INSERT INTO posts (username, post) VALUES ('{username}', '{post}')")
      self.db.commit()
    except mariadb.Error as err:
      flask.flash(f"Database error: {err}")

  def get_posts(self, username):
    try:
      self.sql.execute(f"SELECT post FROM posts WHERE username = '{username}'")
      posts = self.sql.fetchmany(size=4)
      if len(posts) == 0:
        return ["(nie masz postów)"]
      return [post for post, in posts]
    except mariadb.Error as err:
      flask.flash(f"Database error: {err}")
      return []

  def get_post(self, username, index):
    try:
      self.sql.execute(f"SELECT post FROM posts WHERE username = '{username}' AND id = {index}")
      post, = self.sql.fetchone() or (None,)
      return post
    except mariadb.Error as err:
      flask.flash(f"Database error: {err}")
      return None