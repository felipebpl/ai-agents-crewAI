def validate_env_var(var_name: str, value: str) -> str:
    """
    Validates the presence of an environment variable.
    """
    if not value:
        raise ValueError(f"Missing '{var_name}' in environment variables.")
    return value
