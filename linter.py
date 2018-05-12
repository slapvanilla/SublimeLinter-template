#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Adapted by slapvanilla
# Copyright (c) 2018 slapvanilla
#
# License: MIT
#

"""This module exports the fasterer plugin class."""

from SublimeLinter.lint import RubyLinter  # or NodeLinter, PythonLinter, ComposerLinter, RubyLinter

class Fasterer(RubyLinter):
  """Provides an interface to fasterer."""

  syntax = (
      'better rspec',
      'betterruby',
      'cucumber steps',
      'rspec',
      'ruby experimental',
      'ruby on rails',
      'ruby'
  )
  cmd = 'ruby -S fasterer'
  # Using each_with_index is slower than while loop. Occurred at lines: 1469.
  regex = r'^(?P<message>.+). Occurred at lines: (?P<line>\d+)'
  tempfile_suffix = 'rb'

  # Versioning
  version_args = '-S gem list | grep fasterer'
  version_re = r'fasterer \((?P<version>\d+\.\d+\.\d+)\)'
  version_requirement = '>= 0.4.1'

  # config_file = ('-c', '.fasterer.yml')

  # Other Options
  multiline = False
