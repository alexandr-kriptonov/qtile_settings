# -*- coding: utf-8 -*-


class Theme(object):
    bar = {
        'size': 24,
        'background': '000000',
    }
    widget = {
        'font': 'Terminus',
        'fontsize': 20,
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
        'urgent_alert_method': 'border',
        'padding': 4,
        'borderwidth': 2,
        'highlight_method': 'border',
    })

    sep = {
        'background': bar['background'],
        'foreground': '444444',
        'height_percent': 75,
    }

    systray = widget.copy()
    systray.update({
        'icon_size': bar['size'],
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

    clock = widget.copy()
    clock.update({
        'fmt': '[%Y-%m-%d] %a [%H:%M:%S]  ',
        'fontsize': widget['fontsize'],
        'padding': None,
        'foreground': 'eeeeee',
        'background': bar['background'],
    })

    weather = widget.copy()
    weather.update({
        'update_interval': 60,
        'metric': False,
        'format': '{condition_text} {condition_temp}°',
    })

    spacer = widget.copy()
    spacer.update({
        'background': bar['background'],
    })

    sep = widget.copy()
    sep.update({
        'linewidth': 2,
        'foreground': '808088',
        'height_percent': 100,
    })

    thermalsensor = widget.copy()
    thermalsensor.update({
        'fontsize': widget['fontsize'],
        'font': widget['font'],
    })

    notify = widget.copy()
    # notify.update({
    #     'text': "dfsdfdf",
    # })
