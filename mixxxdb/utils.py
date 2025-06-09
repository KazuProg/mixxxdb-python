"""
Utility functions for Mixxx database path detection.
"""
import os
import platform
from pathlib import Path
from typing import Union, Optional


def get_mixxx_settings_dir() -> str:
    """
    Get the path to the Mixxx settings directory for the current platform.
    
    Returns:
        str: Path to Mixxx settings directory.
        
    Raises:
        OSError: If the operating system is not supported.
        ValueError: If required environment variables are not set.
    """
    system = platform.system()
    
    if system == "Windows":
        return _get_windows_settings_dir()
    elif system == "Darwin":  # macOS
        return _get_macos_settings_dir()
    elif system == "Linux":
        return _get_linux_settings_dir()
    else:
        raise OSError(f"Unsupported operating system: {system}")


def _get_windows_settings_dir() -> str:
    """Get Mixxx settings directory on Windows."""
    local_app_data = os.environ.get("LOCALAPPDATA")
    if local_app_data:
        return os.path.join(local_app_data, "Mixxx")
        
    user_profile = os.environ.get("USERPROFILE")
    if user_profile:
        return os.path.join(user_profile, "AppData", "Local", "Mixxx")
        
    raise ValueError("LOCALAPPDATA or USERPROFILE environment variable not set.")


def _get_macos_settings_dir() -> str:
    """Get Mixxx settings directory on macOS."""
    home_dir = os.path.expanduser("~")
    # Mixxx 2.3 and later (sandboxed)
    return os.path.join(
        home_dir,
        "Library", 
        "Containers",
        "org.mixxx.mixxx",
        "Data",
        "Library", 
        "Application Support",
        "Mixxx",
    )


def _get_linux_settings_dir() -> str:
    """Get Mixxx settings directory on Linux."""
    home_dir = os.path.expanduser("~")
    
    # Check for Flatpak installation first
    flatpak_path = os.path.join(home_dir, ".var", "app", "org.mixxx.Mixxx", ".mixxx")
    if os.path.exists(os.path.join(home_dir, ".var")):
        return flatpak_path
        
    # Default installation
    return os.path.join(home_dir, ".mixxx")


def get_mixxx_db_path(settings_dir: Optional[Union[str, Path]] = None) -> str:
    """
    Get the default path to the Mixxx database file.
    
    Args:
        settings_dir: Custom settings directory. If None, uses platform default.
        
    Returns:
        str: Path to mixxxdb.sqlite file.
    """
    if settings_dir is None:
        settings_dir = get_mixxx_settings_dir()
        
    return os.path.join(str(settings_dir), "mixxxdb.sqlite")


def verify_mixxx_db_exists(db_path: Optional[Union[str, Path]] = None) -> bool:
    """
    Verify that the Mixxx database file exists.
    
    Args:
        db_path: Path to database file. If None, uses default location.
        
    Returns:
        bool: True if database file exists, False otherwise.
    """
    if db_path is None:
        db_path = get_mixxx_db_path()
        
    return Path(db_path).exists()
