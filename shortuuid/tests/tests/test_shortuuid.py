from django.test import SimpleTestCase


class TestShortUUIDGeneration(SimpleTestCase):
    def test_generated_ids_are_22_characters_long(self):
        from shortuuid.models.fields import ShortUUIDField

        field = ShortUUIDField()
        self.assertEqual(len(field.default()), 22)
