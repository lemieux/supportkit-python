# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import jwt


def generate(body, secret, key_id):
    return jwt.encode(body, secret, algorithm='HS256', headers={'kid': key_id})
