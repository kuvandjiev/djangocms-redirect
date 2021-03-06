#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from tempfile import mkdtemp

HELPER_SETTINGS = dict(
    INSTALLED_APPS=[
        'djangocms_redirect',
    ],
    FILE_UPLOAD_TEMP_DIR=mkdtemp(),

    MIDDLEWARE_CLASSES=[
        'djangocms_redirect.middleware.RedirectMiddleware',
    ],
    CACHES={
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        }
    }
)


def run():
    from djangocms_helper import runner
    runner.cms('djangocms_redirect')


def setup():
    import sys
    from djangocms_helper import runner
    runner.setup('djangocms_redirect', sys.modules[__name__], use_cms=True)


if __name__ == '__main__':
    run()
