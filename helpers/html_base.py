def single_tag(name, attributes=None):
    if attributes and type(attributes) is list:
        attributes = " ".join(attributes)
    return f"<{name}" + \
           (f" {attributes}>" if attributes is not None else ">")


def no_attribute_tag(name, content=""):
    if content and type(content) is list:
        content = "".join(content)
    return f"<{name}>" + \
           (f"{content}" if content else "") + \
           f"</{name}>"


def tag(name, attributes=None, content=""):
    if attributes and type(attributes) is list:
        attributes = " ".join(attributes)
    if content and type(content) is list:
        content = "".join(content)
    return f"<{name}" + \
           (f" {attributes}>" if attributes else ">") + \
           (f"{content}" if content else "") + \
           f"</{name}>"


def html(attributes, content):
    return "<!DOCTYPE html>" + tag("html", attributes, content)


def head(content):
    return no_attribute_tag("head", content)


def title(content):
    return no_attribute_tag("title", content)


def meta(attributes):
    return single_tag("meta", attributes)


def link(attributes):
    return single_tag("link", attributes)


def body(attributes=None, content=""):
    return tag("body", attributes, content)


def div(attributes=None, content=""):
    return tag("div", attributes, content)


def h4(attributes=None, content=""):
    return tag("h4", attributes, content)


def h5(attributes=None, content=""):
    return tag("h5", attributes, content)


def p(attributes=None, content=""):
    return tag("p", attributes, content)


def span(attributes=None, content=""):
    return tag("span", attributes, content)


def a(attributes=None, content=""):
    return tag("a", attributes, content)


def script(attributes=None, content=""):
    return tag("script", attributes, content)


def input_text(attributes=None):
    return single_tag('input type="text"', attributes)


def input_button(attributes=None):
    return single_tag('input type="button"', attributes)


def textarea(attributes=None):
    return tag('textarea', attributes)
