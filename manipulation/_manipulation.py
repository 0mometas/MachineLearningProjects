# Manipulation #
######################
# 1.0.0:    Initiate #
######################

########################################################################
#                            Import library                            #
########################################################################

import os
from typing import Union
from glob import glob1
import pandas as pd


########################################################################
#                           Class Definition                           #
########################################################################
class Manipulation:

    @staticmethod
    def read_data(data: Union[str, pd.DataFrame]
                  ) -> pd.DataFrame:
        """
        Read the data.

        :param data: [String][Pandas DataFrame]
        String of path to exist [csv] or [excel] file.
        String of path to exist directory.
        The DataFrame
        :return:
        DataFrame of data.
        """
        if isinstance(data, str):
            if os.path.isfile(data):
                pass

            elif os.path.isdir(data):
                data = glob1(data, ".")
                data = os.listdir(data)[-1]

            if data.split(".")[-1].startswith("csv"):
                data = pd.read_csv(data)
            elif data.split(".")[-1].startswith("xls"):
                data = pd.read_excel(data)
            else:
                print("Function can only read the csv or excel format.")
                return None
        elif isinstance(data, pd.DataFrame):
            pass

        else:
            raise ValueError("\"data\" type must be str or pd.DataFrame.")

        return data
