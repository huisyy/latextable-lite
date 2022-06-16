from latextable_lite import utils

"""
Example showcasing modifying color for specific entries within table.
"""

if __name__ == "__main__":
    rows = [["Color", "String"],
            ["Red", "\\leavevmode\\color{red}Text"],
            ["Blue", "\\leavevmode\\color{blue}Text"],
            ["Yellow", "\\leavevmode\\color{yellow}Text"]]
    print(utils.draw_latex(rows))
