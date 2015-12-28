# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division
import time
import gevent
from ivr.common.exception import IVRError
from ivr.ivc.manager.session import UserSession


class UserSession(UserSession):
    pass


class UserSessionDAO(object):

    model_cls = UserSession

    def __init__(self):
        self._sessions = []

    def add_new_user_session(self, *args, **kwargs):
        session = UserSession(*args, **kwargs)
        self._sessions.append(session)
        return session

    def add_user_session(self, session):
        self._sessions.append(session)

    def get_user_session_count(self, project_name=None, camera_id=None):
        cnt = 0
        for s in self._sessions:
            if (project_name is None or (project_name == s.project_name)) \
                    and (camera_id is None or (camera_id == s.camera_id)):
                cnt += 1
        return cnt

    def get_timeout_user_session_list(self, last_keepalive, project_name=None, camera_id=None, start=0, limit=20):
        session_list = []
        index = 0
        for s in self._sessions:
            if (project_name is None or (project_name == s.project_name)) \
                    and (camera_id is None or (camera_id == s.camera_id)) \
                    and (s.end is not None and (s.last_keepalive < last_keepalive)):
                if index >= start:
                    session_list.append(s)
                index += 1
                if index >= start+limit:
                    break
        return session_list


    def get_user_session_list(self, project_name=None, camera_id=None, start=0, limit=20, running=True):
        session_list = []
        index = 0
        if limit == 0:
            return session_list
        for s in self._sessions:
            if (project_name is None or (project_name == s.project_name)) \
                    and (camera_id is None or (camera_id == s.camera_id)) \
                    and (running is None or (running is True and s.end is None) or (running is False and s.end is not None)):
                if index >= start:
                    session_list.append(s)
                index += 1
                if index >= start+limit:
                    break
        return session_list

    def get_user_session(self, project_name, session_id):
        for session in self._sessions:
            if session.project_name == project_name and session.session_id == session_id:
                return session

    def update_user_session(self, project_name, session):
        for i, s in enumerate(self._sessions):
            if s.project_name == session.project_name and s.session_id == session.session_id:
                if session.end is None:
                    self._sessions[i] = session
                else:
                    self._sessions.pop(i)
                return
        raise IVRError("{0} not found".format(session))