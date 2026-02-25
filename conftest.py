import pytest
from api_objects.scooter_api import ScooterApi
from data.payloads import PayloadGenerator

@pytest.fixture
def api():
    return ScooterApi()

@pytest.fixture
def courier_setup(api):
    payload = PayloadGenerator.courier_payload()
    api.create_courier(payload)
    
    login_resp = api.login_courier({
        "login": payload["login"],
        "password": payload["password"]
        })
    courier_id = login_resp.json().get("id")

    yield payload, courier_id

    if courier_id:
        api.delete_courier(courier_id)

@pytest.fixture
def order_setup(api):
    payload = PayloadGenerator.ORDER_DATA.copy()
    resp = api.create_order(payload)
    track = resp.json().get("track")

    yield track

    if track:
        api.cancel_order(track)