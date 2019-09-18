#!/usr/bin/env python3
#
# Copyright (C) 2019 Dmitry Marakasov <amdmi3@amdmi3.ru>
#
# This file is part of repology
#
# repology is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# repology is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with repology.  If not, see <http://www.gnu.org/licenses/>.

# mypy: no-disallow-untyped-calls

from typing import List, Optional

from repology.package import Package
from repology.packagemaker import PackageFactory


def spawn_package(
    *,
    name: str = 'dummyname',
    version: str = '0',
    repo: str = 'dummyrepo',
    family: str = 'dummyfamily',
    flags: int = 0,
    homepage: Optional[str] = None,
    comment: Optional[str] = None,
    category: Optional[str] = None,
    maintainers: Optional[List[str]] = None,
    flavors: Optional[List[str]] = None,
) -> Package:
    m = PackageFactory().begin()

    m.set_name(name)
    m.set_version(version)

    m.set_flags(flags)
    m.set_summary(comment)
    m.add_homepages(homepage)
    m.add_categories(category)
    m.add_maintainers(maintainers)

    p = m.spawn(repo=repo, family=family)

    if flavors is not None:
        p.flavors.extend(flavors)

    return p
