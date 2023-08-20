import pytest
from datetime import datetime, time
from ayo_indonesia import Sewa  

@pytest.fixture
def setup_database():
    
    db = Sewa()
    db.insert_booking(1001, "BK/000001", 15, 12, "2022-12-10", "09:00:00", "11:00:00", 1200000)
    db.insert_booking(1005, "BK/000005", 15, 12, "2022-12-10", "09:00:00", "11:00:00", 1000000)
    db.insert_schedule(11, 15, "2022-12-10", "07:00:00", "09:00:00", 800000)
    db.insert_schedule(12, 15, "2022-12-10", "09:00:00", "11:00:00", 1000000)
    db.insert_schedule(13, 15, "2022-12-10", "11:00:00", "13:00:00", 1200000)
    return db

def test_incorrect_price(setup_database):
    db = setup_database
    
    # Ambil detail pemesanan dari database
    booking_id = "BK/000001"
    booking = db.get_booking_by_id(booking_id)
    
    # Ambil expected price dari schedule
    schedule_id = 12  
    expected_price = db.get_schedule_price(schedule_id)
    
    # Bandingkan harga yang tersimpan dengan harga seharusnya
    assert booking["price"] == expected_price, "Tidak sesuai harga yang seharusnya"

def test_double_booking(setup_database):
    db = setup_database
    
    # Ambil detail pemesanan dari database
    booking_id = "BK/000001"
    booking = db.get_booking_by_id(booking_id)
    
    # Periksa double book pada tanggal dan waktu yang sama
    conflicting_bookings = db.get_conflicting_bookings(booking["venue_id"], booking["date"], booking["start_time"], booking["end_time"])
    
    # Pastikan tidak ada booking yang bermasalah
    assert len(conflicting_bookings) == 0, "Terdeteksi adanya double booking"

if __name__ == "__main__":
    pytest.main()