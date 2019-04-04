import pymysql

def check_user(username,password):
    sql = "SELECT id, username, password, name, surname FROM " \
          "users WHERE username = %s and password = %s"
    conn = pymysql.connect(user = 'root', password = 'root',
                           database = 'user_exams', host = 'localhost')
    cursor = conn.cursor()
    cursor.execute(sql, (username,password,))
    result = cursor.fetchone()
    conn.close()
    return result

def get_all_exams(user_id):
    sql = "SELECT course,grade FROM exams WHERE user_id = %s"
    conn = pymysql.connect(user='root', password='root',
                           database='user_exams', host='localhost')
    cursor = conn.cursor()
    cursor.execute(sql, (user_id,))
    results = cursor.fetchall()
    conn.close()
    return results

if __name__ == '__main__':
    print(check_user("fneaiiegoea","gmeapgnea"))
    print(check_user("alberto.mr", "1234"))
    print(get_all_exams(1))