from app import application
from service.writer_service import get_writer_by_id


@application.route('/writers/<writer_id>', methods=['GET'])
def get_writer(writer_id):
    return get_writer_by_id(writer_id)

