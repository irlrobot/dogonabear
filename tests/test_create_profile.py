#!/usr/bin/env python
from dogonabear.create_profile import handler

def test_update_profile_handler():
  event = {}
  context = {}
  expected = {
    'body': '{"output": "Profile Created"}',
    'headers': {
      'Content-Type': 'application/json'
    },
    'statusCode': 200
  }

  assert handler(event, context) == expected
