# Abu Kamal
# test for textlib


import unittest
from textlib_extra import BodyOfText

class TestBodyOfText(unittest.TestCase):
    # In "test_empty_story", create a BodyOfText instance with an empty
    # string, and assert that its "num_paragraphs" method returns zero
    def test_empty_story(self):
        text = BodyOfText("")
        self.assertEqual(0, text.num_paragraphs())
        self.assertEqual([], text.paragraphs())

    # Add a method named "test_single_paragraph". Within it, create a
    #    BodyOfText instance for a single paragraph (i.e., a string with no
    #    blank lines, as described above). A single sentence will do fine.
    #    Assert that ".num_paragraphs()" returns 1

    def test_single_paragraph(self):
        text = BodyOfText("A single sentence will do fine")
        self.assertEqual(1, text.num_paragraphs())
        self.assertEqual(["A single sentence will do fine"], text.paragraphs())

    # Create a test string with at least three paragraphs (see example
    #   below). Add a function named "test_several_paragraphs", which
    #   creates a "BodyOfText" instance using that test string, then asserts
    #   that ".num_paragraphs()" returns the correct number

    def test_several_paragraphs(self):
        text = BodyOfText("""This is a longer story. It has several paragraphs.

Once upon a time, there was a young dragon living in a lush, ample valley,

One day, the young dragon's wings finally grew big enough

four paragraphs, End of story""")
        self.assertEqual(4, text.num_paragraphs())

        expected = ['This is a longer story. It has several paragraphs.',

'Once upon a time, there was a young dragon living in a lush, ample valley,',

"One day, the young dragon's wings finally grew big enough",

'four paragraphs, End of story',
]
        self.assertEqual(expected, text.paragraphs())


# STEP 2 - NOT modifying "textlib.py
# In Command line Identify following
# Test module - in line of FAIL see test_textlib
# test Class - in line of FAIL see TestBodyOf Text
# test methods - in line of FAIL see test_empty_story
# line number - Traceback 3rd line show Line 7, 26, 11
