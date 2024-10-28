from flask import Blueprint
from controllers.professor_controller import get_professores, create_professor, id_professor, update_professor, delete_professor

professores_bp = Blueprint('professores', __name__)


# Professores routes
professores_bp.route('/professores', methods=['GET'])(get_professores)
professores_bp.route('/professores/create', methods=['POST'])(create_professor)
professores_bp.route('/professores/<int:professor_id>', methods=['GET'])(id_professor)
professores_bp.route('/professores/update/<int:professor_id>', methods=['PUT'])(update_professor)
professores_bp.route('/professores/delete/<int:professor_id>', methods=['DELETE'])(delete_professor)