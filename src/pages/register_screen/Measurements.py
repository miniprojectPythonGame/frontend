from src.globals.const_values import *
from src.components.ColorSchemes import ColorSchemes


class Measurements:
    # WINDOW PARAMETERS
    size_factor = SIZE_FACTOR
    window_width = SCREEN_WIDTH * size_factor
    window_height = SCREEN_HEIGHT * size_factor
    margin = round(SCREEN_WIDTH * SIZE_FACTOR * 0.12)

    # LOGO PARAMETERS
    logo_size_factor = 0.1
    logo_width = 899 * logo_size_factor
    logo_height = 318 * logo_size_factor

    # FONTS: sizes
    title_font = TITLE_FONT
    header_primary_font = HEADER_PRIMARY_FONT
    header_secondary_font = HEADER_SECONDARY_FONT
    header_tertiary_font = HEADER_TERTIARY_FONT
    text_font = TEXT_FONT
    input_font = INPUT_FONT

    # FONTS: colors
    text_color = pygame.Color('gray26')

    # IMAGE: graphic
    graphic = {
        'x': window_width - round(SCREEN_WIDTH * SIZE_FACTOR * 0.45),
        'y': 0,
        'width': round(SCREEN_WIDTH * SIZE_FACTOR * 0.45),
        'height': round(SCREEN_HEIGHT * SIZE_FACTOR),
    }

    # IMAGE: logo
    logo = {
        'x': graphic['width'] + 30,
        'y': 30,
        'width': logo_width,
        'height': logo_height,
    }

    # LABEL: Register
    label_login = {
        'text': 'Register',
        'x': margin + round((SCREEN_WIDTH * SIZE_FACTOR) - (graphic['width'] + 2 * margin)),
        'y': margin - 50,
        'anchor': 'topright',
    }

    # MultilineText: Description
    mt_desc = {
        'text': [
            'Praesent vel tellus accumsan nisl tincidunt.',
            'Pellentesque ullamcorper venenatis lorem et.',],
        'x': margin + round((SCREEN_WIDTH * SIZE_FACTOR) - (graphic['width'] + 2 * margin)),
        'y': margin + 30,
        'anchor': 'topright',
    }

    # INPUT: Nickname
    input_nick = {
        "padding": 5,
        "border": 3,
        "color": ColorSchemes(),
        "x": margin,
        "y": margin + 90,
        "width": round((SCREEN_WIDTH * SIZE_FACTOR) - (graphic['width'] + 2 * margin)),
        "height": 50,
    }

    # INPUT: Email
    input_email = {
        "padding": 5,
        "border": 3,
        "color": ColorSchemes(),
        "x": margin,
        "y": margin + 160,
        "width": round((SCREEN_WIDTH * SIZE_FACTOR) - (graphic['width'] + 2 * margin)),
        "height": 50,
    }


    # INPUT: Password
    input_pass = {
        "padding": 5,
        "border": 3,
        "color": ColorSchemes(),
        "x": margin,
        "y": margin + 230,
        "width": round((SCREEN_WIDTH * SIZE_FACTOR) - (graphic['width'] + 2 * margin)),
        "height": 50,
    }

    # BUTTON: Register
    bt_login = {
        "color": ColorSchemes(),
        "x": margin,
        "y": margin + 305,
        "width": input_pass['width'],
        "height": input_pass['height'],
        "text": 'Register'
    }

    # LABEL: Signin
    label_signup = {
        'text': 'Already registered?',
        'x': margin + input_nick['width'] - 120,
        'y': window_height - margin + 8,
        'anchor': 'topright',
    }

    # BUTTON: Signin
    bt_signup = {
        "color": ColorSchemes(),
        'x': margin + input_nick['width'] - 100,
        "y": window_height - margin,
        "width": 100,
        "height": 35,
        "text": 'Sign in'
    }