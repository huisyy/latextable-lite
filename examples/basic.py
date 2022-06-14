from latextable_lite import utils

if __name__ == "__main__":
    rows = [["Name", "Age", "Sex", "Nickname", "Occupation", "Marital Status"],
            ["Xavier", "32", "M", "Xav'", "Doctor", "Married"],
            ["Baptiste", "1", "F", "Baby", "Baby", "Single"],
            ["Louise", "28", "M", "Lou/Loue", "Engineer", "Single"]]
    print(utils.draw_latex(rows))
