from typing import Dict, Any


class Miscellaneous:
    """
    Misc method. Try to keeps all the method static.
    """

    @staticmethod
    def get_kwargs(prefix,
                   **kwargs
                   ) -> Dict[str, Any]:

        result_kwargs = {}

        for key, value in kwargs.items():

            match_keys = "{}__".format(prefix)

            if key.startswith(match_keys):

                key = key.replace(match_keys, "", 1)

                result_kwargs[key] = value

        return result_kwargs

    ################################################################

########################################################################
