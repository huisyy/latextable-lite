from latextable_lite import utils

"""
Example showcasing all optional arguments:
    num_headers, multi_column_size, caption, caption_above, and c_line.
"""
if __name__ == "__main__":
    num_headers = 2
    rows = [["Item", "Guitar", "Piano", "Flute", "Ukelele", "Mic"],
            ["Setup", "A", "B", "A", "B", "A", "B", "A", "B", "A", "B"],
            ["Uniform w/ replacement", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0"],
            ["", "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}"],
            ["Uniform w/o replacement", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0"],
            ["", "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}"],
            ["S-NeRF", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0"],
            ["", "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}"],
            ["RFE", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0"],
            ["", "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}"],
            ["RFE+", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0"],
            ["", "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}",  "^{\pm 0.5}"]]
    multi_column_size = [1,2,2,2,2,2]
    caption = "advanced latextable-lite example"
    caption_above = True,
    c_line = True
    
    print(utils.draw_latex(rows, 
                num_headers=num_headers,
                multi_column_size=multi_column_size,
                caption=caption,
                caption_above=caption_above,
                c_line=c_line))

