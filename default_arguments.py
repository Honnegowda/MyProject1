#demonstrate the default arguments in python

def make_email(fn,ln, domain=None):
    if domain is None:
        domain = "zeomega"
    email = "@".join([".".join([fn, ln]), ".".join([domain, 'com'])])
    return email
fn = 'honne'
ln = 'gowda'
print make_email(fn, ln)

