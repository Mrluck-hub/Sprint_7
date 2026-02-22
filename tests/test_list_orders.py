import pytest
import allure

@allure.feature("List orders")
class TestListOrders:
    @allure.title("Order list retrieval check")
    def test_get_order_list(self, api):
        resp = api.get_orders_list()
        assert resp.status_code == 200 
        assert 'orders' in resp.json()
        assert len(resp.json().get("orders")) > 0