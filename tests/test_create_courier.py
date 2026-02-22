import pytest
import allure
from data.payloads import PayloadGenerator

@allure.feature("Create courier")
class TestCreateCourier:
    @allure.title("Successful courier craetion")
    def test_create_success(self, api):
        payload = PayloadGenerator.courier_payload()
        resp = api.create_courier(payload)
        assert resp.status_code == 201
        assert resp.json()["ok"] is True

    @allure.title("Can't create two identical couriers")
    def test_no_double_courier(self, api, courier_setup):
        payload, i = courier_setup
        resp = api.create_courier(payload)
        assert resp.status_code == 409
        assert resp.json()["message"] == "Этот логин уже используется"

    @allure.title("Create courier without required field error")
    @pytest.mark.parametrize("field", ["login", "password"])
    def test_missing_field_error(self, api, field):
        payload = PayloadGenerator.courier_payload()
        del payload[field]
        resp = api.create_courier(payload)
        assert resp.status_code == 400
        assert resp.json()["message"] == "Недостаточно данных для создания учетной записи"
        