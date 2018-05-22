#!/usr/bin/env python
from dogonabear.update_profile import handler

def test_update_profile_handler():
  event = {}
  context = {}
  expected = {
    'body': '{"output": "Profile Updated!"}',
    'headers': {
      'Content-Type': 'application/json'
    },
    'statusCode': 200
  }

  assert handler(event, context) == expected
