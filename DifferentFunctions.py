from DbModels import *

def add_customer(Customer_first_name,Customer_last_name,Customer_Phone,Customer_email_id):
    '''
    :param Customer_id:
    :param Customer_first_name:
    :param Customer_last_name:
    :param Customer_Phone:
    :param Customer_email_id:
    :return:
    '''
    add_customer = Customer(Customer_first_name=Customer_first_name,Customer_last_name=Customer_last_name,Customer_Phone=Customer_Phone,Customer_email_id=Customer_email_id)
    session.add(add_customer)
    session.commit()
    return "Successfully Added"

def get_all_customer_data():
    '''
    :return:
    '''
    customers = session.query(Customer)
    for customer in customers:
        return(customer.Customer_id,customer.Customer_first_name,customer.Customer_last_name,customer.Customer_Phone,customer.Customer_email_id)

def update_Customer(id,kwargs):
    '''
    :param kwargs:
    :return:
    '''
    customers = session.query(Customer).filter_by(Customer_id=id)
    for key,values in kwargs.items():
            if key == 'Customer_first_name':
                customers.Customer_first_name=values
            elif key == 'Customer_last_name':
                customers.Customer_last_name=values
            elif key == 'Customer_Phone':
                customers.Customer_Phone=values
            else:
                customers.Customer_email_id=values
    session.commit()

def get_specific_user_data(id):
    '''
    :param id:
    :return:
    '''
    customer = session.query(Customer).filter_by(Customer_id=id).one()
    return customer.__dict__

def get_all_hotels():
    '''
    :return:
    '''
    hotels = session.query(Hotels)
    for hotel in hotels:
        return(hotel.Hotel_id,hotel.Hotel_name,hotel.Location_id)

def add_hotel(Hotel_name,Location_id):
    '''
    :param Hotel_id:
    :param Hotel_name:
    :param Location_id:
    :return:
    '''
    add_hotel = Hotels(Hotel_name=Hotel_name,Location_id=Location_id)
    session.add(add_hotel)
    session.commit()

def get_all_Location_info():
    '''
    :return:
    '''
    locations = session.query(Location_info)
    for loc in locations:
        return loc.__dict__

def get_Location_id_by_address(Locaiton_address):
    '''
    :param Locaiton_address:
    :return:
    '''
    locations = session.query(Location_info).filter_by(Locaiton_address=Locaiton_address).one()
    return locations.Location_id

def add_Location_info(Locaiton_address,States,Countryy,Cityy,Zipcode):
    '''
    :param Locaiton_address:
    :param State:
    :param Country:
    :param City:
    :param Zipcode:
    :return:
    '''
    try:
        state=session.query(State).filter_by(State=States).one()
    except:
        state_id=State(State=States)
        session.add(state_id)
        session.commit()
        state=session.query(State).filter_by(State=States).one()
    try:
        country=session.query(Country).filter_by(Country=Countryy).one()
    except:
        country_id=Country(Country=Countryy)
        session.add(country_id)
        session.commit()
        country=session.query(Country).filter_by(Country=Countryy).one()
    try:
        city=session.query(City).filter_by(City=Cityy).one()
    except:
        city_id=City(City=Cityy)
        session.add(city_id)
        session.commit()
        city=session.query(City).filter_by(City=Cityy).one()

    location=Location_info(Locaiton_address=Locaiton_address,State_id=state.State_id,Country_id=country.Country_id,City_id=city.City_id,Zipcode=Zipcode)
    session.add(location)
    session.commit()

def get_hotel_location_info(id):
    '''
    :param id:
    :return:
    '''
    hotel_loc_info = session.query(Hotels,Location_info,Country,State,City).filter_by(Hotel_id=id).join(Location_info,Location_info.Location_id==Hotels.Location_id).join(Country,Country.Country_id==Location_info.Country_id).join(State,State.State_id==Location_info.State_id).join(City,City.City_id==Location_info.City_id).all()
    for x in hotel_loc_info:
       return(x.Hotels.Hotel_id,x.Hotels.Hotel_name,x.Location_info.Locaiton_address,x.State.State,x.Country.Country,x.City.City,x.Location_info.Zipcode)

def get_Review():
    '''
    :return:
    '''
    reviews = session.query(Reviews)
    for rev in reviews:
        return rev.__dict__

def add_Review(review_id,booking_id,Ratings,comments):
    '''
    :param review_id:
    :param booking_id:
    :param Ratings:
    :param comments:
    :return:
    '''
    add_review_info = Reviews(review_id=review_id,booking_id=booking_id,Ratings=Ratings,comments=comments)
    session.add(add_review_info)
    session.commit()

def get_all_Review_by_hotel(id):
    '''
    :param id:
    :return:
    '''
    review_by_hotel = session.query(Reviews).join(Booking_details, Booking_details.Booking_id == Reviews.booking_id ).filter_by(hotel_id=id).all()
    for rev in review_by_hotel:
        return rev.__dict__

def get_average_rating_by_hotel(id):
    '''
    :param id:
    :return:
    '''
    with engine.connect() as con:
        rs = con.execute('SELECT bd.hotel_id,avg(rev.Ratings) as average_rating FROM `HotelBookinginfo`.`Booking.Booking_details` as bd left join `HotelBookinginfo`.`Booking.Reviews` as rev on bd.Booking_id =rev.booking_id where hotel_id={id}'.format(id=id))
        for row in rs:
            return row

def get_all_Amenities_info():
    '''
    :return:
    '''
    amenities = session.query(Amenities)
    for amenit in amenities:
        return amenit.__dict__

def get_Amenities_by_hotel_info(id):
    '''
    :param id:
    :return:
    '''
    amenities = session.query(Amenities).filter_by(Hotel_id=id).all()
    for amenit in amenities:
        return amenit.__dict__

def add_Amenities(Amenity_id,Amenity_Name,Amenity_Type,Hotel_id):
    '''
    :param Amenity_id:
    :param Amenity_Name:
    :param Amenity_Type:
    :param Hotel_id:
    :return:
    '''
    add_amenities = Amenities(Amenity_id=Amenity_id,Amenity_Name=Amenity_Name,Amenity_Type=Amenity_Type,Hotel_id=Hotel_id)
    session.add(add_amenities)
    session.commit()

def new_Booking(Booking_id,Customer_id,Booking_date,Check_in_date,Check_in_time,check_out_date,check_out_time,No_of_guest,Breakfast_included,Lunch_included,Dinner_included,hotel_id,room_type_id):
    '''
    :param Booking_id:
    :param Customer_id:
    :param Booking_date:
    :param Check_in_date:
    :param Check_in_time:
    :param check_out_date:
    :param check_out_time:
    :param No_of_guest:
    :param Breakfast_included:
    :param Lunch_included:
    :param Dinner_included:
    :param hotel_id:
    :param room_type_id:
    :return:
    '''
    add_new_booking=Booking_details(Booking_id=Booking_id,Customer_id=Customer_id,Booking_date=Booking_date,Check_in_date=Check_in_date,Check_in_time=Check_in_time,check_out_date=check_out_date,check_out_time=check_out_time,No_of_guest=No_of_guest,Breakfast_included=Breakfast_included,Lunch_included=Lunch_included,Dinner_included=Dinner_included,hotel_id=hotel_id,room_type_id=room_type_id)
    session.add(add_new_booking)
    session.commit()
    add_new_booking_status=Booking_Status(Id=Booking_id,Status='Created')
    session.add(add_new_booking_status)
    session.commit()

def cancel_Booking(id):
    '''
    :param id:
    :return:
    '''
    bookings = session.query(Booking_Status).filter_by(Id=id).all()
    bookings.Status='Cancelled'
    session.commit()

def completed_Booking(id):
    '''
    :param id:
    :return:
    '''
    bookings = session.query(Booking_Status).filter_by(Id=id).all()
    bookings.Status='Completed'
    session.commit()

def NoShow_Booking(id):
    '''
    :param id:
    :return:
    '''
    bookings = session.query(Booking_Status).filter_by(Id=id).all()
    bookings.Status='No-Show'
    session.commit()

def retrive_all_booking_by_customer_id(id):
    '''
    :param id:
    :return:
    '''
    bookings = session.query(Booking_details,Booking_Status,Customer).filter_by(Customer_id=id).join(Booking_Status,Booking_Status.Id == Booking_details.Booking_id).join(Customer,Customer.Customer_id==Booking_details.Customer_id).all()
    for book in bookings:
        return(book.Booking_details.Booking_id,book.Customer.Customer_first_name,book.Customer.Customer_email_id,book.Customer.Customer_Phone,book.Booking_details.Booking_date,
              book.Booking_details.Check_in_date,book.Booking_details.check_out_date,book.Booking_details.check_out_time,book.Booking_details.Check_in_time,book.Booking_details.No_of_guest,
            book.Booking_details.Breakfast_included,book.Booking_details.Lunch_included,book.Booking_details.Dinner_included,
              book.Booking_details.hotel_id,book.Booking_details.room_type_id,book.Booking_Status.Status)

def retrive_all_booking_by_customer_first_name(first_name):
    '''
    :param first_name:
    :return:
    '''
    bookings = session.query(Booking_details,Booking_Status,Customer).join(Booking_Status,Booking_Status.Id == Booking_details.Booking_id).join(Customer,Customer.Customer_id==Booking_details.Customer_id).filter_by(Customer_first_name=first_name).all()
    for book in bookings:
        return(book.Booking_details.Booking_id,book.Customer.Customer_first_name,book.Customer.Customer_email_id,book.Customer.Customer_Phone,book.Booking_details.Booking_date,
              book.Booking_details.Check_in_date,book.Booking_details.check_out_date,book.Booking_details.check_out_time,book.Booking_details.Check_in_time,book.Booking_details.No_of_guest,
            book.Booking_details.Breakfast_included,book.Booking_details.Lunch_included,book.Booking_details.Dinner_included,
              book.Booking_details.hotel_id,book.Booking_details.room_type_id,book.Booking_Status.Status)

def retrive_all_booking_by_customer_email(email_id):
    '''
    :param email_id:
    :return:
    '''
    bookings = session.query(Booking_details,Booking_Status,Customer).join(Booking_Status,Booking_Status.Id == Booking_details.Booking_id).join(Customer,Customer.Customer_id==Booking_details.Customer_id).filter_by(Customer_email_id=email_id).all()
    for book in bookings:
        return(book.Booking_details.Booking_id,book.Customer.Customer_first_name,book.Customer.Customer_email_id,book.Customer.Customer_Phone,book.Booking_details.Booking_date,
              book.Booking_details.Check_in_date,book.Booking_details.check_out_date,book.Booking_details.check_out_time,book.Booking_details.Check_in_time,book.Booking_details.No_of_guest,
            book.Booking_details.Breakfast_included,book.Booking_details.Lunch_included,book.Booking_details.Dinner_included,
              book.Booking_details.hotel_id,book.Booking_details.room_type_id,book.Booking_Status.Status)

def retrive_all_booking_by_hotel(id):
    '''
    :param id:
    :return:
    '''
    bookings = session.query(Booking_details,Booking_Status,Customer).filter_by(hotel_id=id).join(Booking_Status,Booking_Status.Id == Booking_details.Booking_id).join(Customer,Customer.Customer_id==Booking_details.Customer_id).all()
    for book in bookings:
        return(book.Booking_details.Booking_id,book.Customer.Customer_first_name,book.Customer.Customer_email_id,book.Customer.Customer_Phone,book.Booking_details.Booking_date,
              book.Booking_details.Check_in_date,book.Booking_details.check_out_date,book.Booking_details.check_out_time,book.Booking_details.Check_in_time,book.Booking_details.No_of_guest,
            book.Booking_details.Breakfast_included,book.Booking_details.Lunch_included,book.Booking_details.Dinner_included,
              book.Booking_details.hotel_id,book.Booking_details.room_type_id,book.Booking_Status.Status)
