import psycopg2
import psycopg2.extras
from datetime import datetime


class Connexion:    
    @classmethod
    def open_db(cls):
        cls.client = psycopg2.connect(host='db-brief.czpfycmrs28b.eu-west-3.rds.amazonaws.com', user='postgres', password='69,xF%6Yw', port='5432', database='exercises')
        cls.client.autocommit = True
        cls.cursor = cls.client.cursor(cursor_factory=psycopg2.extras.DictCursor)

    @classmethod
    def close_db(cls):
        cls.client.close()
        cls.cursor.close()

    @classmethod
    def get_booking_id(cls, _id):
        cls.open_db()
        cls.cursor.execute(f"SELECT cd.bookings.bookid, cd.facilities.name, cd.members.firstname, cd.members.surname FROM cd.bookings JOIN cd.facilities ON cd.bookings.facid = cd.facilities.facid JOIN cd.members ON cd.bookings.memid = cd.members.memid  WHERE bookid={_id}")
        data = cls.cursor.fetchone()
        cls.close_db()
        return {'booking': {'bookid': data['bookid'], 'facility': {'name': data['name']}, 'member': {'firstname': data['firstname'], 'surname': data['surname']}}}
    
    @classmethod
    def get_bookings_name(cls, firstname, surname):
        cls.open_db()
        cls.cursor.execute(f"SELECT cd.bookings.bookid, cd.facilities.name, cd.bookings.starttime, cd.members.surname FROM cd.bookings JOIN cd.facilities ON cd.bookings.facid = cd.facilities.facid JOIN cd.members ON cd.bookings.memid = cd.members.memid  WHERE firstname='{firstname}' AND surname='{surname}'")
        datas = cls.cursor.fetchall()
        cls.close_db()
        return {'bookings':[{'facility': data['name'], 'starttime': data['starttime'].strftime("%Y/%m/%d, %H:%M:%S")} for data in datas]}