def draw_line_from_string(line_string):
    for char in line_string:
        color = get_color(line_string)
        draw_color_pixel(color)