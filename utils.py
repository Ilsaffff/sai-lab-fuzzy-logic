import importlib.util

from pydantic import FilePath


def load_module(file_path: FilePath):
    spec = importlib.util.spec_from_file_location("module",
                                                  file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
