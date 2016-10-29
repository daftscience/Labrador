# -*- coding: utf-8 -*-
"""Application assets."""
from flask_assets import Bundle, Environment

css = Bundle(
    'scss/theme.scss',
    filters='sass',
    output='js/common.css'
)

js = Bundle(
    'libs/jQuery/dist/jquery.js',
    'libs/materialize/bin/materialize.js',
    'libs/jquery-touchswipe/jquery.touchSwipe.js',
    'js/script.js',
    filters='jsmin',
    output='js/common.js'
)

assets = Environment()

assets.register('js_all', js)
assets.register('css_all', css)
