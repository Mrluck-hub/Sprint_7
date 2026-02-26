import pytest
from api_objects.scooter_api import ScooterApi
from data.payloads import PayloadGenerator

@pytest.fixture
def api():
    return ScooterApi()

@pytest.fixture
def courier_setup(api):
    couriers = []
    yield couriers
    
    for p in couriers:
        r = api.login_courier(p)
        if r.status_code == 200: api.delete_courier(r.json()["id"])

@pytest.fixture
def order_setup(api):
    tracks_to_cancel = []
    yield tracks_to_cancel
    
    for track in tracks_to_cancel:
        api.cancel_order(track)