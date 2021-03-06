# Copyright: 2008 MoinMoin:BastianBlank
# License: GNU GPL v2 (or any later version), see LICENSE.txt for details.

"""
MoinMoin - Tests for moin.converters._args_wiki
"""

import pytest

from moin.converters._args_wiki import Arguments, parse, unparse


@pytest.mark.parametrize('wiki,positional,keyword', [
    (ur'both positional both=foo keyword=bar',
     [u'both', u'positional'],
     {u'both': u'foo', u'keyword': u'bar'}),

    (ur'a-b a_b a-c=foo a_c=bar',
     [u'a-b', u'a_b'],
     {u'a-c': u'foo', u'a_c': u'bar'}),

    (ur'''"a b\tc\nd" k="a b\tc\nd"''',
     [u'a b\tc\nd'],
     {u'k': u'a b\tc\nd'}),
])
def test(wiki, positional, keyword):
    a = parse(wiki)
    assert a.positional == positional
    assert a.keyword == keyword

    s = unparse(Arguments(positional, keyword))
    assert s == wiki


def test_parse():
    a = parse(ur''''a b\tc\nd',k="a b\tc\nd"''')
    assert a.positional == [u'a b\tc\nd']
    assert a.keyword == {u'k': u'a b\tc\nd'}
