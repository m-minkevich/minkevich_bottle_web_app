import sqlite3
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
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
    conn = sqlite3.connect('projects.db')
    c = conn.cursor()

    if request.GET.save:
        first_name = request.GET.first_name.strip()
        last_name = request.GET.last_name.strip()
        birth = request.GET.birth.strip()

        c.execute("INSERT INTO students (first_name, last_name, birth) VALUES (?,?,?)", (first_name,last_name,birth))
        conn.commit()

    results = fetch_all('students')
    return template('home.tpl', rows=results)

@route('/new-student')
def new_student():
    return template('new_student.tpl')

@route('/delete-student-<no:int>')
def delete_student(no:int):
    if request.GET.delete:
        delete('students',no)
        return index()

@route('/teachers')
def show_teachers():
    if request.GET.save:
        conn = sqlite3.connect('projects.db')
        c = conn.cursor()
        first_name = request.GET.first_name.strip()
        last_name = request.GET.last_name.strip()

        c.execute("INSERT INTO teachers (first_name,last_name) VALUES (?,?)", (first_name, last_name))
        conn.commit()
    
    results = fetch_all('teachers')
    return template('teachers.tpl', rows=results)

@route('/new-teacher')
def new_student():
    return template('new_teacher.tpl')

@route('/delete-teacher-<no:int>')
def delete_teacher(no:int):
    if request.GET.delete:
        delete('teachers',no)
        return show_teachers()

@route('/<no:int>', method="GET")
def student_overview(no:int):

    connection = sqlite3.connect('projects.db')
    c = connection.cursor()

    c.execute("SELECT first_name, last_name FROM students WHERE id LIKE ?", str(no))
    result = c.fetchall()

    c.execute("SELECT id, first_name, last_name, number_of_hours FROM teachers LEFT JOIN lessons ON teachers.id = lessons.teacher_id AND lessons.student_id LIKE ?", str(no))
    teachers = c.fetchall()

    c.close()
    return template('student_order.tpl', result=result, no=no, rows=teachers, student_id=no)

@route('/save-lesson-for-<t:int>-<st:int>', method="GET")
def save_lesson(t:int,st:int):
    if request.GET.save:
        conn = sqlite3.connect('projects.db')
        c = conn.cursor()

        number_of_hours = request.GET.hours.strip()

        for row in c.execute("SELECT number_of_hours FROM lessons WHERE teacher_id=? AND student_id=?", (t,st)):
            c.execute("UPDATE lessons SET number_of_hours=? WHERE teacher_id=? AND student_id=?", (number_of_hours,t,st))
            break
        else:
            c.execute("INSERT INTO lessons (student_id,teacher_id,number_of_hours) VALUES (?,?,?)", (st,t,number_of_hours))
            
        conn.commit()
        c.close()
        return student_overview(st)

@route('/workload.png')
def workload_png():
    fig = create_barchart()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    output.getvalue()
    return template('workload.tpl', mimetype='image/png')

def create_barchart():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]
    axis.plot(xs, ys)
    return fig

run(host='localhost', port=8080, debug=True)