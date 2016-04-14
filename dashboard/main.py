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
import base64
import json
import logging
import urllib

import webapp2
from google.appengine.api import memcache


# class MainHandler(webapp2.RequestHandler):
#     def get(self):
#         index_html = open('client/main.html').read()
#         self.response.out.write(index_html)


class GetTeams(webapp2.RequestHandler):
    def get(self):
        teams = memcache.get(key='teams')
        if teams is None:
            teams = []
        else:
            teams = teams.split(',')

        teams = memcache.get_multi(keys=teams, namespace='team')
        self.response.out.write("[" + ','.join(
            '{{\"key\":\"{0}\",\"value\":{1}}}'.format(k[1], teams[k[1]]) for k in enumerate(teams)) + "]")


class GetUsers(webapp2.RequestHandler):
    def get(self):
        users = memcache.get(key='users')
        if users is None:
            users = []
        else:
            users = users.split(',')

        users = memcache.get_multi(keys=users, namespace='user')
        self.response.out.write("[" + ','.join(
            '{{\"key\":\"{0}\",\"value\":{1}}}'.format(k[1], users[k[1]]) for k in enumerate(users)) + "]")


class SetTeam(webapp2.RequestHandler):
    def post(self):
        # logging.debug(self.request.body);
        message = json.loads(urllib.unquote(self.request.body).rstrip('='))
        message_body = base64.b64decode(str(message['message']['data']))
        messageData = json.loads(message_body)

        teams = memcache.get(key='teams')
        if teams is None:
            teams = []
        else:
            teams = teams.split(',')
        team = messageData['name']
        if team not in teams:
            teams.append(team)
        memcache.set(key='teams', value=','.join(teams))
        memcache.set(key=team, value=messageData['value'], namespace='team')

        self.response.status = 204


class SetUser(webapp2.RequestHandler):
    def post(self):
        # logging.debug(self.request.body);
        message = json.loads(urllib.unquote(self.request.body).rstrip('='))
        message_body = base64.b64decode(str(message['message']['data']))
        messageData = json.loads(message_body)

        users = memcache.get(key='users')
        if users is None:
            users = []
        else:
            users = users.split(',')
        user = messageData['name']
        if user not in users:
            users.append(user)
        memcache.set(key='users', value=','.join(users))
        memcache.set(key=user, value=messageData['value'], namespace='user')

        self.response.status = 204


app = webapp2.WSGIApplication([
    # ('/', MainHandler),
    ('/api/getTeams', GetTeams),
    ('/api/getUsers', GetUsers),
    ('/api/setTeam', SetTeam),
    ('/api/setUser', SetUser)
], debug=True)
