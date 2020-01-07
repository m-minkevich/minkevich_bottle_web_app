import sqlite3
from bottle import route, run, debug, template, request



@route('/')
def index():

    conn = sqlite3.connect('projects.db')
    c = conn.cursor()
    c.execute("SELECT * FROM projects")
    result = c.fetchall()
    c.close()

    # return template('home.tpl')
    print(result[0][1])
    return template('home.tpl', rows=result)

@route('/new-project')
def new_project():
    if request.GET.save:

        name = request.GET.name.strip()
        author = request.GET.author.strip()

        conn = sqlite3.connect('projects.db')
        c = conn.cursor()

        c.execute("INSERT INTO projects (name, author) VALUES (?,?)", (name,author))
        new_id = c.lastrowid

        conn.commit()
        c.close()

        return '<p>The new project was inserted into the database, the ID is %s</p>' % new_id
    else:
        return template('new_project.tpl')

@route('/<no:int>', method="GET")
def project_overview(no:int):

    connection = sqlite3.connect('projects.db')
    c = connection.cursor()
    c.execute("SELECT name, author FROM projects WHERE id LIKE ?", str(no))

    result = c.fetchall()
    c.close()

    print(no, result[0])

    return template('project_overview.tpl', result=result, no=no)

@route('/<no:int>/subjects')
def subjects(no):

    conn = sqlite3.connect('projects.db')
    c = conn.cursor()

    c.execute("SELECT name, places FROM subjects WHERE reference LIKE ?", str(no))
    result = c.fetchall()
    c.close()

    print(result)

    if request.GET.save:
        print('Save request!')
        
        new_subject = request.GET.subject.strip()

        c = conn.cursor()
   
        c.execute("INSERT INTO subjects (name,places) VALUES (?,?)", (new_subject, 20))

        conn.commit()
        c.close()

        return template('subjects.tpl', rows=result, no=no)
    else:
        return template('subjects.tpl', rows=result, no=no)





@route('/create-subject')
def new_subject():
    if request.GET.save:

        new = request.GET.subject.strip()
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()

        c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new,1))
        new_id = c.lastrowid

        conn.commit()
        c.close()

        return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id
    else:
        return template('new_task.tpl')

@route('/test')
def test():
    return template('test.tpl', title = 'matvei')


@route('/todo')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    c.close()
    return template('make_table', rows=result)

@route('/new', method='GET')
def new_item():

    if request.GET.save:

        new = request.GET.task.strip()
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()

        c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new,1))
        new_id = c.lastrowid

        conn.commit()
        c.close()

        return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id
    else:
        return template('new_task.tpl')

@route('/edit/<no:int>', method='GET')
def edit_item(no):

    if request.GET.save:
        edit = request.GET.task.strip()
        status = request.GET.status.strip()

        if status == 'open':
            status = 1
        else:
            status = 0

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("UPDATE todo SET task = ?, status = ? WHERE id LIKE ?", (edit, status, no))
        conn.commit()

        return '<p>The item number %s was successfully updated</p>' % no
    else:
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT task FROM todo WHERE id LIKE ?", (str(no),))
        cur_data = c.fetchone()

        return template('edit_task', old=cur_data, no=no)

run(host='localhost', port=8080, debug=True)