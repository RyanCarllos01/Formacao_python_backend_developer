from flask import Blueprint, request
from src.app import User, db
from http import HTTPStatus
from sqlalchemy import inspect
from flask_migrate import Migrate
from flask_jwt_extended import get_jwt_identity, jwt_required
from src.controllers.utils import requires_role

# a forma de instanciar o app é bem parecido

# o nome entre parênteses é o nome de identificação que colocaremos nesse blueprint
# o __name__ vai puxar o nome do módulo
# estamos fazendo no padrão restful então o nome sempre será no plural, como o caso users 


app = Blueprint('user', __name__, url_prefix='/users')
# localhost:5000/users
def _create_user():
    data = request.json
    user = User(
                username=data["username"],
                password=data["password"],
                role_id=data["role_id"],
                )
    
    
    db.session.add(user)
    db.session.commit()
 
 # retornando usuário do banco de dados   
def _list_users():
    query = db.select(User)
    users = db.session.execute(query).scalars()
    return[
        {
         'id': user.id, 
         'username': user.username,
         "role": {
                  "id": user.role.id, 
                  "name": user.role.name,
                  },
        }
        for user in users
    ]

@app.route('/', methods=["GET", "POST"])
@jwt_required()
@requires_role("admin")
def handle_user():
    user_id = get_jwt_identity()
    user = db.get_or_404(User, user_id)
    if user.role.name != "admin":
         return ({"msg": "uset dont have found"}), HTTPStatus.FORBIDDEN
    requires_role("admin")
    if request.method == "POST":
        _create_user()
        # CREATED é o status 201, significa que deu tudo certo e criou o usuário
        # sempre pra ver os números clicar cntrl e em cima do HTTPStatus
        return {'message': 'User created!'}, HTTPStatus.CREATED
        pass
    else:
        return {"Users": _list_users()}
    
@app.route('/<int:user_id>')
# esse jwt required só permite que liste ou crie usuário se tiver logado via token
# toda vez que for fazer uma operação no /users até pra listar
# precisa do token que é gerado no auth/login na operação de post quando criamos o usuário gera o token

def list_or_create_user(user_id):
   user = db.get_or_404(User, user_id )
   return {
       "id": user.id,
       "username": user.username,
   }
   # PATCH é atualização parcial, e pode alterar todos os atributos também
   # put tem que alterar tudo 
@app.route('/<int:user_id>', methods=["PATCH"])
def update_user(user_id):
   user = db.get_or_404(User, user_id )
   data = request.json
   
   
   mapper = inspect(User)
   for column in mapper.attrs:
       if column.key in data:
        setattr(user, column.key, data[column.key])
   db.session.commit() 
   
   return {
       "id": user.id,
       "username": user.username,
   }
   
 # fazendo delete  
@app.route('/<int:user_id>', methods=["DELETE"])
def delete_user(user_id):
   user = db.get_or_404(User, user_id )
   db.session.delete(user)
   db.session.commit()
   return "", HTTPStatus.NO_CONTENT