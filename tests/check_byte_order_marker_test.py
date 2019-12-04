from __future__ import absolute_import
from __future__ import unicode_literals

from pre_commit_hooks import check_byte_order_marker


def test_failure(tmpdir):
    f = tmpdir.join('f.txt')
    f.write_text('ohai', encoding='utf-8-sig')
    assert check_byte_order_marker.main((f.strpath,)) == 1


def test_success(tmpdir):
    f = tmpdir.join('f.txt')
    f.write_text('ohai', encoding='utf-8')
    assert check_byte_order_marker.main((f.strpath,)) == 0
