import pytest
import allure

@allure.feature("Order retrieval")
class TestGetOrder:
    @allure.title("Successful order retrieval by track number")
    def test_get_order_by_track_success(self, api, order_setup):
        track = order_setup
        resp = api.get_order_by_track(track)
        assert resp.status_code == 200
        assert resp.json()["order"]["track"] == track