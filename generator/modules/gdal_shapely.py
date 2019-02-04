# -*- coding: utf-8 -*-
from .__module__ import Module, dependency, source, version
from .python import Python
from .tools import Tools


@dependency(Tools, Python)
@source("pip")
class Gdal_Shapely(Module):
    def build(self):
        return r"""
            DEBIAN_FRONTEND=noninteractive $APT_INSTALL libgdal-dev python-gdal \
            && \
            CPLUS_INCLUDE_PATH=/usr/include/gdal \
            && \
            C_INCLUDE_PATH=/usr/include/gdal \
            && \
            $PIP_INSTALL GDAL==$(gdal-config --version | awk -F'[.]' '{print $1"."$2}') \
            && \
            $PIP_INSTALL shapely --no-binary shapely \
            && \
        """
