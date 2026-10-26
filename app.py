import os
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from werkzeug.utils import secure_filename

app = Flask(__name__)


UPLOAD_FOLDER = os.path.join(app.root_path, 'static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Body_2005#",  
        database="library"
    )


def save_uploaded_file(file_element):
    if file_element and file_element.filename != '':
        filename = secure_filename(file_element.filename)
       
        unique_filename = f"{os.urandom(8).hex()}_{filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file_element.save(filepath)
        return unique_filename
    return None



@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM AUTHOR")
        authors = cursor.fetchall()
        
        cursor.execute("SELECT * FROM BOOK")
        books = cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
        
    return render_template('index.html', authors=authors, books=books)


@app.route('/authors/add', methods=['POST'])
def add_author():
    name = request.form.get('name')
    country = request.form.get('country')
    image_file = request.files.get('image')
    image_filename = save_uploaded_file(image_file)
    
    if name and country:
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO AUTHOR (name, country, image) VALUES (%s, %s, %s)", 
                           (name, country, image_filename))
            conn.commit()
        finally:
            cursor.close()
            conn.close()
            
    return redirect(url_for('index'))


@app.route('/books/add', methods=['POST'])
def add_book():
    title = request.form.get('title')
    price = request.form.get('price')
    author_id = request.form.get('author_id')
    image_file = request.files.get('image')
    image_filename = save_uploaded_file(image_file)
    
    if title and price and author_id:
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO BOOK (title, price, author_id, image) VALUES (%s, %s, %s, %s)", 
                           (title, price, author_id, image_filename))
            conn.commit()
        finally:
            cursor.close()
            conn.close()
            
    return redirect(url_for('index'))


@app.route('/authors/edit/<int:id>', methods=['POST'])
def edit_author(id):
    name = request.form.get('name')
    country = request.form.get('country')
    image_file = request.files.get('image')
    image_filename = save_uploaded_file(image_file)
    
    if name and country:
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            if image_filename:
                cursor.execute("UPDATE AUTHOR SET name = %s, country = %s, image = %s WHERE author_id = %s", 
                               (name, country, image_filename, id))
            else:
                cursor.execute("UPDATE AUTHOR SET name = %s, country = %s WHERE author_id = %s", 
                               (name, country, id))
            conn.commit()
        finally:
            cursor.close()
            conn.close()
            
    return redirect(url_for('index'))


@app.route('/books/edit/<int:id>', methods=['POST'])
def edit_book(id):
    title = request.form.get('title')
    price = request.form.get('price')
    author_id = request.form.get('author_id')
    image_file = request.files.get('image')
    image_filename = save_uploaded_file(image_file)
    
    if title and price and author_id:
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            if image_filename:
                cursor.execute("UPDATE BOOK SET title = %s, price = %s, author_id = %s, image = %s WHERE book_id = %s", 
                               (title, price, author_id, image_filename, id))
            else:
                cursor.execute("UPDATE BOOK SET title = %s, price = %s, author_id = %s WHERE book_id = %s", 
                               (title, price, author_id, id))
            conn.commit()
        finally:
            cursor.close()
            conn.close()
            
    return redirect(url_for('index'))


@app.route('/books/delete/<int:id>', methods=['GET', 'POST'])
def delete_book(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM BOOK WHERE book_id = %s", (id,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()
    return redirect(url_for('index'))


@app.route('/authors/delete/<int:id>', methods=['GET', 'POST'])
def delete_author(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM AUTHOR WHERE author_id = %s", (id,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)