#
# MIT License
#
# Copyright (c) 2025 nbiotcloud
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
"""
UVM Objects.
"""

import ucdp as u

from .cfg import UvmCfg
from .env import UvmEnv
from .object import UvmObject
from .scoreboard import UvmScoreboard
from .seq import UvmSeq
from .test import UvmTest
from .vseq import UvmVseq


class UvmTbMixin(UvmObject):
    """Base Class for All UVM Testbenches."""

    def get_envs(self) -> tuple[UvmEnv, ...]:
        """Environments."""
        return ()

    def get_seqs(self) -> tuple[UvmSeq, ...]:
        """Sequences."""
        return ()

    def get_vseq(self) -> tuple[UvmVseq, ...]:
        """Virtual Sequences."""
        return ()

    def get_cfg(self) -> tuple[UvmCfg, ...]:
        """Configurations."""
        return ()

    def get_scoreboards(self) -> tuple[UvmScoreboard, ...]:
        """Score Boards."""
        return ()

    def get_tests(self) -> tuple[UvmTest, ...]:
        """Tests."""
        return ()


class AUvmTbMod(u.ATbMod, UvmTbMixin):
    """Static UVM Testbench."""


class AGenericUvmTbMod(u.AGenericTbMod, UvmTbMixin):
    """Generic UVM Testbench."""


class AConfigurableUvmTbMod(u.AConfigurableTbMod, UvmTbMixin):
    """Configurable UVM Testbench."""
