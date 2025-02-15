import os
import platform


def get_mixxx_settings_dir():
    """Gets the path to the Mixxx settings directory, platform-specifically."""
    system = platform.system()
    if system == "Windows":
        local_app_data = os.environ.get("LOCALAPPDATA")
        if local_app_data:
            return os.path.join(local_app_data, "Mixxx")
        else:
            user_profile = os.environ.get("USERPROFILE")
            if user_profile:
                return os.path.join(user_profile, "AppData", "Local", "Mixxx")
            else:
                raise ValueError(
                    "LOCALAPPDATA or USERPROFILE environment variable not set."
                )
    elif system == "Darwin":  # macOS
        home_dir = os.path.expanduser("~")
        return os.path.join(
            home_dir,
            "Library",
            "Containers",
            "org.mixxx.mixxx",
            "Data",
            "Library",
            "Application Support",
            "Mixxx",
        )  # Mixxx 2.3 and later
    elif system == "Linux":
        home_dir = os.path.expanduser("~")
        if os.path.exists(os.path.join(home_dir, ".var")):  # For Flatpak
            return os.path.join(home_dir, ".var", "app", "org.mixxx.Mixxx", ".mixxx")
        else:
            return os.path.join(home_dir, ".mixxx")
    else:
        raise OSError(f"Unsupported operating system: {system}")


def get_mixxx_db_path():
    """Gets the default path to the Mixxx database."""
    settings_dir = get_mixxx_settings_dir()
    return os.path.join(settings_dir, "mixxxdb.sqlite")
