def is_float(candidate):
    try:
        return str(float(candidate)) == str(candidate)
    except (ValueError, TypeError):
        return False