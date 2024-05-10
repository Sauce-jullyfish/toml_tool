import tomltool
import os


def test_load():
    t = tomltool.TomlTool.load('test.toml')
    assert isinstance(t, tomltool.TomlTool)


def test_add_item():
    t = tomltool.TomlTool.load('test.toml')
    t.add_item('key', 'value')
    t.save()
    assert t.key == 'value'


def test_remove_item():
    t = tomltool.TomlTool.load('test.toml')
    t.add_item('section.key', 'value')
    t.remove_item('section.key')
    assert 'key' not in t.get('section')


def test_update_item():
    t = tomltool.TomlTool.load('test.toml')
    t.add_item('key', 'value')
    t.update_item('key', 'new_value')
    assert t.key == 'new_value'


def test_save():
    t = tomltool.TomlTool.load('test.toml')
    t.add_item('key', 'value')
    t.save_to_file('test_save.toml')
    assert os.path.exists('test_save.toml')
