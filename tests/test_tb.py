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
"""Environment Test."""

import ucdp_uvm as uvm


class UvmTbMod(uvm.AUvmTbMod):
    """Example UVM Testbench."""

    def _build(self):
        pass


def test_tb():
    """Testbench."""
    tb = UvmTbMod()
    assert tb.name == "uvm_tb"
    assert tb.modname == "uvm_tb"
    assert tb.libname == "tests"

    assert tb.get_envs() == ()
    assert tb.get_seqs() == ()
    assert tb.get_vseqs() == ()
    assert tb.get_cfgs() == ()
    assert tb.get_scoreboards() == ()
    assert tb.get_tests() == ()
