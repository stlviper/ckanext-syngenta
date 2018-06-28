# encoding: utf-8

u'''Defines openAFRICA plugin
Extends CKAN plugins core which provides plugin services to the CKAN
'''

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class SyngentaPlugin(plugins.SingletonPlugin):
    u"""
    Syngenta templating plugin.
    """
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True)
    plugins.implements(plugins.ITemplateHelpers)

    def update_config(self, config):
        u"""
        Called by load_environment at earliest point when config is
        available to plugins. The config should be updated in place.

        :param config: ``config`` object
        """
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_resource('fanstatic', 'syngenta')

    def before_map(self, map):
        u"""
        Called before the routes map is generated. ``before_map`` is before any
        other mappings are created so can override all other mappings.

        :param map: Routes map object
        :returns: Modified version of the map object
        """
        map.connect('/about/terms-and-conditions',
                    controller='ckanext.syngenta.controller:CustomPageController',
                    action='toc')
        map.connect('/about/accessibility',
                    controller='ckanext.syngenta.controller:CustomPageController',
                    action='accessibility')
        map.connect('/about/code-of-conduct',
                    controller='ckanext.syngenta.controller:CustomPageController',
                    action='coc')
        map.connect('/about/moderation-policy',
                    controller='ckanext.syngenta.controller:CustomPageController',
                    action='moderation')
        map.connect('/about/faq',
                    controller='ckanext.syngenta.controller:CustomPageController',
                    action='faq')
        map.connect('/about/privacy',
                    controller='ckanext.syngenta.controller:CustomPageController',
                    action='privacy')
        map.connect('/about/contact-us',
                    controller='ckanext.syngenta.controller:CustomPageController',
                    action='contact')
        map.connect('/about/suggest-a-dataset',
                    controller='ckanext.syngenta.controller:CustomPageController',
                    action='suggest_a_dataset')
        map.connect('/atlas-for-africa',
                    controller='ckanext.syngenta.controller:CustomPageController',
                    action='atlas')
        return map

    def get_helpers(self):
        u"""
        All functions, not starting with __ in the ckanext.syngenta.lib
        module will be loaded and made available as helpers to the
        templates.
        """
        from ckanext.syngenta.lib import helpers
        from inspect import getmembers, isfunction

        helper_dict = {}

        funcs = [o for o in getmembers(helpers, isfunction)]
        return dict([(f[0], f[1],) for f in funcs if not f[0].startswith('__')])
