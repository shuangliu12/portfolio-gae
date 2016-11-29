#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import webapp2
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader('templates')
  )

class BaseHandler(webapp2.RequestHandler):
  def get(self):
  	vars = {'title': 'Home'}
  	template = JINJA_ENVIRONMENT.get_template("base.html")
  	self.response.out.write(template.render(vars))

class IconsHandler(webapp2.RequestHandler):
  def get(self):
  	vars = {'title': 'Icons'}
  	template = JINJA_ENVIRONMENT.get_template("icons.html")
  	self.response.out.write(template.render(vars))

class IllustrationsHandler(webapp2.RequestHandler):
  def get(self):
  	vars = {'title': 'Illustrations'}
  	template = JINJA_ENVIRONMENT.get_template("illustrations.html")
  	self.response.out.write(template.render(vars))

class PaintingsHandler(webapp2.RequestHandler):
  def get(self):
  	vars = {'title': 'Paintings'}
  	template = JINJA_ENVIRONMENT.get_template("paintings.html")
  	self.response.out.write(template.render(vars))

app = webapp2.WSGIApplication([
  ('/', BaseHandler),
  ('/icons', IconsHandler),
  ('/illustrations', IllustrationsHandler),
  ('/paintings', PaintingsHandler)
], debug=True)
