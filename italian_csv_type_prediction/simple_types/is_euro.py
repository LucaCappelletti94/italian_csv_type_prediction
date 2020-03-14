def is_euro(candidate) -> bool:
    if isinstance(candidate, str):
        for target in ("EUR", "€"):
            candidate = candidate.replace(target, " ")
        candidate = " ".join(candidate.split()).strip()
    try:
        return len(str(float(candidate)).split(".")) <= 2
    except (ValueError, TypeError):
        return False
