class Employee(object):
    def  __init__(self, fn, ln):
        self._fn =  fn
        self._ln  = ln
    
    @property
    def _email(self):
        return  self._fn+"."+self._ln+"@zeomega.com"

    @_email.setter
    def _email(self, value):
        fn_ln_li = value.split("@")[0].split('.')
        self._fn = fn_ln_li[0]
        self._ln = fn_ln_li[1]

    def __str__(self):
        st  = "Employee({}, {}, {})".format(self._fn, self._ln, self._email)
        return  st


if __name__ == "__main__":
    fn, ln = "Honne", "Gowda"
    emp1 = Employee(fn, ln)
    emp1._email=  "Manje.Gowda@zeomega.com"
    print emp1
