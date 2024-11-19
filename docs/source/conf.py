# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'sagittal_average'
copyright = '2024, cansuoktem, zcabsjm, VanyMo'
author = 'cansuoktem, zcabsjm, VanyMo'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_rtd_theme",  # Using the Read the Docs theme
    # Removed "sphinx_github_pages" since it caused import errors
]

templates_path = ['_templates']
exclude_patterns = []

language = 'en'  # Changed to standard language code

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"  # Confirmed to use Read the Docs theme
html_static_path = ['_static']  # For custom CSS or static assets

# Optional: Add a custom title for the documentation
html_title = "SAGITTAL_AVERAGE Documentation"

# Optional: Add a favicon if desired
# html_favicon = "_static/favicon.ico"

# Optional: Custom sidebar logo
# html_logo = "_static/logo.png"

