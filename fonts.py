from tkinter.font import Font

def button_fonts(size, family):
    button_font = Font(
        family = family,
        size = size,
        weight = 'bold',
        slant = 'italic',
        overstrike = 0
    )
    return button_font

def label_fonts(size, family):
    label_font = Font(
        family = family,
        size = size,
        weight='bold',
        slant='roman',
        overstrike=0,
        )
    return label_font