from rest_framework import test, status

from vehicle.models import Car


class CarTestCase(test.APITestCase):
    def setUp(self) -> None:
        pass

    def test_create_car(self):

        data = {
            'title': 'test create',
            'description': 'test description'
        }

        response = self.client.post(
            '/cars/',
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.json(),
            {'id': 1, 'mileages': [], 'title': 'test create', 'description': 'test description', 'owner': None}
        )

        self.assertTrue(
            Car.objects.all().exists()
        )

    def test_list_car(self):

        Car.objects.create(
            title='test list',
            description='test description'
        )

        responce = self.client.get(
            '/cars/'
        )

        self.assertEquals(
            responce.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            responce.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [
                {'id': 2, 'mileages': [], 'title': 'test list', 'description': 'test description', 'owner': None}]}

        )
