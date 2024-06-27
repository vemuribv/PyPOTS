"""
The package of the partially-observed time-series imputation model TiDE.

Refer to the paper
`Abhimanyu Das, Weihao Kong, Andrew Leach, Shaan Mathur, Rajat Sen, and Rose Yu.
"Long-term Forecasting with TiDE: Time-series Dense Encoder".
In Transactions on Machine Learning Research, 2023.
<https://openreview.net/pdf?id=pCbC3aQB5W>`_

Notes
-----
This implementation is inspired by the official one
https://github.com/google-research/google-research/blob/master/tide and https://github.com/lich99/TiDE

"""

# Created by Wenjie Du <wenjay.du@gmail.com>
# License: BSD-3-Clause


from .model import TiDE

__all__ = [
    "TiDE",
]
