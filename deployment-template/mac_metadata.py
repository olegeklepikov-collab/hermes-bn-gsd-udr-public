"""macOS extended attributes through its native read-only interface."""
import ctypes,hashlib,os
lib=ctypes.CDLL('/usr/lib/libSystem.B.dylib',use_errno=True)
lib.listxattr.argtypes=[ctypes.c_char_p,ctypes.c_void_p,ctypes.c_size_t,ctypes.c_int]
lib.listxattr.restype=ctypes.c_ssize_t
lib.getxattr.argtypes=[ctypes.c_char_p,ctypes.c_char_p,ctypes.c_void_p,ctypes.c_size_t,ctypes.c_uint32,ctypes.c_int]
lib.getxattr.restype=ctypes.c_ssize_t
lib.removexattr.argtypes=[ctypes.c_char_p,ctypes.c_char_p,ctypes.c_int]
lib.removexattr.restype=ctypes.c_int
def hashes(path):
    raw=os.fsencode(path);size=lib.listxattr(raw,None,0,1)
    if size<0:raise OSError(ctypes.get_errno(),str(path))
    if not size:return {}
    buf=ctypes.create_string_buffer(size)
    count=lib.listxattr(raw,buf,size,1)
    if count!=size:raise OSError('Extended attributes changed while reading: '+str(path))
    result={}
    for key in buf.raw.split(b'\0'):
        if not key:continue
        n=lib.getxattr(raw,key,None,0,0,1)
        if n<0:raise OSError(ctypes.get_errno(),str(path))
        value=ctypes.create_string_buffer(n)
        got=lib.getxattr(raw,key,value,n,0,1)
        if got!=n:raise OSError('Extended attribute changed while reading: '+str(path))
        result[os.fsdecode(key)]=hashlib.sha256(value.raw).hexdigest()
    return result
def remove_extra_attributes(path,expected):
    for name in set(hashes(path))-set(expected):
        if lib.removexattr(os.fsencode(path),os.fsencode(name),1):raise OSError(ctypes.get_errno(),str(path))
