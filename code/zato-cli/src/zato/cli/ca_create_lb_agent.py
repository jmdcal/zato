# -*- coding: utf-8 -*-

"""
Copyright (C) 2010 Dariusz Suchojad <dsuch at gefira.pl>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

# stdlib
from copy import deepcopy

# Zato
from zato.cli import CACreateCommand, common_ca_create_opts

class CreateLBAgent(CACreateCommand):
    command_name = "ca create-lb-agent"

    opts = [
        dict(name="--organizational-unit", help="Organizational unit name (defaults to ZatoLBAgent)"),
    ]
    opts += deepcopy(common_ca_create_opts)

    description = "Creates the load balancer agent's crypto material (keys, the certificate and a CSR)"

    def get_file_prefix(self, file_args):
        return "lb-agent"

    def get_organizational_unit(self, args):
        return "zato-lb-agent"

    def execute(self, args):
        return self._execute(args, "v3_server")

def main(target_dir):
    CreateLBAgent(target_dir).run()

if __name__ == "__main__":
    main(".")