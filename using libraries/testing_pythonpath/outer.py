import pathlib
from inner.inner import printpath
import sys

print(f"outer sys.path: {sys.path}")

print(f"Outer CWD: {pathlib.Path.cwd()}")
printpath()