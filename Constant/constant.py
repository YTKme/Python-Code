"""Constant Module

This module implements constant(s) to be used.
"""

import platform


PLATFORM_SYSTEM = platform.system()
PLATFORM_PROCESSOR = platform.processor()

IS_LINUX = PLATFORM_SYSTEM == 'Linux'
IS_MAC_X64 = PLATFORM_SYSTEM == 'Darwin' and PLATFORM_PROCESSOR == 'i386'
IS_MAC_ARM = PLATFORM_SYSTEM == 'Darwin' and PLATFORM_PROCESSOR == 'arm'
IS_MAC = IS_MAC_X64 or IS_MAC_ARM
IS_WINDOW = PLATFORM_SYSTEM = 'Windows'
