#!/usr/bin/env python
from dogonabear.get_matches import handler

def test_get_matches_handler():
  event = {}
  context = {}
  expected = {
    'body': '{"output": "Your Matches"}',
    'headers': {
      'Content-Type': 'application/json'
    },
    'statusCode': 200
  }

  assert handler(event, context) == expected
