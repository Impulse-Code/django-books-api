from django.test import TestCase
from .models import Book
# Create your tests here.

class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book=Book.objects.create(
            title="Black Panther",
            number_of_pages=400,
            quantity=100
        )

    def test_model_content(self):
        self.assertEqual(self.book.title, "Black Panther")
        self.assertEqual(self.book.number_of_pages, 400)
        self.assertEqual(self.book.quantity, 100)
        self.assertEqual(str(self.book), "Black Panther") 