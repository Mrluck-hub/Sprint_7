import pytest
import allure
from data.payloads import PayloadGenerator

@allure.feature("Order retrieval")
class TestGetOrder:
    @allure.title("Successful order retrieval by track number")
    def test_get_order_by_track_success(self, api, order_setup):
        payload = PayloadGenerator.ORDER_DATA
        order_resp = api.create_order(payload)
        track = order_resp.json()["track"]
        order_setup.append(track)
        resp = api.get_order_by_track(track)
        assert resp.status_code == 200
        assert resp.json()["order"]["track"] == track