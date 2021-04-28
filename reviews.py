from db import db
import users

def get_list(film_id):
    sql = "SELECT u.username, r.content, r.grade, TO_CHAR(r.submitted, 'DD Month - HH24:MI') " \
          "FROM reviews AS r, users AS u " \
          "WHERE r.film_id=:film_id AND u.id=r.user_id"
    result = db.session.execute(sql, {"film_id":film_id})
    return result.fetchall()

def send(user_id, film_id, content, grade):
    sql = "INSERT INTO reviews (user_id, film_id, content, grade, submitted) " \
          "VALUES (:user_id, :film_id, :content, :grade, NOW())"
    db.session.execute(sql, {"user_id":user_id, "film_id":film_id, "content":content, "grade":grade})
    db.session.commit()
    return True