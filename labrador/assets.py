# -*- coding: utf-8 -*-
"""Application assets."""
from flask_assets import Bundle, Environment
import os

print()
root = os.path.abspath(os.path.dirname(__file__))
css = Bundle(
    os.path.join(root, 'static', 'scss/theme.scss',
    filters='scss',
    output='css/common.css',
    depends='scss/*.scss'
)

js=Bundle(
    'libs/jQuery/dist/jquery.js',
    'libs/materialize/bin/materialize.js',
    'libs/jquery-touchswipe/jquery.touchSwipe.js',
    'js/script.js',
    filters='jsmin',
    output='js/common.js'
)

assets=Environment()

assets.register('js_all', js)
assets.register('css_all', css)
