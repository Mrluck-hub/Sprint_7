import requests
import allure
from data.urls import Urls

class ScooterApi:
    @allure.step("POST Create courier")
    def create_courier(self, payload):
        return requests.post(Urls.COURIER, data=payload)
    
    @allure.step("POST Login courier")
    def login_courier(self, payload):
        return requests.post(Urls.LOGIN, data=payload)
    
    @allure.step("DELETE Delete courier")
    def delete_courier(self, courier_id):
        return requests.delete(f"{Urls.COURIER}/{courier_id}")
    
    @allure.step("POST Create order")
    def create_order(self, payload):
        return requests.post(Urls.ORDERS, json=payload)
    
    @allure.step("GET Orders list")
    def get_orders_list(self):
        return requests.get(Urls.ORDERS)
    
    @allure.step("PUT Accept order")
    def accept_order(self, order_id, courier_id):
        return requests.put(f"{Urls.ACCEPT_ORDER}/{order_id}", params={"courierId": courier_id})
    
    @allure.step("GET Order by track")
    def get_order_by_track(self, track):
        return requests.get(Urls.GET_ORDER_TRACK, params={"t": track})
    
    @allure.step("PUT Accept order")
    def accept_order(self, order_id, courier_id):
        return requests.put(f"{Urls.ACCEPT_ORDER}/{order_id}", params={"courierId": courier_id})
    
    @allure.step("PUT Cancel order")
    def cancel_order(self, track_number):
        return requests.put(Urls.CANCEL_ORDER, params={"track": track_number})