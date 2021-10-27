from config import connection_params
from dbconnector import DBConnector


def init_db():
    connection = DBConnector().connect(**connection_params)

    commands = (
        """DROP TABLE IF EXISTS book;""",
        """DROP TABLE IF EXISTS writer;""",
        """
        CREATE TABLE writer (
            id SERIAL,
            name varchar(100),
            PRIMARY KEY(id)
        );
        """,
        """CREATE TABLE book (
            id SERIAL,
            author_id INT,
            name varchar(100),
            PRIMARY KEY(id),
            CONSTRAINT fk_writer FOREIGN KEY(author_id) REFERENCES writer(id)
        );
        """,

        """INSERT INTO writer(name) VALUES('Пушкин А.С.');""",
        """INSERT INTO book(author_id, name) VALUES(1, 'Руслан и Людмила');""",
        """INSERT INTO book(author_id, name) VALUES(1, 'Капитанская дочка');""",

        """INSERT INTO writer(name) VALUES('Толстой Л.Н.');""",
        """INSERT INTO book(author_id, name) VALUES(2, 'Анна Каренина');""",
        """INSERT INTO book(author_id, name) VALUES(2, 'Война и мир');""",

        """INSERT INTO writer(name) VALUES('Лермонтов М.Ю.');""",
        """INSERT INTO book(author_id, name) VALUES(3, 'Герой нашего времени');""",
    )
    cursor = connection.cursor()
    for command in commands:
        cursor.execute(command)

    connection.commit()
