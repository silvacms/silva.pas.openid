# Copyright (c) 2008 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$

from AccessControl.Permissions import manage_users as ManageUsers
from Products.PluggableAuthService.PluggableAuthService import registerMultiPlugin
from Products.Silva.ExtensionRegistry import extensionRegistry

from plugins import oid
registerMultiPlugin(oid.OpenIdPlugin.meta_type)

import install

def initialize(context):
    extensionRegistry.register(
        'silva.pas.openid', 'Silva OpenID Support', context, [],
        install, depends_on='silva.pas.base')

    context.registerClass(oid.OpenIdPlugin,
                          permission=ManageUsers,
                          constructors=
                          (oid.manage_addOpenIdPlugin,
                           oid.addOpenIdPlugin),
                          visibility=None,
                          icon="www/openid.png")

