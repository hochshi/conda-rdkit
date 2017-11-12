from __future__ import print_function

import os
from datetime import datetime

from rdkit.rdBase import rdkitVersion

if rdkitVersion.endswith(".dev1"):
    pkg_version = rdkitVersion[:-1] + datetime.today().strftime("%Y%m%d")
else:
    pkg_version = rdkitVersion
