import unittest
from helpers import extract_code_blocks


class TestExtractCodeBlocks(unittest.TestCase):
    def test_single_code_block(self):
        content = """This is some text.
        
```
def foo():
    return 'bar'
```

        More text.
        """
        expected = ["def foo():\n    return 'bar'"]
        result = extract_code_blocks(content)
        self.assertEqual(result, expected)

    def test_multiple_code_blocks(self):
        content = """Here is some markdown.

```
def foo():
    return 'bar'
```

Some more explanations.

```
print("Hello, world!")
```

Even more text.
"""
        expected = ["def foo():\n    return 'bar'", 'print("Hello, world!")']
        result = extract_code_blocks(content)
        self.assertEqual(result, expected)

    def test_no_code_blocks(self):
        content = """This is some text without any code blocks.
        
        Here is more text.
        """
        expected = []
        result = extract_code_blocks(content)
        self.assertEqual(result, expected)

    def test_empty_code_block(self):
        content = """This text surrounds an empty code block.
        
        ```
        ```

        And some more text.
        """
        expected = [""]
        result = extract_code_blocks(content)
        self.assertEqual(result, expected)

    def test_code_block_with_triple_backticks(self):
        content = """Here is a code block with triple backticks inside:

```
def foo():
    return '''bar'''
```

        More text.
        """
        expected = ["def foo():\n    return '''bar'''"]
        result = extract_code_blocks(content)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
