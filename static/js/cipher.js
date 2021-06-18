const
    vrt = "∣", hrz = "-",
    y = "^", n = "=", h = "\"",
    Y = "Y", N = "N", H = "H",
    NW = "🡤", NE = "🡥", SW = "🡧", SE = "🡦",
    a = ">", e = "<", i = "Ʌ", o = "O", u = "V",
    A = "A", E = "E", I = "I", O = "O", U = "U",
    w = "∣^", x = "∣∣", m = "∣=",
    W = "W", X = "X", M = "M",
    plain_list = [
             "J", "D", "B",
        "G", "C", "T", "P",
        H, Y, W, X, N, M,
        "K", "S", "L", "F",
        "Q", "Z", "R", "V",
        A, E, I, O, U,
    ],

    NWh = NW + hrz, NEh = NE + hrz, VNEh = vrt + NE + hrz,

    VNW  = vrt + NW, VNE = vrt + NE,

    VSW  = vrt + SW,       VSE  = vrt + SE,
    SWh  =       SW + hrz,  SEh =       SE + hrz,
    VSWh = vrt + SW + hrz, VSEh = vrt + SE + hrz,

    cipher_list = [
             NWh, NEh, VNEh,
        VNW, NW,  NE,  VNE,
        h, y, w, x, n, m,
        VSW, SW,  SE,  VSE,
        VSWh, SWh, SEh, VSEh,
        a, e, i, o, u,
    ],

    ec = function (plain_text) {
        ct = "";
        for (let plain_char of plain_text.toUpperCase()) {
            let index = plain_list.indexOf(plain_char);
            ct += index >= 0 ? cipher_list[index] : plain_char;
        }
        return ct;
    },

    dc = function (cipher_text) {
        if (cipher_text.length > 0){
            fetch('/decipher/' + cipher_text).then(function(response) {
                response.text().then(function(text) {
                    document.getElementById('decipher-output').innerHTML = text;
                });
            });
        }
        else{
            document.getElementById('decipher-output').innerHTML = "";
        }
    };