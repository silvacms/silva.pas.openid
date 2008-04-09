# Copyright (c) 2008 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$

from zope.component import getUtility
from silva.pas.base.interfaces import IUserConverter
from silva.pas.openid.interfaces import IOpenIDAskUserInformation

from Products.Five import BrowserView

from zExceptions import Redirect

class StartOpenIDRegistration(BrowserView):

    def __call__(self):
        """Register a new user to use OpenID.
        """

        root = self.context.get_root()
            
        id = self.request.form.get('__ac_identity_register', '').strip()
        if not id:
            next_url = root.absolute_url() + '/silva_openid_register.html'
            raise Redirect, next_url

        self.request.form['__ac_identity_url'] = id # Re-inject the id

        smembers = root.service_members

        if smembers.is_user(id):
            # Authenticate
            # direct lookup ?
            root.acl_users.validate(self.request)
            return

        utility = getUtility(IUserConverter, name="openid")
        converter = utility()
        userid = converter.convert(id)
        members = root.Members
        members.manage_addProduct['Silva'].manage_addSimpleMember(userid)

        provider = IOpenIDAskUserInformation(self.request)
        provider.require('email')
        provider.optional('nickname')
        provider.optional('fullname')

        # Add some roles ?

        root.acl_users.validate(self.request)

        


