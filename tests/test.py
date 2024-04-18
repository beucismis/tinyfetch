import pytest

import tinyfetch
from tinyfetch import cli


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


class TestCLI:
    def test_version(self):
        @pytest.mark.parametrize("option", ("--version"))
        def test_help(capsys, option):
            cli.main([option])
            output = capsys.readouterr().out

            assert output == f"tinyfetch v{tinyfetch.__version__}"

    def test_help(self):
        @pytest.mark.parametrize("option", ("-h", "--help"))
        def test_help(capsys, option):
            cli.main([option])
            output = capsys.readouterr().out

            assert "Python and system information command-line fetch tool" in output
