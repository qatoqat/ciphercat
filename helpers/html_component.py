from helpers.html_base import *


def link_css(href):
    return link(f'rel="stylesheet" href="{href}"'),


def link_icon(icon_type, href):
    return link(f'rel="icon" type="{icon_type}" href="{href}"')


def div_container(content):
    return div('class="container"', content)


def div_row(content):
    return div('class="row"', content)


def div_tooltip(tooltip, content):
    return div('class="tooltip"', [content, tooltip])
