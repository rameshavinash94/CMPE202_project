import DifferentFunctions
from fastapi import APIRouter
from pydantic import BaseModel

router=APIRouter(prefix='/hotel',tags=['hotel'])

class Hotel(BaseModel):
    Hotel_name:str
    Locaiton_address:str
    State:str
    Country:str
    City:str
    Zipcode:int

class Hotel_Amenities(BaseModel):
    #need to write it
    pass

@router.post('/add_hotel')
def add_hotel(hotel: Hotel):
    DifferentFunctions.add_Location_info(hotel.Locaiton_address,hotel.State,hotel.Country,hotel.City,hotel.Zipcode)
    DifferentFunctions.add_hotel(hotel.Hotel_name,DifferentFunctions.get_Location_id_by_address(hotel.Locaiton_address))
    return "Added Successfully"

@router.post('/add_hotel_amenities')
def add_hotel(hotel: Hotel):
    pass
    # need to work on this

@router.get('/get_all_hotel')
def get_all_hotels():
    return DifferentFunctions.get_all_hotels()

@router.get('/get_specific_hotel')
def get_specific_hotels(id):
    return DifferentFunctions.get_hotel_location_info(id)

@router.get('/get_hotel_review')
def get_hotel_avg_rating(id):
    return DifferentFunctions.get_average_rating_by_hotel(id)

@router.get('/get_all_Review_by_hotel')
def get_all_Review_by_hotel(id):
    return DifferentFunctions.get_all_Review_by_hotel(id)
