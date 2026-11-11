"""Exact source snapshots with native copy-on-write when the filesystem supports it."""
from pathlib import Path
import ctypes
import errno
import os
import shutil
import sys


def copy_original(source, destination):
    source, destination = Path(source), Path(destination)
    if destination.exists():
        raise FileExistsError('snapshot_destination_exists')
    if sys.platform == 'darwin':
        clone = ctypes.CDLL(None, use_errno=True).clonefile
        clone.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint32]
        clone.restype = ctypes.c_int
        # CLONE_NOFOLLOW: a final source alias cannot be substituted after validation.
        if clone(os.fsencode(source), os.fsencode(destination), 1) == 0:
            return 'apfs_clone_exact_bytes'
        error = ctypes.get_errno()
        if error not in {errno.EXDEV, errno.ENOTSUP, errno.EINVAL}:
            raise OSError(error, os.strerror(error), str(source))
    if source.stat().st_size > shutil.disk_usage(destination.parent).free:
        raise OSError(errno.ENOSPC, 'insufficient_space_for_exact_snapshot', str(destination))
    shutil.copyfile(source, destination)
    return 'exact_byte_copy'
