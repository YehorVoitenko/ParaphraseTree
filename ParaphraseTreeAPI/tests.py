from django.test import TestCase


# Create your tests here.


class TestAPI(TestCase):
    def setUp(self):
        self.test_text = (
            "(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter) ) (, ,) (CC or) (NP (NNP "
            "Barri) (NNP "
            "Gòtic) ) ) "
            "(, ,) (VP (VBZ has) (NP (NP (JJ narrow) (JJ medieval) (NNS streets) ) (VP (VBN filled) (PP "
            "(IN with) "
            "(NP (NP "
            "(JJ trendy) (NNS bars) ) (, ,) (NP (NNS clubs) ) (CC and) (NP (JJ Catalan) (NNS "
            "restaurants) ) ) ) ) "
            ") ) )"
        )

    def test_paraphrase_page_with_all_params(self):
        response = self.client.get(f"/paraphrase/?tree={self.test_text};limit=10")
        self.assertEqual(response.status_code, 200)

    def test_paraphrase_page_trees_quantity_by_user_value(self):
        response = self.client.get(f"/paraphrase/?tree={self.test_text};limit=10")
        self.assertEqual(response.status_code, 200)

        # Test if trees quantity is similar to limit value

        self.assertEqual(len(response.data["paraphrases"]), 10)

    def test_paraphrase_page_trees_quantity_by_default(self):
        response = self.client.get(f"/paraphrase/?tree={self.test_text}")
        self.assertEqual(response.status_code, 200)

        # Test if trees quantity is similar to default (20) limit value
        self.assertEqual(len(response.data["paraphrases"]), 20)
