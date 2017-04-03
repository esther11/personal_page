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
import os
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(loader = jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"))

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	title = "HOME"
    	template_vars = {"title": title, 'name':'index'}
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_vars))

class resumeHandler(webapp2.RequestHandler):
    def get(self):
    	title = "RESUME"
    	template_vars = {"title": title, 'name':'resume'}
        template = JINJA_ENVIRONMENT.get_template('resume.html')
        self.response.write(template.render(template_vars))

class skillsHandler(webapp2.RequestHandler):
    def get(self):
    	title = "SKILLS"
    	template_vars = {"title": title, 'name':'skills'}
        template = JINJA_ENVIRONMENT.get_template('skills.html')
        self.response.write(template.render(template_vars))

class doodlesHandler(webapp2.RequestHandler):
    def get(self):
    	title = "DOODLES"
    	template_vars = {"title": title, 'name':'doodles'}
        template = JINJA_ENVIRONMENT.get_template('doodles.html')
        self.response.write(template.render(template_vars))

class contactHandler(webapp2.RequestHandler):
    def get(self):
    	title = "CONTACT"
    	template_vars = {"title": title}
        template = JINJA_ENVIRONMENT.get_template('contact.html')
        self.response.write(template.render(template_vars))

class redirectHandler(webapp2.RequestHandler):
    def get(self):
    	self.redirect('/')


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/resume.html', resumeHandler),
    ('/skills.html', skillsHandler),
    ('/doodles.html', doodlesHandler),
    ('/contact.html', contactHandler),
    ('/.*', redirectHandler)
], debug=True)
