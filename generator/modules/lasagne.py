# -*- coding: utf-8 -*-
from .__module__ import Module, dependency, source
from .python import Python
from .theano import Theano
from .tools import Tools


@dependency(Tools, Python, Theano)
@source("git")
class Lasagne(Module):
    def build(self):
        return r"""
            $GIT_CLONE https://github.com/Lasagne/Lasagne ~/lasagne && \
            cd ~/lasagne && \
            $PIP_INSTALL \
                . && \
        """
