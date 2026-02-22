import pytest
import allure

@allure.feature("Order Acceptance")
class TestAcceptOrder:
    @allure.title("Order acceptance with non-existent courier ID error")
    def test_accept_order_not_found(self, api, order_setup):
        track = order_setup
        order_info = api.get_order_by_track(track).json()
        order_id = order_info["order"]["id"]
        resp = api.accept_order(order_id, courier_id=999999)
        assert resp.status_code == 404