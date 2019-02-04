# -*- coding: utf-8 -*-
from .__module__ import Module, dependency, source, version
from .config_files.odbcinst import ODBC_INST
from .python import Python
from .tools import Tools


@dependency(Tools, Python)
@source("git")
class Pymssql(Module):
    def build(self):
        return r"""
            apt-get update && apt-get install -y \
                curl apt-transport-https debconf-utils freetds-dev freetds-common freetds-bin freetds-dev \
            && \
            curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
            && \
            curl https://packages.microsoft.com/config/debian/8/prod.list > /etc/apt/sources.list.d/mssql-release.list \
            && \
            DEBIAN_FRONTEND=noninteractive ACCEPT_EULA=Y $APT_INSTALL msodbcsql17 \
            && \
            echo "{0}" > /etc/odbcinst.ini
        """.format(
            ODBC_INST
        )
