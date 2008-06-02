Copyright (c) 2008, Infrae. All rights reserved.
See also LICENSE.txt

OpenID Support for Silva
------------------------

This extension provide a full support for OpenID in Silva. This rely
on PluggableAuthService and ``silva.pas.base``. 

After installing the extension, users would be able to logon on Silva
using an OpenID identity. First, users will have to register, with an
form protected by a captcha. This registration step are going to fetch
available information about the user from the OpenID provider. After
registration, site managers can attributes roles to users, and check
information about them on theirs Silva member objects.

This extension require at least `Silva`_ 2.1a or higher.

Installation
------------

If you installed Silva using buildout, by getting one from the `Infrae
SVN`_ repository, or creating one using `Paster`_, you should edit your
buildout configuration file ``buildout.cfg`` to add or edit the
following section::

  [instance]

  eggs = ... 
        silva.pas.openid

  zcml = ...
        silva.pas.openid

If the section ``instance`` wasn't already in the configuration file,
pay attention to re-copy values for ``eggs`` and ``zcml`` from the
profile you use.

After you can restart buildout::

  $ ./bin/buildout


If you don't use buildout, you can install this extension using
``easy_install``, and after create a file called
``silva.pas.openid-configure.zcml`` in the
``/path/to/instance/etc/package-includes`` directory.  This file will
responsible to load the extension and should only contain this::

  <include package="silva.pas.openid" />


Latest version
--------------

The latest version is available in a `Subversion repository
<https://svn.infrae.com/silva.pas.openid/trunk#egg=silva.pas.openid-dev>`_.


.. _Infrae SVN: https://svn.infrae.com/buildout/silva/
.. _Paster: https://svn.infrae.com/buildout/silva/INSTALL.txt
.. _Silva: http://infrae.com/products/silva


Credits
-------
Silva's OpenID integration was sponsored by Marc Petitmermet, who's at the 
Department of Materials at ETH Zurich (http://www.mat.ethz.ch/ but it was 
funded from another source). 
