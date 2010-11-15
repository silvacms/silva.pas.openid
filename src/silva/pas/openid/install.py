# Copyright (c) 2008 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$

from zope.interface import alsoProvides, noLongerProvides

from Products.PluggableAuthService.interfaces import plugins
from Products.Silva.install import add_helper, zpt_add_helper
from silva.pas.base.interfaces import IPASMemberService
from silva.pas.openid.interfaces import IOpenIDAware


def install(root):
    """Installation method for OpenID support
    """
    assert IPASMemberService.providedBy(root.service_members)

    # Change the login page to get a OpenID field
    add_helper(root, 'silva_login_form.html', globals(), zpt_add_helper, 0)
    # Add a OpenID registration page
    add_helper(root, 'silva_openid_register.html', globals(), zpt_add_helper, 0)

    # Register PAS plugins
    registerPASPlugins(root.acl_users)

    # Register views
    registerViews(root.service_view_registry)

    alsoProvides(root.service_members, IOpenIDAware)


def uninstall(root):
    """Uninstall OpenID support
    """
    assert IPASMemberService.providedBy(root.service_members)
    # FIXME: We should restore the previous login page

    unregisterPASPlugins(root.acl_users)

    # Remove views
    unregisterViews(root.service_view_registry)

    # We remove the registration page.
    root.manage_delObjects(['silva_openid_register.html',])
    noLongerProvides(root.service_members, IOpenIDAware)

def is_installed(root):
    return IOpenIDAware.providedBy(root.service_members)


def registerPASPlugins(pas):
    """Register new PAS plugins.
    """
    plugin_ids = pas.objectIds()
    if 'session' not in plugin_ids:
        pas.manage_addProduct['plone.session'].manage_addSessionPlugin('session')
    if 'openid' not in plugin_ids:
        pas.manage_addProduct['silva.pas.openid'].manage_addOpenIDPlugin('openid')
    if 'members' not in plugin_ids:
        pas.manage_addProduct['silva.pas.membership'].manage_addMembershipPlugin('members')

    def registerPluginIfNew(ptype, pid):
        if pid not in pas.plugins.listPluginIds(ptype):
            pas.plugins.activatePlugin(ptype, pid)

    registerPluginIfNew(plugins.IExtractionPlugin, 'session')
    registerPluginIfNew(plugins.IAuthenticationPlugin, 'session')
    registerPluginIfNew(plugins.ICredentialsResetPlugin, 'session')
    registerPluginIfNew(plugins.ICredentialsUpdatePlugin, 'session')

    registerPluginIfNew(plugins.IExtractionPlugin, 'openid')
    registerPluginIfNew(plugins.IAuthenticationPlugin, 'openid')

    registerPluginIfNew(plugins.IUserEnumerationPlugin, 'members')


def registerViews(reg):
    """Register Views.
    """
    reg.register('edit', 'Silva OpenID Member',
                 ['edit', 'Member', 'SimpleMember'])


def unregisterViews(reg):
    """Unregister Views.
    """
    reg.unregister('edit', 'Silva OpenID Member')


def unregisterPASPlugins(pas):
    """Remove PAS plugins.
    """
    pas.manage_delObjects(['session', 'openid', 'members',])


if __name__ == '__main__':
    print """This module is not an installer. You don't have to run it."""
