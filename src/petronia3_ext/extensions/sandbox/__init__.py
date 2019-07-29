
"""
Handles running extensions inside a sandbox, which runs outside the primary
Petronia memory space with OS specific constraints.
"""

from .module_loader import create_sandbox_module_loader
