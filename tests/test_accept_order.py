import pytest
import allure
from data.payloads import PayloadGenerator

@allure.feature("Order Acceptance")
class TestAcceptOrder:
    @allure.title("Order acceptance with non-existent courier ID error")
    def test_accept_order_not_found(self, api, order_setup):
        payload = PayloadGenerator.ORDER_DATA
        order_resp = api.create_order(payload)
        track = order_resp.json()["track"]
        order_setup.append(track)
        order_info = api.get_order_by_track(track).json()["order"]["id"]
        resp = api.accept_order(order_info, courier_id=999999)
        assert resp.status_code == 404
        assert resp.json()["message"] == "Курьера с таким id не существует"