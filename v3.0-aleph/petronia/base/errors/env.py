
"""
Environmental issues that cause problems.  These mostly occur just during
bootstrap time.
"""


from .base import PetroniaError


class PetroniaEnvironmentError(PetroniaError):
    """
    Base class for errors related to the environment.
    """


class PetroniaFileSystemError(PetroniaEnvironmentError):
    """
    A problem with the file system.  General Python I/O errors should continue
    to be thrown as the original Python error, rather than masked as one of
    these.
    """

class PetroniaFileError(PetroniaFileSystemError):
    """
    There was a problem with a file or directory.
    """
    def __init__(self, filename: str, msg: str) -> None:
        PetroniaFileSystemError.__init__(self, '{0}: {1}'.format(filename, msg))


class PetroniaPlatformNotSupported(PetroniaEnvironmentError):
    """
    Petronia doesn't support this OS + processor combination.
    """
    def __init__(self, name: str) -> None:
        PetroniaEnvironmentError.__init__(
            self,
            ('Petronia does not support {0}.  '
            'Please reach out to the Petronia team if you want to help '
            'supporting your platform.').format(name)
        )
