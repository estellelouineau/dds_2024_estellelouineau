"""kartoffel."""

__all__ = (
    "__version__",
    "hello_world"
    # Add functions and variables you want exposed in `kartoffel.` namespace here
    # this lists to the user what he will get when installing my package
)

__version__ = "0.1"
# version is defined in the command invite when running
# cruft create https://github.com/brightway-lca/cookiecutter-brightwaylib

from .printing import hello_world
# required to be able to add it to __all__
# one dot mean the function is in the same folder
# two dots means go back one folder, etc.
