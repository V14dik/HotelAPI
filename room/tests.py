from rest_framework.test import APITestCase
from room.models import Room, Equipment
from django.contrib.auth.models import User


class RoomTests(APITestCase):
    def setUp(self):
        self.room = Room.objects.create(
            description="Test room",
            cost=300,
            square='22.0',
            room_level='ST',
        )
        self.admin = User.objects.create(
            email="admin.admin.com",
            username='admin',
            password='wertyuiuytfd',
            is_staff='True'
        )

    def test_room_unauthorized(self):
        payload = {
            "description": "Test creating room",
            "cost": 310,
            "square": "23.0",
            "room_level": "ST",
            "equipments_inst": [{
                "name": "Test Equipment"
            }]
        }
        response = self.client.post('/api/v1/room/', data=payload)
        self.assertEqual(response.status_code, 401)

    def test_post_room(self):
        payload = {
            "description": "Test creating room",
            "cost": 310,
            "square": "23.0",
            "room_level": "ST",
            "equipments_inst": [{
                "name": "Test Equipment"
            }]
        }

        self.client.force_authenticate(self.admin)
        response = self.client.post('/api/v1/room/', data=payload, format='json')
        self.assertEqual(response.data["description"], payload["description"])
        self.assertEqual(response.data["cost"], payload["cost"])
        self.assertEqual(response.data["square"], payload["square"])
        self.assertEqual(response.data["room_level"], payload["room_level"])
        self.assertEqual(len(response.data["equipments"]), len(payload["equipments_inst"]))

    def test_get_rooms(self):
        response = self.client.get('/api/v1/room/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['description'], self.room.description)
        self.assertEqual(response.data['results'][0]['cost'], self.room.cost)
        self.assertEqual(response.data['results'][0]['square'], self.room.square)
        self.assertEqual(response.data['results'][0]['room_level'], self.room.room_level)
        self.assertEqual(Room.objects.count(), 1)

    def test_delete_room(self):
        rooms_count = len(Room.objects.all())
        self.client.force_authenticate(user=self.admin)
        self.client.delete(f"/api/v1/room/{self.room.id}/")
        self.assertEqual(len(Room.objects.all()), rooms_count-1)
