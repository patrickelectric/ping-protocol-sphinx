# -*- coding: utf-8 -*-
import os
import sys
from datetime import date

# Global variables

SITE_URL = "https://patrickelectric.github.io/ping-protocol-sphinx/"
REPO_URL = "https://github.com/patrickelectric/ping-protocol-sphinx/"
REPO_NAME = "ping-protocol-sphinx"
PROJECT_NAME ="Ping Protocol Sphinx"

# Add the parent directory to the system path
#root_path = os.path.abspath(os.path.join("..", ".."))

#sys.path.insert(0, root_path)

# Project information
project = PROJECT_NAME
copyright = f"{date.today().year} - Blue Robotics Inc"
author = "Blue Robotics contributors"

# General configuration
extensions = [
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.githubpages",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "myst_parser",
    "sphinx_blue_robotics_theme",
    # "sphinx_blue_robotics_theme.extensions.extras",
    # "sphinx_blue_robotics_theme.extensions.python",
    # "sphinx_blue_robotics_theme.extensions.cpp",
    # "sphinx_blue_robotics_theme.extensions.lua",
]
master_doc = "index"
source_suffix = {'.rst': 'restructuredtext', '.md': 'restructuredtext'}
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Syntax highlighting
pygments_style = "sphinx"

# Substitutions
myst_substitutions = {
  "project_name": "Blue Robotics"
}

# External links
extlinks = {
    'issue': (REPO_URL + '/issues/%s', 'issue %s')
    }

# HTML output configuration
html_theme = "sphinx_blue_robotics_theme"
html_static_path = ["_static"]
html_theme_options = {
    "site_url": SITE_URL,
    "repo_url": REPO_URL,
    "repo_name": REPO_NAME,
    "icon": {
        "repo": "fontawesome/brands/github",
        "edit": "material/file-edit-outline",
    },
    "globaltoc_collapse": False,
    "edit_uri": "blob/master/docs/source",
        "features": [
        "navigation.sections",
        "navigation.megamenu",
        "navigation.top",
        "toc.follow",
        "toc.sticky",
        "content.tabs.link",
        "announce.dismiss",
    ],
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "toggle": {
                "icon": "octicons/moon-16",
                "name": "Switch to dark mode",
            }
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "toggle": {
                "icon": "octicons/sun-16",
                "name": "Switch to light mode",
            }
        },
    ],
    "toc_title_is_page_title": True,
}

html_last_updated_fmt = "%d %b %Y"
htmlhelp_basename = "BlueRoboticsDocumentationdoc"
html_baseurl = SITE_URL
html_context = {
    "homepage_url": "https://bluerobotics.com",
    "project_url": html_baseurl, 
    "project": project, 
    "exclude_comments": True
    }

# Myst Parser options
myst_enable_extensions = ["substitution", "colon_fence"]

# Autodoc configuration (Python documentation)
# autodoc2_packages = [
#     {
#         "path": "../../src/python",
#     },
# ]

# autodoc2_output_dir = "python_api"

# Breathe configuration (CPP documentation)
# breathe_projects = {"myproject": root_path + "/src/cpp/xml"}
# breathe_default_project = "myproject"

# Exhale configuration (CPP documentation)
# exhale_args = {
#     "containmentFolder":     "./cpp_api",
#     "rootFileName":          "library_root.rst",
#     "doxygenStripFromPath":  "..",
#     "rootFileTitle":         "CPP API reference",
#     "createTreeView":        True,
#     "exhaleExecutesDoxygen": True,
#     "exhaleDoxygenStdin":    """
#         INPUT       = ../../src/cpp
#         GENERATE_XML = YES
#         XML_OUTPUT  = ./xml
#     """,}

# sphinx-lua (Lua documentation)
# lua_source_path = [root_path + "/src/lua"]
# lua_source_encoding = 'utf8'
# lua_source_comment_prefix = '---'
# lua_source_use_emmy_lua_syntax = True
# lua_source_private_prefix = '_'
# lua_output_folder = "lua_api"
# lua_output_title = "Lua API reference"