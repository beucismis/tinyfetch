import pytest

import tinyfetch


class Test:
    def test_module(self):
        module = tinyfetch.Module()
        module.title = "Title"
        module.value = "Value"
        module.no_color = True

        assert module.title == "Title"
        assert module.value == "Value"
        assert module.title_color == tinyfetch.Color.white
        assert module.no_color == True
        assert module.output() == "Title: Value"
