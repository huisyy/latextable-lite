import latextable_lite

if __name__ == "__main__":
    rows = [["Name", "Age", "Nickname"],
            ["Mr\nXavier\nHuon", 32, "Xav'"],
            ["Mr\nBaptiste\nClement", 1, "Baby"],
            ["Mme\nLouise\nBourgeau", 28, "Lou\n \nLoue"]]
    print(latextable_lite.draw_latex(rows))
