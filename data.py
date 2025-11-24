class TextResponse:
    DOUBLE_USER_CREATED = "User already exists"
    INTERNAL_SERVER_ERROR = 'Internal Server Error'
    UNAUTHORIZED_RESPONSE = 'You should be authorised'
    

class StatusCode:
    OK = 200
    BAD_REQUEST = 400
    CREATED = 201
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    CONFLICT = 409
    INTERNAL_SERVER_ERROR = 500


class Ingredients:
    correct_ingredients_hash_data = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
        }
    incorrect_ingredients_hash_data = {
        "ingredients": ["69d5b44abracadabaraf6a76", "609646e4daboradabara2870"]
        }
    empty_ingredients_data = {
        "ingredients": []
        }
