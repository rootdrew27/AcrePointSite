from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import GalleryCategory, GalleryItem

# class GalleryViewTests(TestCase):
#     def setUp(self):
#         self.category1 = GalleryCategory.objects.create(title="Category 1")
#         self.category2 = GalleryCategory.objects.create(title="Category 2")

#         # Create a sample image file for testing
#         image_file = SimpleUploadedFile("test_image.jpg", content=b"", content_type="image/jpeg")

#         self.item1 = GalleryItem.objects.create(title="Item 1", image=image_file)
#         self.item1.categories.add(self.category1)

#         self.item2 = GalleryItem.objects.create(title="Item 2", image=image_file)
#         self.item2.categories.add(self.category1, self.category2)


#     def test_gallery_index_view(self):
#         response = self.client.get(reverse('GalleryIndex'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'Gallery/index.html')
#         self.assertContains(response, "Category 1")
#         self.assertContains(response, "Category 2")
#         self.assertContains(response, "Item 1")
#         self.assertContains(response, "Item 2")

#     def test_gallery_detail_view(self):
#         response = self.client.get(reverse('GalleryDetail', args=[self.item1.pk]))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'Gallery/detail.html')
#         self.assertContains(response, "Item 1")
#         self.assertNotContains(response, "Item 2")

#         response = self.client.get(reverse('GalleryDetail', args=[self.item2.pk]))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'Gallery/detail.html')
#         self.assertNotContains(response, "Item 1")
#         self.assertContains(response, "Item 2")