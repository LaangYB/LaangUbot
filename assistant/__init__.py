# Laang - Ubot
# Copyright (C) 2024 @LaangYB
#
# This file is a part of < https://github.com/LaangYB/LaangUbot >
# Please read the GNU Affero General Public License in
# <https://www.github.com/LaangYB/LaangUbot/blob/main/LICENSE/>.
#
# FROM LaangUbot <https://github.com/LaangYB/LaangUbot>
# t.me/ybtraviss & t.me/ybtraviss


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

import logging
from config import *
from git import Repo
from pyLnnggg import PyrogramYB
from pyLnnggg.Clients import *
from pyLnnggg.config import Var

# Mendapatkan repository git dan branch aktif
repo = Repo()
branch = repo.active_branch

# Inisialisasi PyrogramYB dan Var
yins = PyrogramYB()
var = Var()

# Logger untuk modul ini
logs = logging.getLogger(__name__)
