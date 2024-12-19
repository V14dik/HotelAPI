from rest_framework.test import APITestCase

from booking.models import Booking
from room.models import Room
from django.contrib.auth.models import User


class TestBooking(APITestCase):
    def setUp(self):
        self.admin = User.objects.create(
            email="admin.admin.com",
            username='admin',
            password='wertyuiuytfd',
            is_staff='True'
        )
        self.user = User.objects.create(
            email="user@mail.com",
            username='user',
            password='wertyutfd',
        )
        self.room = Room.objects.create(
            description="Test room",
            cost=300,
            square='22.0',
            room_level='ST',
        )
        self.bookings = Booking.objects.bulk_create([
            Booking(
                user=User.objects.get(id=self.user.id),
                room=Room.objects.get(id=self.room.id),
                date_from='2026-12-20 00:00:00',
                date_till='2026-12-21 00:00:00',
                price=310,),
            Booking(
                user=User.objects.get(id=self.admin.id),
                room=Room.objects.get(id=self.room.id),
                date_from='2026-12-25 00:00:00',
                date_till='2026-12-29 00:00:00',
                price=310)
        ]
        )

    def test_unauthorized_request(self):
        response = self.client.get("/api/v1/booking/")
        self.assertEqual(response.status_code, 401)

    def test_get_bookings_count(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get("/api/v1/booking/")
        self.assertEqual(len(response.data['results']), 1)

        self.client.force_authenticate(user=self.admin)
        response = self.client.get("/api/v1/booking/")
        self.assertEqual(len(response.data["results"]), 2)

    def test_post_booking(self):
        payload = {
            "user": User.objects.get(id=self.user.id).id,
            "room": Room.objects.get(id=self.room.id).id,
            "price": 330,
            "date_from": '2024-12-22',
            "date_till": '2024-12-23'
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post("/api/v1/booking/", data=payload)
        self.assertEqual(response.data["price"], payload["price"])

    def test_get_bookings(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get("/api/v1/booking/")
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['price'], self.bookings[0].price)

    def test_delete_booking(self):
        self.client.force_authenticate(user=self.admin)
        self.client.delete(f"/api/v1/booking/{self.bookings[0].id}/")
        self.assertEqual(len(Booking.objects.all()), len(self.bookings)-1)
