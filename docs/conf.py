import os
import shutil
import sys

sys.path.insert(0, os.path.abspath("../src"))
project = "Whist Game Backend"
copyright = "2023, Daniel Naylor"
author = "Daniel Naylor"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx_rtd_theme",
    "sphinx_autodoc_typehints",
    "sphinx.ext.coverage",
    "sphinx.ext.viewcode",
    "myst_parser",
]

templates_path = ["_templates"]
# exclude_patterns = []
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": True,
}
always_document_param_types = True
shutil.copyfile("../CHANGELOG.md", "../docs/changelog.md")

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
