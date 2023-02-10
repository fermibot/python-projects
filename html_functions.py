
def CreateBlankHTMLPage(title: str = 'fermibot'):
    _blankHTMLPage = "      <!DOCTYPE html              \n  " +   \
                            "<html>                     \n  " +   \
                            "   <head>                  \n  " +   \
                            "        <title>            \n  " +   \
                            "            " + title + "\n" + \
                            "        </title>           \n  " +   \
                            "    </head>                \n  " +   \
                            "    <body>                 \n  " +   \
                            "    </body>                \n  " +   \
                            "</html>"
    return _blankHTMLPage
