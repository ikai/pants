# coding=utf-8
# Copyright 2014 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import (nested_scopes, generators, division, absolute_import, with_statement,
                        print_function, unicode_literals)

from pants_test.pants_run_integration_test import PantsRunIntegrationTest

class TestScalaLibraryIntegrationTest(PantsRunIntegrationTest):

  def test_bundle(self):
        pants_run = self.run_pants(['goal', 'test', 'src/scala/com/pants/testproject/javasources/BUILD:javasources'])
        self.assertEquals(pants_run.returncode, self.PANTS_SUCCESS_CODE)