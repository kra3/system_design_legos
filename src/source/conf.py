# -*- coding: utf-8 -*-

from datetime import datetime


project = 'System Design Legos'
copyright = '{:d}, Arun Karunagath'.format(datetime.now().year)
author = 'Arun Karunagath'

version = ''
release = '0.0.1'

extensions = [
    'sphinx.ext.githubpages',
    'sphinxcontrib.blockdiag',
]

templates_path = ['templates']
source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = []
pygments_style = 'sphinx'

html_theme = 'alabaster'

# html_theme_options = {}
html_theme_options = {
    'description': "A system design exercise",
    'github_user': 'kra3',
    'github_repo': 'system_design_legos',
    'fixed_sidebar': True,
    'show_powered_by': False,
    'show_related': True
}

html_static_path = ['static']

# html_sidebars = {}
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
    ]
}

htmlhelp_basename = 'system_design_legos'

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '12pt',
    # 'preamble': '',
    # 'figure_align': 'htbp',
}

latex_documents = [
    (master_doc, 'system_design_legos.tex', 'System Design Legos',
     'Arun Karunagath', 'manual'),
]

man_pages = [
    (master_doc, 'system_design_legos', 'System Design Legos',
     [author], 1)
]

texinfo_documents = [
    (master_doc, 'system_design_legos', 'System Design Legos',
     author, 'system_design_legos', 'A system design exercise.',
     'Miscellaneous'),
]
