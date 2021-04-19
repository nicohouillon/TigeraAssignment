import os
import unittest
import requests
import pytest
from nose.tools import assert_true


from flask import Flask
from app import app
from fetch import get_name, get_joke
from flask_testing import TestCase


class MyTest(unittest.TestCase):

    def get_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        # Default port is 5000
        app.config['LIVESERVER_PORT'] = 5000
        # Default timeout is 5 seconds
        app.config['LIVESERVER_TIMEOUT'] = 10
        return app

    def test_app_200(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.data, '')

def test_name_200():
  resp = requests.get('https://api.namefake.com/')
  assert_true(resp.ok)

 
def test_joke_200():
  resp = requests.get('http://api.icndb.com/jokes')
  assert_true(resp.ok)

def test_joke_with_parameters():
  firstName = "John"
  lastName = "Doe"
  test = get_joke(firstName,lastName)
  assert info is not None
  assert username == test['info']['joke']


if __name__ == "__main__":
  unittest.main()