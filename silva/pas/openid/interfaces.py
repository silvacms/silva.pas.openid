# Copyright (c) 2008 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$

from zope.interface import Interface
from Products.PluggableAuthService.interfaces.plugins import IExtractionPlugin

class IOpenIdExtractionPlugin(IExtractionPlugin):
    """Extract OpenID credential information from a request.
    """

    def initiateAuthentication(identity_url, return_to=None):
        """Initiate the OpenID authentication.
        """


    def extractCredentials(request):
        """ request -> { 'openid.identity' : identity,
                         'openid.assoc_handle' : assoc_handle,
                         'openid.return_to' : return_to,
                         'openid.signed' : signed,
                         'openid.sig' : sig,
                         'openid.invalidate_handle' : invalidate_handle,
                        }
        """


class IOpenIDAware(Interface):
    """Marker to let known that service_members is OpenID Aware.
    """

class IOpenIDAskUserInformation(Interface):
    """Let ask some information to the OpenID provider.
    """

    def require(name):
        """Require name from the provider.
        """

    def optional(name):
        """Ask optionally name to the provider.
        """


class IOpenIDAskedUserInformation(Interface):
    """Let OpenID plugin known which information have been asked.
    """

    def require():
        """Return a list of required information.
        """

    def optional():
        """Return a list of optional information.
        """
