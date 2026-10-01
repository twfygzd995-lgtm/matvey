import math
import sys
import site
import sysconfig

import six

print("=== Проверка пакета six ===")
print("six.__version__ =", six.__version__)
print("six.__file__    =", six.__file__)

print("\n=== Совместимость с PY2/PY3 ===")
print("PY2?", six.PY2, "| PY3?", six.PY3)
print("six.moves.range(3) ->", list(six.moves.range(3)))

print("\n=== Пути поиска модулей ===")
print("sys.path[0] =", sys.path[0])


print("\n=== Решение TODO (Пути к site-packages) ===")


purelib_path = sysconfig.get_paths()["purelib"]
print("site-packages (универсальный):", purelib_path)


try:
    print("site-packages (через site):   ", site.getsitepackages())
except AttributeError:
    print("site-packages (через site):    Недоступно в данном виртуальном окружении")