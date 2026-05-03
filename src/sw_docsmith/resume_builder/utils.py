from datetime import datetime
from pprint import pprint

html_newline = "<br>"
typ_tbl_char_padding = 2 + len(html_newline)


def sort_exp(exp):
    dt = datetime.strptime(exp["start_date"], "%Y-%m-%d")
    return dt.timestamp()


def print_splash(openfile, filetype="html"):
    splash_graphic = "\n"
    splash_graphic += "<!--------------------------------\n"
    splash_graphic += "   R E S U M E    B U I L D E R   \n"
    splash_graphic += "----------------------------------\n"
    splash_graphic += "   by Salvador Workshop           \n"
    splash_graphic += "--------------------------------->\n"
    splash_graphic += "\n"

    openfile.write(splash_graphic)


def format_phone_num(phone_num, type="txt"):
    country_code = "1"
    area_code = phone_num[0:3]
    mid = phone_num[3:6]
    end = phone_num[6:10]

    output_num = f"({area_code}) {mid} {end}"

    if type == "html":
        output_num = f"+{country_code}{phone_num}"

    return output_num


def format_date(date_str, type="txt"):
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    output_str = dt.strftime("%b %Y")

    return output_str


def get_dashline(line_len):
    out_str = ""
    for idx in range(line_len):
        out_str = out_str + "-"

    return out_str


def get_dashline_for_str(str):
    line_len = len(str) + typ_tbl_char_padding

    out_str = ""
    for idx in range(line_len):
        out_str = out_str + "-"

    return out_str


def get_padline(str, line_len):
    str_len = len(str)
    diff_len = line_len - str_len

    out_str = str
    for idx in range(diff_len):
        out_str = out_str + " "

    return out_str
