# -*- coding: utf-8 -*-


class Theme(object):
    bar = {
        'size': 24,
        'background': '15181a',
    }
    widget = {
        'font': 'Open Sans',
        'fontsize': 11,
        'background': bar['background'],
        'foreground': 'eeeeee',
    }
    graph = {
        'background': '000000',
        'border_width': 0,
        'border_color': '000000',
        'line_width': 1,
        'margin_x': 0,
        'margin_y': 0,
        'width': 50,
    }

    groupbox = widget.copy()
    groupbox.update({
        'padding': 2,
        'borderwidth': 3,
    })

    sep = {
        'background': bar['background'],
        'foreground': '444444',
        'height_percent': 75,
    }

    systray = widget.copy()
    systray.update({
        'icon_size': 16,
        'padding': 3,
    })

    battery = widget.copy()
    #battery.update({
    #    'energy_now_file': 'charge_now',
    #    'energy_full_file': 'charge_full',
    #    'power_now_file': 'current_now',
    #    })

    battery_text = battery.copy()
    battery_text.update({
        'charge_char': '↑ ',
        'discharge_char': '↓ ',
        'format': '{char}{hour:d}:{min:02d}',
    })

    weather = widget.copy()
    weather.update({
        'update_interval': 60,
        'metric': False,
        'format': '{condition_text} {condition_temp}°',
    })
