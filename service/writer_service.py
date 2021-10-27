from config import connection_params
from dbconnector import DBConnector


def get_writer_by_id(writer_id):
    connection = DBConnector().connect(**connection_params)

    select_query = """
            SELECT json_build_object(
                'id', writer.id, 
                'name', writer.name, 
                'books', json_agg(
                            json_build_object(
                            'id', book.id, 
                            'name', book.name
                            )
                    )
            )
            FROM writer
            INNER JOIN book ON writer.id = book.author_id
            WHERE writer.id = %s
            GROUP BY writer.id, writer.name;
            """
    cursor = connection.cursor()
    cursor.execute(select_query, (writer_id,))
    record = cursor.fetchall()
    return record[0][0]
