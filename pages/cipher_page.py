from helpers.html_component import *

button_style = 'style="float: right; width: 120px; margin-left: 10px"'
input_text_style = 'style="width: calc(100% - 300px); text-align: center"'
output_div_style = 'style="width: 100%; min-height: 80px; font-size: 40px; text-align: center"'
output_text_style = 'style="width: 100%; min-height: 80px; font-size: 40px; text-align: center; overflow: auto;"'


def get_page():
    return html(
        None,
        [
            get_head(),
            get_body(),
            script('script src="js/cipher.js"'),
            script('script src="js/bind.js"'),
        ])


def get_head():
    return head([
        title("cipher"),
        meta('name="viewport" charset="UTF-16" content="width=device-width, initial-scale=1"'),
        link('rel="stylesheet" href="css/normalize.css"'),
        link('rel="stylesheet" href="css/skeleton.css"'),
        link('rel="stylesheet" href="css/style.css"'),
        # link_css('css/normalize.css'),
        # link_css('css/skeleton.css'),
        link_icon('image/png', 'images/favicon.png')
    ])


def get_body():
    return body(None, div_container(div('style="margin-top: 25%"', [get_encipher_div(), get_decipher_div()])))


def get_encipher_div():
    return div(
        None,
        [
            h5('id="encipher-title"'),
            div(f'{output_div_style}',
                [
                    span('id="encipher-output" readonly="readonly"'),
                ]),
            div(None,
                [
                    input_text(f'id="encipher-input" {input_text_style}'),
                    input_button(f'id="encipher-copy" value="copy" {button_style}'),
                    input_button(f'id="encipher-clear" value="clear" {button_style}')
                ])
        ])


def get_decipher_div():
    return div(
        None,
        [
            h5('id="decipher-title"'),
            div(None,
                [
                    div(f'id="decipher-output" readonly="readonly" {output_text_style}'),
                ]),
            div(None,
                [
                    input_text(f'id="decipher-input" {input_text_style}'),
                    input_button(f'id="decipher-copy" value="copy" {button_style}'),
                    input_button(f'id="decipher-clear" value="clear" {button_style}')
                ])
        ])
