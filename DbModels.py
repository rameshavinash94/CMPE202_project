#importing Libraries
from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import Column,String,DateTime,Integer,BigInteger,create_engine

#DB connect info
engine = create_engine('mysql+pymysql://avnadmin:AVNS_ZT6dfWkjrsI7bgE@mysql-avinash-sjsu-adbc.aivencloud.com:17991/HotelBookinginfo')

#session creation
Session = sessionmaker(bind=engine)
session= Session()
Base= declarative_base()

#Customer Class
class Customer(Base):
    __tablename__ = 'Customer.Customer_Details'
    Customer_id=Column(Integer,primary_key=True,autoincrement=True)
    Customer_first_name=Column(String)
    Customer_last_name=Column(String)
    Customer_Phone=Column(Integer)
    Customer_email_id=Column(String)

#Hotels Class
class Hotels(Base):
    __tablename__ = 'Hotel.Hotels'
    Hotel_id=Column(Integer,primary_key=True,autoincrement=True)
    Hotel_name=Column(String(50))
    Location_id=Column(Integer)

#Location Info
class Location_info(Base):
    __tablename__ = 'Hotel.Location_info'
    Location_id=Column(Integer,primary_key=True,autoincrement=True)
    Locaiton_address=Column(String(100))
    State_id=Column(Integer)
    Country_id=Column(Integer)
    City_id=Column(Integer)
    Zipcode=Column(Integer)

#Review Info
class Reviews(Base):
    __tablename__ = 'Booking.Reviews'
    review_id=Column(Integer,primary_key=True,autoincrement=True)
    booking_id=Column(Integer)
    Ratings=Column(Integer)
    comments=Column(String(200))

#Amenities
class Amenities(Base):
    __tablename__ = 'Hotel.Amenities'
    Amenity_id=Column(Integer,primary_key=True)
    Amenity_Name=Column(String(50))
    Amenity_Type=Column(String(50))
    Hotel_id=Column(Integer,primary_key=True)

# Booking Details
class Booking_details(Base):
    __tablename__ = 'Booking.Booking_details'
    Booking_id=Column(Integer,primary_key=True,autoincrement=True)
    Customer_id=Column(Integer)
    Booking_date=Column(String(50))
    Check_in_date=Column(DateTime)
    Check_in_time=Column(String(5))
    check_out_date=Column(DateTime)
    check_out_time=Column(String(5))
    No_of_guest=Column(Integer)
    Breakfast_included=Column(String(1))
    Lunch_included=Column(String(1))
    Dinner_included=Column(String(1))
    hotel_id=Column(Integer)
    room_type_id=Column(Integer)

# Room types
class Rooms_types(Base):
    __tablename__ = 'Hotel.Rooms_types'
    Room_type_id=Column(Integer,primary_key=True)
    Room_type_Name=Column(String(20))
    Room_capacity=Column(Integer)

#Booking Status
class Booking_Status(Base):
    __tablename__ = 'Booking.Booking_Status'
    Id=Column(Integer,primary_key=True)
    Status=Column(String(50))

#Booking Rooms
class Booking_rooms(Base):
    __tablename__ = 'Booking.Booking_rooms'
    Id=Column(Integer,primary_key=True)
    Booking_id= Column(Integer)
    Room_type_id=Column(Integer)
    Allocated_room=Column(Integer)

#State
class State(Base):
    __tablename__ = 'Hotel.State'
    State_id=Column(Integer,primary_key=True,autoincrement=True)
    State=Column(String(30))

#Country
class Country(Base):
    __tablename__ = 'Hotel.Country'
    Country_id=Column(Integer,primary_key=True,autoincrement=True)
    Country=Column(String(30))

#City
class City(Base):
    __tablename__ = 'Hotel.City'
    City_id=Column(Integer,primary_key=True,autoincrement=True)
    City=Column(String(30))

#Customer Points
class Customer_Points(Base):
    __tablename__ = 'Rewards.Customer_Points'
    Customer_id=Column(Integer,primary_key=True,autoincrement=True)
    Points=Column(BigInteger)
