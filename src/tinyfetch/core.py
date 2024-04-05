from tinyfetch import module


def render() -> None:
    modules = [
        module.Space(),
        module.UserHost(),
        module.SplitLine(),
        module.PythonVersion(),
        module.PIPVersion(),
        module.PIPPackages(),
        module.Implementation(),
        module.Compiler(),
        module.Space(),
        module.Kernel(),
        module.OperationSystem(),
        module.Space(),
    ]

    for m in modules:
        print(m.output())
