import unittest
from textlib import BodyOfText

class TestBodyOfText(unittest.TestCase):
    def test_empty_story(self):
        text = BodyOfText("")
        self.assertEqual(0, text.num_paragraphs())

    def test_single_paragraph(self):
        text = BodyOfText("A single sentence will do fine")
        self.assertEqual(1, text.num_paragraphs())

    def test_several_paragraphs(self):
        text = BodyOfText("""This is a longer story. It has several paragraphs.

Once upon a time, there was a young dragon living in a lush, ample
valley, nestled among the mountains. The dragon had a happy childhood,
growing up playing fun games with other dragon children, and being
taken care of well by his parents.

One day, the young dragon's wings finally grew big enough that he
could start to fly. What a wonderful experience! For the first time in
his life, he could gracefully sail over the tops of trees.
        
four paragraphs, End pf story""")
        self.assertEqual(4, text.num_paragraphs())

# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
