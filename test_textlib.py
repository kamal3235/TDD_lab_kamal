import unittest
from textlib import BodyOfText

class TestBodyOfText(unittest.TestCase):
    # In "test_empty_story", create a BodyOfText instance with an empty
    # string, and assert that its "num_paragraphs" method returns zero
    def test_empty_story(self):
        text = BodyOfText("")
        self.assertEqual(0, text.num_paragraphs())

    # Add a method named "test_single_paragraph". Within it, create a
    #    BodyOfText instance for a single paragraph (i.e., a string with no
    #    blank lines, as described above). A single sentence will do fine.
    #    Assert that ".num_paragraphs()" returns 1

    def test_single_paragraph(self):
        text = BodyOfText("A single sentence will do fine")
        self.assertEqual(1, text.num_paragraphs())

    # Create a test string with at least three paragraphs (see example
    #   below). Add a function named "test_several_paragraphs", which
    #   creates a "BodyOfText" instance using that test string, then asserts
    #   that ".num_paragraphs()" returns the correct number

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

# STEP 2 - NOT modifying "textlib.py
# In Command line Identify following
# Test module - in line of FAIL see test_textlib
# test Class - in line of FAIL see TestBodyOf Text
# test methods - in line of FAIL see test_empty_story
# line number - Traceback 3rd line show Line 7, 26, 11
# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
