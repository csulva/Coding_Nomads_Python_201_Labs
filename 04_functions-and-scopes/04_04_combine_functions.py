# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.
def greet(greeting: str, name: str):
    """[produces a greeting to the name provided in the arg]

    Args:
        greeting ([str]): [provides a greeting to the user]
        name ([str]): [the person who is greeted in the function]
    Returns:
        [str]: [greets the name with the greeting input]
    """
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

def write_letter(goodbye):
    return greet('Hello!', 'Chris') + goodbye

print(write_letter('\nGoodbye!'))
