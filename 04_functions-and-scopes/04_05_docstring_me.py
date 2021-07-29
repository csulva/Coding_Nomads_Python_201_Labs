# Add a Google-style docstring to the function below. Your docstring
# should at least describe what it does, what arguments it takes,
# and what it returns.

def km_to_miles(km):
    """Converts kilometers to miles.

    Args:
      one argument which is int you can represent as kilometers input.

    Returns:
      the arg into miles.

    Raises:
      Arg must be int otherwise will not convert.
    """
    miles = km * 0.6
    return miles

print(km_to_miles.__doc__)
