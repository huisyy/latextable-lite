"""
Functions for outputting a table in Latex format.
"""

def draw_latex(rows, 
            num_headers=1, 
            multi_column_size=None, 
            caption=None, 
            caption_above=False,
            label=None,
            c_line=False):
    """
    :param rows: 2d list containing all entries of the table in row-first format
    :param num_headers: Number of header rows
    :param multi_column_size: List describing how many columns correspond to each entry in the first header row
    :param caption: A string that adds a caption to the Latex formatting
    :param caption_above: Boolean indicating if caption is above the table
    :param label: A string that adds a referencing label to the Latex formatting
    :param c_line: Boolean; if true, cmidrules are drawn for every other row
    
    :return: The formatted Latex table returned as a single string.
    """
    if not multi_column_size:
        multi_column_size = [1] * len(rows[0])
    out = ""
    out += _draw_latex_preamble(num_cols=len(rows[-1]), 
                                        caption=caption if caption_above else None)
    out += _draw_latex_header(headers=rows[:num_headers], 
                                        multi_column_size=multi_column_size)
    out += _draw_latex_content(rows=rows[num_headers:], 
                                        c_line=c_line)
    out += _draw_latex_postamble(caption=caption if not caption_above else None,
                                        label = label)
    return out

def _draw_latex_preamble(num_cols, caption):
    """
    Draw the Latex table preamble.
    """
    out = "\\begin{table}[ht]"
    out += "\n"

    # Add caption if given
    out += _draw_table_caption(caption)

    # Begin center
    out += _indent_text("\\centering", 1)
    out += "\n"
    out += _indent_text("\\renewcommand{\\arraystretch}{1.5}", 1)
    out += "\n"

    if num_cols == 2:
        column_str = "X" * 2
    else:
        column_str = "l" + "X" * num_cols
    tabular_str = "\\begin{tabularx}{\\textwidth}{" + column_str + "}\n"
    out += _indent_text(tabular_str, 1)

    return out

def _draw_latex_header(headers, multi_column_size):
    """
    Draw the Latex header rows.
    """
    if not headers:
        return ""
    out = _indent_text("\\{}\n".format('toprule'), 2)

    # Latex for first row/main header
    main_header = headers[0]
    if multi_column_size[0] == 1:
        main_header_latex = main_header[0]
    else:
        main_header_latex = "\\multicolumn{%s}{c}{%s}" % (multi_column_size[0],main_header[0])
    for i, entry in enumerate(main_header[1:]):
        if multi_column_size[i+1] == 1:
            main_header_latex += " & %s" % (entry)
        else:
            main_header_latex += " & \\multicolumn{%s}{c}{%s}" % (multi_column_size[i+1], entry)
    main_header_latex += "\\\\"+ "\n"
    out += _indent_text(main_header_latex, 3)

    # Handling additional headers
    if len(headers) > 1:
        dashed_divider = ""
        counter = 1
        for num in multi_column_size:
            dashed_divider += "\\cmidrule(lr){%s-%s} " % (counter, counter + num - 1)
            counter += num
        
        for header_row in headers[1:]:
            header_row_latex = _indent_text(dashed_divider + "\n", 3)
            header_row_latex += _indent_text(" & ".join(header_row), 3)
            header_row_latex += "\n"
            out += header_row_latex
        out += _indent_text("\\\\" + "\n", 3)
        
    out += _indent_text("\\hline\n", 3)
    return out

def _draw_latex_content(rows, c_line):
    """
    Draw the Latex table content.
    """
    out = ""
    num_cols = len(rows[-1])
    for i, row in enumerate(rows):
        row_latex = ""
        if c_line and not i % 2 and i != len(rows) and i!= 0:
            row_latex += "\cmidrule(lr){2-%s}" % (num_cols)
        row_latex += " & ".join(row) + " \\\\" + "\n"
        out += _indent_text(row_latex, 3)
    return out

def _draw_latex_postamble(caption, label):
    """
    Draw the Latex table postamble.
    """
    out = ""
    out += _indent_text("\\bottomrule \\\\ \n", 2)
    out += _indent_text("\\end{tabularx}\n", 1)

    out += _draw_table_caption(caption)

    if label is not None:
        out += _indent_text("\\label{" + label + "}\n", 1)
    
    out += "\\end{table}"
    return out

def _draw_table_caption(caption):
    """
    Draw the Latex table caption.
    """
    out = ""
    if caption is not None:
        out += _indent_text("\\caption", 1)
        out += "{" + caption + "}\n"
    return out

def _indent_text(text, indent):
    """
    Indent a string by a certain number of tabs.

    :param text: String to indent.
    :param indent: Number of tabs.
    :return: The indented string.
    """
    return '\t' * indent + text