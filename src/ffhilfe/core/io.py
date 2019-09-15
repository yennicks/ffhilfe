import logging
import random
import string


def get_temporary_filename(extension: str) -> str:
    """
    Generate a short filename, meant to be used for intermediate processing of files.

    Try to preserve compatibility with 8.3 filename.
    https://en.wikipedia.org/wiki/8.3_filename

    :param extension:
    :return: filename
    """
    prefix = str().join(random.choices(string.ascii_uppercase + string.digits, k=8))
    extension = extension.upper()

    if len(extension) > 3:
        logging.debug(f"Extension '{extension}' is longer than 3 characters, 8.3 filename compatibility broken.")

    temporary_filename = f"{prefix}.{extension}"

    return temporary_filename