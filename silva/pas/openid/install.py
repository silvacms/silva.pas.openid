# Copyright (c) 2008 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$

from Products.Silva.install import add_fss_directory_view, add_helper, zpt_add_helper
from zope.interface import alsoProvides, noLongerProvides
from silva.pas.base.interfaces import IPASMemberService
from interfaces import IOpenIDAware

def install(root):
    """Installation method for OpenID support
    """
    assert IPASMemberService.providedBy(root.service_members)

    # Change the login page to get a OpenID field
    add_helper(root, 'silva_login_form.html', globals(), zpt_add_helper, 0)
    
    # Register PAS plugins
    registerPASPlugin(root.acl_users)

    alsoProvides(root.service_members, IOpenIDAware)
    
    
def uninstall(root):
    assert IPASMemberService.providedBy(root.service_members)
    # FIXME: We should restore the previous login page
    noLongerProvides(root.service_members, IOpenIDAware)
    
def is_installed(root):
    return IOpenIDAware.providedBy(root.service_members)

def registerViews(reg):
    """Register core views on registry.
    """
    pass

def unregisterViews(reg):
    """Unregister core views on registry.
    """
    pass

def registerPASPlugin(pas):
    # FIXME: TODO
    pass

if __name__ == '__main__':
    print """This module is not an installer. You don't have to run it."""
