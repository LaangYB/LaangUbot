# Laang - Ubot
# Copyright (C) 2024 @LaangYB
#
# This file is a part of <https://github.com/LaangYB/LaangUbot>
# Please read the GNU Affero General Public License in
# <https://www.github.com/LaangYB/LaangUbot/blob/main/LICENSE/>.
#
# FROM LaangUbot <https://github.com/LaangYB/LaangUbot>
# t.me/ybtraviss & t.me/ybtraviss

# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

import logging
from typing import Optional

from fipper import Client
from fipper.raw.functions.channels import GetFullChannel
from fipper.raw.functions.messages import GetFullChat
from fipper.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from fipper.types import Message

from config import *
from git import Repo
from pyLnnggg import PyrogramYB
from pyLnnggg.Clients import *
from pyLnnggg.config import Var
from pyLnnggg.pyrogram import eod, eor

# Initialize variables and constants
flood = {}
OLD_MSG = {}
repo = Repo()
branch = repo.active_branch.name  # Get the branch name
yins = PyrogramYB()
var = Var()
hndlr = [f"{var.HNDLR[i]}" for i in range(6)]
logs = logging.getLogger(__name__)

# Cache and font file paths
file = './cache/'
cache = "cache/{}.png"
cache_thumb = "cache/thumb{}.png"
font = "assets/font.ttf"
font2 = "assets/font2.ttf"
