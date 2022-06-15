from app.api import PetFriends
from app.settings import valid_email, valid_password
from app.pets import valid_name, valid_age, valid_animal_type, valid_pet_photo
import os

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_add_pet(name=valid_name, animal_type=valid_animal_type, age=valid_age, pet_photo=valid_pet_photo):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert 'id' in result



"""
def test_del_pet(pet_id):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status = pf.delete_pet(auth_key, pet_id)
    assert status == 200
"""





