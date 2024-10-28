from flask import Blueprint
from controllers.turma_controller import get_turmas, create_turma, get_turma

turmas_bp = Blueprint('turmas', __name__)


# Turmas routes
turmas_bp.route('/turmas', methods=['GET'])(get_turmas)
turmas_bp.route('/turmas', methods=['POST'])(create_turma)
turmas_bp.route('/turmas/<int:turma_id>', methods=['GET'])(get_turma)