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
        'padding': 1,
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

    groupbox = widget.copy()
    groupbox.update({
        'urgent_alert_method': 'border',
        'padding': widget['padding'],
        'borderwidth': 2,
        'highlight_method': 'border',
    })

    systray = widget.copy()
    systray.update({
        'icon_size': bar['size'],
        'padding': widget['padding'],
    })

    battery = widget.copy()
    battery.update({
        'energy_now_file': 'charge_now',
        'energy_full_file': 'charge_full',
        'power_now_file': 'current_now',
        'padding': widget['padding'],
    })

    battery_text = battery.copy()
    battery_text.update({
        'charge_char': '↑ ',
        'discharge_char': '↓ ',
        'format': '{char}{hour:d}:{min:02d}',
        'padding': widget['padding'],
    })

    clock = widget.copy()
    clock.update({
        'fmt': '[%Y-%m-%d] %a [%H:%M:%S]  ',
        'fontsize': widget['fontsize'],
        'padding': widget['padding'],
        'foreground': 'eeeeee',
        'background': bar['background'],
    })

    weather = widget.copy()
    weather.update({
        'update_interval': 60,
        'metric': False,
        'format': '{condition_text} {condition_temp}°',
        'padding': widget['padding'],
    })

    thermalsensor = widget.copy()
    thermalsensor.update({
        'fontsize': widget['fontsize'],
        'font': widget['font'],
        'padding': widget['padding'],
    })

    notify = widget.copy()
    # notify.update({
    #     'text': "dfsdfdf",
    # })

    backlight = widget.copy()
    backlight.update({
        'fontsize': widget['fontsize'],
        'font': widget['font'],
        'padding': widget['padding'],
    })

    keyboard = widget.copy()
    keyboard.update({
        'fontsize': widget['fontsize'],
        'font': widget['font'],
        'configured_keyboards': ['us', 'ru'],
        'padding': widget['padding'],
    })
