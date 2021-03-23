from fastapi import FastAPI
from starlette.responses import RedirectResponse
from data import Connexion

app = FastAPI()

@app.get("/", include_in_schema=False)
def redirect():
    return RedirectResponse('/docs')

@app.get("/booking_by_id/{id}", tags=['Bookings'])
def get_booking_id(id: int):
    return Connexion.get_booking_id(id)

@app.get("/bookings_by_name", tags=['Bookings'])
def get_bookings_name(firstname: str, surname: str):
    return Connexion.get_bookings_name(firstname, surname)