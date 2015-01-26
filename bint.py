# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_bint', [dirname(__file__)])
        except ImportError:
            import _bint
            return _bint
        if fp is not None:
            try:
                _mod = imp.load_module('_bint', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _bint = swig_import_helper()
    del swig_import_helper
else:
    import _bint
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _bint.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _bint.SwigPyIterator_value(self)
    def incr(self, n=1): return _bint.SwigPyIterator_incr(self, n)
    def decr(self, n=1): return _bint.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _bint.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _bint.SwigPyIterator_equal(self, *args)
    def copy(self): return _bint.SwigPyIterator_copy(self)
    def next(self): return _bint.SwigPyIterator_next(self)
    def __next__(self): return _bint.SwigPyIterator___next__(self)
    def previous(self): return _bint.SwigPyIterator_previous(self)
    def advance(self, *args): return _bint.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _bint.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _bint.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _bint.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _bint.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _bint.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _bint.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _bint.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class bint(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, bint, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, bint, name)
    def __str__(self): return _bint.bint___str__(self)
    def __repr__(self): return _bint.bint___repr__(self)
    def toString(self): return _bint.bint_toString(self)
    def __init__(self, *args): 
        this = _bint.new_bint(*args)
        try: self.this.append(this)
        except: self.this = this
    def st(self): return _bint.bint_st(self)
    def read(self, *args): return _bint.bint_read(self, *args)
    def write(self, *args): return _bint.bint_write(self, *args)
    def readbin(self, *args): return _bint.bint_readbin(self, *args)
    def writebin(self, *args): return _bint.bint_writebin(self, *args)
    def __eq__(self, *args): return _bint.bint___eq__(self, *args)
    def __ne__(self, *args): return _bint.bint___ne__(self, *args)
    def __lt__(self, *args): return _bint.bint___lt__(self, *args)
    def __gt__(self, *args): return _bint.bint___gt__(self, *args)
    def __le__(self, *args): return _bint.bint___le__(self, *args)
    def __ge__(self, *args): return _bint.bint___ge__(self, *args)
    def __add__(self, *args): return _bint.bint___add__(self, *args)
    def __sub__(self, *args): return _bint.bint___sub__(self, *args)
    def __mul__(self, *args): return _bint.bint___mul__(self, *args)
    def __div__(self, *args): return _bint.bint___div__(self, *args)
    def __mod__(self, *args): return _bint.bint___mod__(self, *args)
    def __xor__(self, *args): return _bint.bint___xor__(self, *args)
    def powmod(self, *args): return _bint.bint_powmod(self, *args)
    def __iadd__(self, *args): return _bint.bint___iadd__(self, *args)
    def __isub__(self, *args): return _bint.bint___isub__(self, *args)
    def __imul__(self, *args): return _bint.bint___imul__(self, *args)
    def __idiv__(self, *args): return _bint.bint___idiv__(self, *args)
    def __imod__(self, *args): return _bint.bint___imod__(self, *args)
    def __ixor__(self, *args): return _bint.bint___ixor__(self, *args)
    def __neg__(self): return _bint.bint___neg__(self)
    __swig_destroy__ = _bint.delete_bint
    __del__ = lambda self : None;
bint_swigregister = _bint.bint_swigregister
bint_swigregister(bint)

def _out(*args):
  return _bint._out(*args)
_out = _bint._out

def _in(*args):
  return _bint._in(*args)
_in = _bint._in

# This file is compatible with both classic and new-style classes.


