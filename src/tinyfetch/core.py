from tinyfetch import module
from tinyfetch.module import ASCII_LOGO, Color

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


def render(title_color: str, no_color: bool = False, no_logo: bool = False) -> None:
    if len(ASCII_LOGO) < len(modules_list):
        for _ in range(len(modules_list) - len(ASCII_LOGO)):
            ASCII_LOGO.append(module.Space(amount=len(ASCII_LOGO[0])).output())

    for ascii_logo_line, module_obj in zip(ASCII_LOGO, modules_list):
        output = module_obj.__call__(
            title_color=Color[title_color], no_color=no_color
        ).output()

        if no_logo:
            print(output)
        else:
            print("{} {}".format(ascii_logo_line, output))
