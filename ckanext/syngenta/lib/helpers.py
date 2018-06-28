# encoding: utf-8



import datetime

from ckan import plugins


def current_year():
    u""" Return the current year """
    year = datetime.datetime.now().year
    return year


def is_plugin_enabled(plugin_name):
    u"""
    Returns a boolean True or False, indicating if the supplied plugin_name
    is enabled in the config file

    :param plugin_name: the name of the plugin to check for in the config file
    :type plugin_name: string
    """
    return plugins.plugin_loaded(plugin_name)
