A Few Notes on this Fork
========================

I created this fork/branch so I could easily install Acrylamid with my custom filters and dependencies.

Some of my changes:

- Based on acrylamid 0.7.10. I changed the version number to 0.7.10a in setup.py so I could tell it from the main project.
- Requires `Pandoc <http://pandoc.org/>`_, the Markdown and RST filters were updated to use pandoc with the specific options that I like.
- Uses Jinja 2.8 + a custom Jinja filter I added to process steps in a series of articles.
- Has some hacky filters to insert <div>'s and bootstrap tabs where necessary.

Installation
------------

#. ``cd ~``

#. ``virtualenv acry``

#. ``source ~/acry/bin/activate``

#. ``pip install git+https://github.com/jacobhammons/acrylamid.git@develop#egg=acrylamid``

You can now ``cd`` into the root of any acrylamid project and run ``acrylamid aco``. The site is served at http://localhost:8000.

