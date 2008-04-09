

def atOpenIDSuccess(object, event):
    root = object.get_root()
    member = getattr(root.Members, event.userid)

    extra = event.result.extensionResponse('sreg', True)
    if extra.has_key('email'):
        member.set_email(extra['email'])
    if extra.has_key('fullname'):
        member.set_fullname(extra['fullname'])
    if extra.has_key('title'):
        member._title = extra['title']

