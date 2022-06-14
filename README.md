# latextable-lite

Latextable-lite is a Python package that can create simple Latex tables. It is heavily based on [Latextable](https://github.com/JAEarly/latextable), but removes latextable's dependency on [Texttable](https://github.com/foutaise/texttable).

## Features
- Draws a table in a Latex format using tabularx formatting.
- The output is correctly indented for directly copying into Latex.
- Supports multiple header rows and multi-column header rows.

## Installation
```
pip install latextable-lite
```
## Usage

The single function `latextable_lite.draw_latex` returns a formatted Latex string based on the provided table.
Aside from `rows`, all arguments are optional.
```
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
```
## Examples
A basic example is given below. For more see the examples directory.

Code:

```
import latextable_lite

rows = [["Name", "Age", "Nickname"],
        ["Mr\nXavier\nHuon", 32, "Xav'"],
        ["Mr\nBaptiste\nClement", 1, "Baby"],
        ["Mme\nLouise\nBourgeau", 28, "Lou\n \nLoue"]]
print(latextable_lite.draw_latex(rows))
```

Output:

```
\begin{table}[ht]
        \centering
        \renewcommand{\arraystretch}{1.5}
        \begin{tabularx}{\textwidth}{lXXXXXX}
                \toprule
                        Name & Age & Sex & Nickname & Occupation & Marital Status\\
                        \hline
                        Xavier & 32 & M & Xav' & Doctor & Married \\
                        Baptiste & 1 & F & Baby & Baby & Single \\
                        Louise & 28 & M & Lou/Loue & Engineer & Single \\
                \bottomrule \\ 
        \end{tabularx}
\end{table}
```



