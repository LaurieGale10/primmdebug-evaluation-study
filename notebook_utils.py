
def display_percentage_string(x: int | float, y: int | float, decimal_places: int = 2) -> str:
    """Display a percentage string in the form 'x/y (percentage%)'"""
    if y == 0:
        return f"{x}/{y} (N/A)"
    percentage: float = (x / y) * 100
    return f"{x}/{y} ({percentage:.{decimal_places}f}%)"