import pytest
import allure
from data.payloads import PayloadGenerator

@allure.feature("Login courier")
class TestLoginCourier:
    @allure.step("Successful courier login")
    def test_login_success(self, api, courier_setup):
        payload = PayloadGenerator.courier_payload()
        api.create_courier(payload)
        courier_setup.append(payload)
        resp = api.login_courier({
            "login": payload["login"],
            "password": payload["password"]
        })
        assert resp.status_code == 200
        assert "id" in resp.json()

    @allure.title("Error: Incorrect password")
    def test_login_wrong_pass(self, api, courier_setup):
        payload = PayloadGenerator.courier_payload()
        api.create_courier(payload)
        courier_setup.append(payload)
        resp = api.login_courier({
            "login": payload["login"],
            "password": "wrong_password"
             
        })
        assert resp.status_code == 404
        assert resp.json()["message"] == "Учетная запись не найдена"
