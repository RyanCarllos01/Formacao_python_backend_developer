from http import HTTPStatus

from src.app import User, db, Role

def test_get_user_sucess(client):
    # Given
    role = Role(name="admin")
    db.session.add(role)
    db.session.commit()
    
    user = User(username="Ryan", password="test", role_id=role.id)
    
    db.session.add(user)
    db.session.commit()
    
    # When
    response = client.get(f'/users/{user.id}')
    
    # Then
    assert response.status_code == HTTPStatus.OK
    assert response.json == {
        "id": user.id, 
        "username": user.username,
        }
    
def test_get_user_not_found(client):
    # Given
    role = Role(name="admin")
    db.session.add(role)
    db.session.commit()
    
    user_id = 1
    
    # user = User(username="Ryan", password="test", role_id=role.id)
    
    # db.session.add(user)
    # db.session.commit()
    
    # When
    response = client.get(f'/users/{user_id}')
    
    # Then
    assert response.status_code == HTTPStatus.NOT_FOUND
    # assert response.json == {
    #     "id": user.id, 
    #     "username": user.username,
    #     }
    
    