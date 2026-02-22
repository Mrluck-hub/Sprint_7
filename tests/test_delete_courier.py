import pytest
import allure
import random

@allure.feature("Delete courier")
class TestDeleteCourier:
    @allure.title("Successful deleted courier")
    def test_delete_success(self, api, courier_setup):
        i, courier_id = courier_setup
        resp = api.delete_courier(courier_id)
        assert resp.status_code == 200
        assert resp.json()["ok"] is True

    @allure.title("Error deletion without ID")
    def test_delete_courier_without_id_error(self, api):
        resp = api.delete_courier("")
        assert resp.status_code == 400
        assert resp.json()["message"] == "Недостаточно данных для удаления курьера"

    @allure.title("Error deletion with non-existent ID")
    def test_delete_courier_non_existent_id_error(self, api):
        resp = api.delete_courier(random.randint(9999999,999999999))
        assert resp.status_code == 404
        assert resp.json()["message"] == "Курьера с таким id нет"
