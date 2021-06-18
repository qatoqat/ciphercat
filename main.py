from blacksheep import Request, Response
from blacksheep.server import Application
from blacksheep.server.responses import html, text
from pages import cipher_page
from helpers import cipher
app = Application()
app.serve_files("static")


@app.route("/")
async def home(_):
    return html(cipher_page.get_page())


@app.route("/encipher/{text}")
async def encipher(request: Request) -> Response:
    return text(cipher.encipher(request.route_values["text"]))


@app.route("/decipher/{text}")
async def decipher(request: Request) -> Response:
    return text(cipher.decipher(request.route_values["text"]))
