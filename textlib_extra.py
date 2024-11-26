# Abu Kamal
# Count paragraph
# Split text to make paragraph (\n)
# paragraphs = text.split('\n')


class BodyOfText:
    def __init__(self, text):
        self.text = text.strip()
        # strip leading/trailing whitespace
    def num_paragraphs(self):
        return len([p for p in self.text.split('\n\n') if p.strip()])

    def paragraphs(self):
        return [p.strip() for p in self.text.split('\n\n') if p.strip()]

