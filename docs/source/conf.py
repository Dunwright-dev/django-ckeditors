# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.insert(0, os.path.abspath(".."))

__version__ = "0.2.4"

project = "Django CKEditors"
project_copyright = "2024, Mark Sevelj"
author = "Mark Sevelj"
release = __version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx_copybutton",
    "sphinx_inline_tabs",
    "sphinx.ext.todo",
]

templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "build", "Thumbs.db", ".DS_Store"]

pygments_style = "monokai"
pygments_dark_style = "monokai"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]

# sphinx-copybutton is a lightweight code-block copy button
# config options are here https://sphinx-copybutton.readthedocs.io/en/latest/
# This config removes Python Repl + continuation, Bash line prefixes,
# ipython and qtconsole + continuation, jupyter-console + continuation and
# preceding line numbers
copybutton_prompt_text = (
    r"^\d{1,4}|^.\d{1,4}|>>> |\s{2,6}|\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}:"
)
copybutton_prompt_is_regexp = True

"""
# detailed download-url
# http://www.tldp.org/LDP/Bash-Beginners-Guide/Bash-Beginners-Guide.pdf \
# --dataset . \
# -m "add beginners guide on bash" \
# -O books/bash_guide.pdf
# is correctly pasted with the following setting
"""
copybutton_line_continuation_character = "\\"
