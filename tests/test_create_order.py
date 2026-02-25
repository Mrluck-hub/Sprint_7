import pytest
import allure
from data.payloads import PayloadGenerator

@allure.feature("Create order")
class TestCreateOrder:
    @allure.title("Order creation with color parametrization")
    @pytest.mark.parametrize("colors", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
        ])
    def test_create_order_colors(self, api, colors):
        payload = PayloadGenerator.ORDER_DATA.copy()
        payload["color"] = colors
        resp = api.create_order(payload)
        assert resp.status_code == 201
        assert "track" in resp.json()

        track = resp.json().get("track")
        if track:
            api.cancel_order(track)
