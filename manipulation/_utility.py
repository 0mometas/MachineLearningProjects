import glob
import os.path
from typing import NoReturn, Union, Dict

import pandas as pd

from _decorators import create_path_if_not_exist
from _defaults import DefaultValue
from _miscellaneous import Miscellaneous


class IO(DefaultValue, Miscellaneous):

    ########################################################################

    @create_path_if_not_exist
    def save_excel(self,
                   data: Union[pd.DataFrame, Dict[str, pd.DataFrame]],
                   *,
                   path: str,
                   index: bool = False
                   ) -> NoReturn:

        if not path.endswith(self.DEFAULT_EXCEL_EXTENSION):
            path += self.DEFAULT_EXCEL_EXTENSION

        if isinstance(data, dict):

            with pd.ExcelWriter(path) as writer:

                for name, df in data.items():
                    df.to_excel(writer, sheet_name=name, index=index)

        else:

            data.to_excel(path, index=index)

    ########################################################################

    def load_excel(self,
                   data: Union[str, pd.DataFrame],
                   **kwargs
                   ) -> pd.DataFrame:

        # If DataFrame is given
        if isinstance(data, pd.DataFrame):
            return data

        # If path is given
        if isinstance(data, str):

            if os.path.isdir(data):

                excel_list = glob.glob1(data, self.DEFAULT_EXCEL_PATTERN)

                sorted_list = sorted(
                    excel_list,
                    key=lambda f: os.path.getmtime(os.path.join(data, f)))

                file = sorted_list[-1]

                print(
                    "\nParameter type: {}".format("Directory"),
                    "\nLast modified file: '{}' has been read".format(file))

                data = os.path.join(data, file)

            elif os.path.isfile(data):

                file = os.path.basename(data)

                print(
                    "\nParameter type: {}".format("File"),
                    "\n'{}' has been read".format(file))

            else:
                raise TypeError(
                    "\"data\" should be string or Pandas DataFrame",
                    "{} is given.".format(type(data))
                )

        filtered_kwargs = self.get_kwargs(prefix="read_excel", **kwargs)

        data = pd.read_excel(data, **filtered_kwargs)

        return data

    ########################################################################

###############################################################################


if __name__ == "__main__":

    print("#"*72)
