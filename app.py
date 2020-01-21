import sqlite3
from bottle import route, run, debug, template, request

def fetch_all(table):
    conn = sqlite3.connect('projects.db')
    c = conn.cursor()

    action = 'SELECT * FROM ' + table

    c.execute(action)
    result = c.fetchall()
    c.close()

    return result

def delete(table,id):

    conn = sqlite3.connect('projects.db')

    action = 'DELETE FROM ' + table + ' WHERE id=?'
    c = conn.cursor()
    c.execute(action, (str(id),))
    conn.commit()

@route('/')
def index():
    if request.GET.save:

        conn = sqlite3.connect('projects.db')

        first_name = request.GET.first_name.strip()
        last_name = request.GET.last_name.strip()
        birth = request.GET.birth.strip()

        c = conn.cursor()

        c.execute("INSERT INTO students (first_name, last_name, birth) VALUES (?,?,?)", (first_name,last_name,birth))
        # new_id = c.lastrowid

        conn.commit()

    conn = sqlite3.connect('projects.db')
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    result = c.fetchall()
    c.close()

    # return template('home.tpl')
    # print(result[0])
    return template('home.tpl', rows=result)

@route('/new-student')
def new_student():
    return template('new_student.tpl')

@route('/delete-student-<no:int>')
def delete_teacher(no:int):
    if request.GET.delete:
        delete('students',no)
        return index()

@route('/teachers')
def show_teachers():

    conn = sqlite3.connect('projects.db')

    c = conn.cursor()

    if request.GET.save:

        conn = sqlite3.connect('projects.db')
        c = conn.cursor()

        first_name = request.GET.first_name.strip()
        last_name = request.GET.last_name.strip()

        c.execute("INSERT INTO teachers (first_name,last_name) VALUES (?,?)", (first_name, last_name))

        conn.commit()
    
    c.execute("SELECT * FROM teachers")
    result = c.fetchall()
    c.close() 

    return template('teachers.tpl', rows=result)

@route('/new-teacher')
def new_student():
    return template('new_teacher.tpl')

@route('/delete-teacher-<no:int>')
def delete_teacher(no:int):
    if request.GET.delete:
        delete('teachers',no)
        return show_teachers()

@route('/<no:int>', method="GET")
def project_overview(no:int):

    connection = sqlite3.connect('projects.db')
    c = connection.cursor()

    c.execute("SELECT first_name, last_name FROM students WHERE id LIKE ?", str(no))
    result = c.fetchall()

    # teachers = fetch_all('teachers')


    c.execute("SELECT tid, first_name, last_name, number_of_hours FROM teachers LEFT JOIN lessons ON teachers.tid = lessons.teacher_id AND lessons.student_id LIKE ?", str(no))
    teachers = c.fetchall()

    print(teachers)

    c.close()

    return template('student_order.tpl', result=result, no=no, rows=teachers, student_id=no)

@route('/save-lesson-for-<t:int>-<st:int>', method="GET")
def save_lesson(t:int,st:int):
    if request.GET.save:
    
        conn = sqlite3.connect('projects.db')
        c = conn.cursor()

        number_of_hours = request.GET.hours.strip()

        for row in c.execute("SELECT number_of_hours FROM lessons WHERE teacher_id=? AND student_id=?", (t,st)):
            print("FOUND!")
            c.execute("UPDATE lessons SET number_of_hours=? WHERE teacher_id=? AND student_id=?", (number_of_hours,t,st))
            break
        else:
            print("NOT FOUND!!!")
            c.execute("INSERT INTO lessons (student_id,teacher_id,number_of_hours) VALUES (?,?,?)", (st,t,number_of_hours))
            
        conn.commit()
        return project_overview(st)

run(host='localhost', port=8080, debug=True)