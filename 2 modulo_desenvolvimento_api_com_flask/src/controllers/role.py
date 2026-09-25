from flask import Blueprint, request
from src.app import Role, db
from http import HTTPStatus
from sqlalchemy import inspect


# a forma de instanciar o app é bem parecido

# o nome entre parênteses é o nome de identificação que colocaremos nesse blueprint
# o __name__ vai puxar o nome do módulo
# estamos fazendo no padrão restful então o nome sempre será no plural, como o caso users 


app = Blueprint('role', __name__, url_prefix='/roles')

@app.route('/', methods=["POST"])
def create_role():
        data = request.json
        role = Role(name=data['name'])
        db.session.add(role)
        db.session.commit()
        # CREATED é o status 201, significa que deu tudo certo e criou o usuário
        # sempre pra ver os números clicar cntrl e em cima do HTTPStatus
        return {'message': 'Role created!'}, HTTPStatus.CREATED
        