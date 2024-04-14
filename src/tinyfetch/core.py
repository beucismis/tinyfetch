from tinyfetch import module
from tinyfetch.module import Color

modules_list = [
    module.Space,
    module.UserHost,
    module.SplitLine,
    module.PythonVersion,
    module.PIPVersion,
    module.PIPPackages,
    module.Implementation,
    module.Compiler,
    module.Space,
    module.Kernel,
    module.OperationSystem,
    module.Space,
]


def render(title_color: str, no_color: bool = False) -> None:
    for m in modules_list:
        print(m.__call__(title_color=Color[title_color], no_color=no_color).output())
