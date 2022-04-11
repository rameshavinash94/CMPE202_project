CREATE TABLE "Booking.Booking_details" (
  "Booking_id" int NOT NULL AUTO_INCREMENT,
  "Customer_id" int NOT NULL,
  "Booking_date" date NOT NULL,
  "Check_in_date" date NOT NULL,
  "Check_in_time" varchar(5) NOT NULL,
  "check_out_date" date DEFAULT NULL,
  "check_out_time" varchar(5) DEFAULT NULL,
  "No_of_guest" int NOT NULL,
  "Breakfast_included" char(1) NOT NULL DEFAULT 'N',
  "Lunch_included" char(1) NOT NULL DEFAULT 'N',
  "Dinner_included" char(1) NOT NULL DEFAULT 'N',
  "hotel_id" int NOT NULL,
  "room_type_id" int NOT NULL,
  PRIMARY KEY ("Booking_id"),
  KEY "fk_Booking_details_Customer_id" ("Customer_id"),
  KEY "fk_Booking_details_hotel_id" ("hotel_id"),
  KEY "fk_Booking_details_room_type_id" ("room_type_id"),
  CONSTRAINT "fk_Booking_details_Customer_id" FOREIGN KEY ("Customer_id") REFERENCES "Customer.Customer_Details" ("Customer_id"),
  CONSTRAINT "fk_Booking_details_hotel_id" FOREIGN KEY ("hotel_id") REFERENCES "Hotel.Hotels" ("Hotel_id"),
  CONSTRAINT "fk_Booking_details_room_type_id" FOREIGN KEY ("room_type_id") REFERENCES "Hotel.Rooms_types" ("Room_type_id")
);

CREATE TABLE "Booking.Booking_rooms" (
  "Id" int NOT NULL,
  "Booking_id" int NOT NULL,
  "Room_type_id" int NOT NULL,
  "Allocated_room" int NOT NULL,
  PRIMARY KEY ("Id"),
  KEY "fk_Booking_rooms_Booking_id" ("Booking_id"),
  KEY "fk_Allocated_rooms_info_Booking_id" ("Room_type_id"),
  CONSTRAINT "fk_Allocated_rooms_info_Booking_id" FOREIGN KEY ("Room_type_id") REFERENCES "Booking.Booking_details" ("room_type_id"),
  CONSTRAINT "fk_Booking_rooms_Booking_id" FOREIGN KEY ("Booking_id") REFERENCES "Booking.Booking_details" ("Booking_id")
);

CREATE TABLE "Booking.Booking_Status" (
  "Id" int NOT NULL,
  "Status" varchar(30) NOT NULL,
  PRIMARY KEY ("Id"),
  CONSTRAINT "fk_Booking_Status_Id" FOREIGN KEY ("Id") REFERENCES "Booking.Booking_details" ("Booking_id")
);

CREATE TABLE "Booking.Reviews" (
  "review_id" int NOT NULL AUTO_INCREMENT,
  "booking_id" int NOT NULL,
  "Ratings" int NOT NULL,
  "comments" varchar(200) NOT NULL,
  PRIMARY KEY ("review_id"),
  KEY "fk_Reviews_booking_id" ("booking_id"),
  CONSTRAINT "fk_Reviews_booking_id" FOREIGN KEY ("booking_id") REFERENCES "Booking.Booking_details" ("Booking_id")
);

CREATE TABLE "Customer.Customer_Details" (
  "Customer_id" int NOT NULL AUTO_INCREMENT,
  "Customer_first_name" varchar(50) NOT NULL,
  "Customer_last_name" varchar(50) NOT NULL,
  "Customer_Phone" int NOT NULL,
  "Customer_email_id" varchar(60) NOT NULL,
  PRIMARY KEY ("Customer_id")
);

CREATE TABLE "Hotel.Amenities" (
  "Amenity_id" int NOT NULL,
  "Amenity_Name" varchar(50) NOT NULL,
  "Amenity_Type" varchar(50) NOT NULL,
  "Hotel_id" int NOT NULL,
  PRIMARY KEY ("Hotel_id","Amenity_id"),
  CONSTRAINT "fk_Hotels_Hotel_id" FOREIGN KEY ("Hotel_id") REFERENCES "Hotel.Hotels" ("Hotel_id")
);

CREATE TABLE "Hotel.City" (
  "City_id" int NOT NULL AUTO_INCREMENT,
  "City" varchar(30) NOT NULL,
  PRIMARY KEY ("City_id")
);

CREATE TABLE "Hotel.Country" (
  "Country_id" int NOT NULL AUTO_INCREMENT,
  "Country" varchar(30) NOT NULL,
  PRIMARY KEY ("Country_id")
);

CREATE TABLE "Hotel.Hotels" (
  "Hotel_id" int NOT NULL AUTO_INCREMENT,
  "Hotel_name" varchar(50) NOT NULL,
  "Location_id" int NOT NULL,
  PRIMARY KEY ("Hotel_id"),
  KEY "fk_Hotels_Location_id" ("Location_id"),
  CONSTRAINT "fk_Hotels_Location_id" FOREIGN KEY ("Location_id") REFERENCES "Hotel.Location_info" ("Location_id")
);

CREATE TABLE "Hotel.Location_info" (
  "Location_id" int NOT NULL AUTO_INCREMENT,
  "Locaiton_address" varchar(100) NOT NULL,
  "State_id" int NOT NULL,
  "Country_id" int NOT NULL,
  "City_id" int NOT NULL,
  "Zipcode" int NOT NULL,
  PRIMARY KEY ("Location_id"),
  KEY "fk_Location_info_State_id" ("State_id"),
  KEY "fk_Location_info_Country_id" ("Country_id"),
  KEY "fk_Location_info_City_id" ("City_id"),
  CONSTRAINT "fk_Location_info_City_id" FOREIGN KEY ("City_id") REFERENCES "Hotel.City" ("City_id"),
  CONSTRAINT "fk_Location_info_Country_id" FOREIGN KEY ("Country_id") REFERENCES "Hotel.Country" ("Country_id"),
  CONSTRAINT "fk_Location_info_State_id" FOREIGN KEY ("State_id") REFERENCES "Hotel.State" ("State_id")
);

CREATE TABLE "Hotel.Rooms_types" (
  "Room_type_id" int NOT NULL,
  "Room_type_Name" varchar(20) NOT NULL,
  "Room_capacity" int NOT NULL,
  PRIMARY KEY ("Room_type_id")
);

CREATE TABLE "Hotel.State" (
  "State_id" int NOT NULL AUTO_INCREMENT,
  "State" varchar(30) NOT NULL,
  PRIMARY KEY ("State_id")
);

CREATE TABLE "Rewards.Customer_Points" (
  "Customer_id" int NOT NULL,
  "Points" bigint NOT NULL,
  "Customer_loyality_band" varchar(45) DEFAULT NULL,
  PRIMARY KEY ("Customer_id"),
  CONSTRAINT "fk_Customer_Points_Customer_id" FOREIGN KEY ("Customer_id") REFERENCES "Customer.Customer_Details" ("Customer_id")
);
