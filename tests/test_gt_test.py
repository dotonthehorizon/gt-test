#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_gt_test
----------------------------------

Tests for `gt_test` module.
"""

import unittest

import gt_test

from pytrends.request import TrendReq

class TestGt_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        assert(gt_test.__version__)

    def tearDown(self):
        pass
