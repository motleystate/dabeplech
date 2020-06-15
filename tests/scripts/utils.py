import colored


def _format_print(key_word, msg, color=None):
    """
    Format message such as:
      --> {key_word} ... {msg}
    """
    if color:
        return f" --> {key_word} ... {colored.stylize(msg, colored.fg(color))}"
    return f" --> {key_word} ... {msg}"
