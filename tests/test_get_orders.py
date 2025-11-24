import requests
import allure
from urls import URL, Endpoints
from data import StatusCode, TextResponse, Ingredients


class TestGetOrder:
    @allure.title('Get order by authorized user')
    def test_get_orders_by_authorized_user(self, create_user):
        token = create_user[1].json()['accessToken']
        headers = {'Authorization': token}
        response_create_order = requests.post(URL.main_url + Endpoints.CREATE_ORDER,
                                              headers=headers, data=Ingredients.correct_ingredients_hash_data)
        response_get_order = requests.get(URL.main_url + Endpoints.GET_ORDERS, headers=headers)
        assert response_get_order.status_code == StatusCode.OK
        assert response_create_order.json()['order']['number'] == response_get_order.json()['orders'][0]['number']

    @allure.title('Get order by unauthorized user')
    def test_get_orders_by_unauthorized_user(self):
        response_get_orders = requests.get(URL.main_url + Endpoints.GET_ORDERS)
        assert response_get_orders.status_code == StatusCode.UNAUTHORIZED
        assert TextResponse.UNAUTHORIZED_RESPONSE in response_get_orders.text
