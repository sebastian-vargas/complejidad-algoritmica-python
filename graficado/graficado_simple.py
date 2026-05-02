from bokeh.plotting import figure, output_file, show

if __name__ == "__main__":
    output_file("graficado_simple.html")

    x = [1, 2, 3, 4, 5]
    y = [6, 7, 2, 4, 5]

    p = figure(title="Simple Line Example", x_axis_label='x', y_axis_label='y')

    p.line(x, y, legend_label="Line", line_width=2)

    show(p) 