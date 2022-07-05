from datetime import date, datetime
from django.test import TestCase

from blog.models import Post

# Create your tests here.


class TestPost(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            title="abc",
            body="This is the beginning of the blog post, which is going to be more than 150 characters long. This is so we can test that our excerpt property correctly truncates the body to create an",
        )

    def test_str(self):

        expected = "abc"
        actual = str(self.post)

        self.assertEqual(expected, actual)

    def test_excerpt(self):

        expected = "This is the beginning of the blog post, which is going to be more than 150 characters long. This is so we can test that our excerpt property correctly..."

        actual = self.post.excerpt

        self.assertEqual(expected, actual)

    def test_slug_automatically_assigned(self):
        """
        Test that slugs are calculated from the title automatically.
        """
        expected = "abc"
        actual = self.post.slug

        self.assertEqual(expected, actual)

    def test_slug_uniqueness(self):
        """
        Test that two posts with identical titles get unique slugs.
        """
        post2 = Post.objects.create(title="abc", body="test post")

        self.assertNotEqual(self.post.slug, post2.slug)

    def test_post_draft_by_default(self):
        """Test post is automatically given a status of 'draft'"""

        self.assertEqual(self.post.status, "draft")

    def test_created_date(self):
        created = self.post.created_date

        self.assertTrue(created)

    def test_no_published_date(self):
        self.assertFalse(self.post.published_date)

    def test_publish(self):
        self.post.publish()

        self.assertEqual(self.post.status, "published")
        self.assertTrue(self.post.published_date)

    def test_category(self):
        category = self.post.category
        self.assertEqual(category.name, "Uncategorised")
