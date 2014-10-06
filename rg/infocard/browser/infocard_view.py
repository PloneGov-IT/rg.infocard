# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from plone import api
from plone.memoize.view import memoize


class View(BrowserView):
    ''' Custom view and methods for infocard
    '''
    @property
    @memoize
    def public_infos(self):
        ''' Return all the infos that are public
        '''
        return [
            info for info in self.context.default_args
            if info['arg_public']
        ]

    @property
    @memoize
    def private_infos(self):
        ''' Return all the infos that are public
        '''
        return [
            info for info in self.context.default_args
            if not info['arg_public']
        ]

    @property
    @memoize
    def allowed_infos(self):
        ''' Return all the infos that are public
        '''
        if api.user.is_anonymous():
            return self.public_infos
        else:
            return self.private_infos

    @property
    @memoize
    def searched_text(self):
        ''' The text searched
        '''
        parts = [
            self.title,
            self.description
        ]
        parts.extend([
            x['arg_value'] for x in self.allowed_infos
        ])
        return u" ".join(parts)
