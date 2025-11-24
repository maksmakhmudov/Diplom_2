import pytest
import requests
import allure
from urls import URL, Endpoints
from data import StatusCode, TextResponse
from helpers import PersonData


class TestChangeUserInfo:
    @allure.title('Change user name after auth test')
    def test_change_user_name(self, create_user):
        token = create_user[1].json()['accessToken']
        headers = {'Authorization': token}
        new_name = PersonData.create_correct_user_data()['name']
        data = {'name': new_name}
        response = requests.patch(URL.main_url + Endpoints.CHANGE_DATA, headers=headers, json=data)
        assert response.status_code == StatusCode.OK
        assert response.json().get('success') is True

    @allure.title('Change data without auth test')
    @pytest.mark.parametrize('field,value', [
        ('name', 'New Test Name'),
        ('email', 'new_test@example.com'),
        ('password', 'newpassword123')
    ])
    def test_change_unauthorized_user_data(self, field, value):
        data = {field: value}
        response = requests.patch(URL.main_url + Endpoints.CHANGE_DATA, json=data)
        assert response.status_code == StatusCode.UNAUTHORIZED
        assert response.json().get('message') == TextResponse.UNAUTHORIZED_RESPONSE
