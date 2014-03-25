from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.layout import floating
from theme import Theme

screenshot = 'scrot screenshot.png'
filemanager = "thunar"

############################# KEYBOARD BINDINGS ################################

mod = "mod4"

keys = [

    Key(
        [mod, "shift"],
        "q",
        lazy.shutdown()
    ),
    Key(
        [mod, "shift"],
        "r",
        lazy.restart()
    ),
    Key(
        [mod, "shift"],
        "c",
        lazy.window.kill()
    ),
    Key(
        [mod],
        "r",
        lazy.spawn("dmenu_run -b -fn 'Terminus:size=14' -nb '#000000' -nf '#fefefe'")
    ),
    Key(
        [mod],
        "Return",
        lazy.spawn("rxvt-unicode")
    ),
    Key(
        [mod],
        "k",
        lazy.layout.up()
    ),
    Key(
        [mod],
        "j",
        lazy.layout.down()
    ),
    Key(
        [mod],
        "Tab",
        lazy.layout.up()
    ),
    Key(
        [mod, "shift"],
        "Tab",
        lazy.layout.down()
    ),
    Key(
        [mod],
        "h",
        lazy.layout.previous()
    ),
    Key(
        [mod],
        "l",
        lazy.layout.next()
    ),
    Key(
        [mod],
        "space",
        lazy.nextlayout()
    ),
    Key(
        [mod, "shift"],
        "space",
        lazy.prevlayout()
    ),
    Key(
        [mod],
        "Left",
        lazy.group.prevgroup()
    ),
    Key(
        [mod],
        "Right",
        lazy.group.nextgroup()
    ),
    Key(
        [mod, "shift"],
        "Left",
        lazy.to_next_screen()
    ),
    Key(
        [mod, "shift"],
        "Right",
        lazy.to_prev_screen()
    ),
    Key(
        [mod, "shift"],
        "space",
        lazy.layout.rotate()
    ),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split()
    ),
    Key(
        [], "XF86AudioRaiseVolume",
        lazy.spawn("amixer -c 0 -q set Master 2dB+")
    ),
    Key(
        [], "XF86AudioLowerVolume",
        lazy.spawn("amixer -c 0 -q set Master 2dB-")
    ),
    Key(
        [], "XF86AudioMute",
        lazy.spawn("amixer -c 0 -q set Master toggle")
    ),

    Key(
        [], "XF86ScreenSaver",
        lazy.spawn("xscreensaver-command -lock")
    ),
    Key(
        [mod],
        'e',
        lazy.spawn(filemanager)
    ),
    Key(
        [mod],
        'p',
        lazy.spawn(screenshot)
    ),
]

############################## MOUSE BINDINGS ##################################

mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag(
        [mod], "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
    Click(
        [mod],
        "Button2",
        lazy.window.bring_to_front())
]

##################################  GROUPS  ####################################

group_setup = (
    ('MAIN', {
        'layout': 'max',
        'apps': {'wm_class': ('Firefox', 'Google-chrome')},
    }),
    ('WWW', {
        'layout': 'max',
        'apps': {'wm_class': ('Komodo Edit',)},
    }),
    ('IM', {}),
    ('SUBL', {'layout': 'tile', }),
    ('URXVT', {
        'layout': 'max',
        'apps': {'wm_class': ('VirtualBox',)},
    }),
    ('FILE', {
        'layout': 'max',
        'apps': {'wm_class': ('audacious',)},
    }),
)

groups = []
for idx, (name, config) in enumerate(group_setup):
    hotkey = str(idx + 1)
    groups.append(Group(name, layout=config.get('layout', 'tile')))
    keys.append(Key([mod], hotkey, lazy.group[name].toscreen()))
    keys.append(Key([mod, 'shift'], hotkey, lazy.window.togroup(name)))

dgroups_key_binder = None
dgroups_app_rules = []

main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating()
mouse = ()
auto_fullscreen = True
widget_defaults = {}

##################################  LAYOUTS  ###################################

# Layout Theme
layout_theme = {
    "border_width": 3,
    "margin": 3,
    "border_focus": "#0038D4",
    "border_normal": "#555555"
}

layouts = [
    layout.Max(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Stack(stacks=2, **layout_theme),
    layout.Tile(shift_windows=True, **layout_theme),
    layout.TreeTab(),  # display tree windows on left
    # a layout just for gimp(stolen from tych0's config)
    layout.Slice(
        'left',
        192,
        name='gimp',
        role='gimp-toolbox',
        fallback=layout.Slice('right', 256, role='gimp-dock',
        fallback=layout.Stack(stacks=1, **layout_theme))
    ),
]

floating_layout = layout.Floating(
    auto_float_types=floating.DEFAULT_FLOAT_WM_TYPES,
    float_rules=[
        dict(wmclass="spotify"),
        dict(wmclass="gnome-calculator"),
        dict(wname="Unlock Login Keyring")
    ],
    **layout_theme
)


@hook.subscribe.client_new
def floating_dialogs(window):
    if(window.window.get_wm_type() == 'dialog' or window.window.get_wm_transient_for()):
        window.floating = True

screens = [
    Screen(
        top=bar.Bar([
            widget.GroupBox(**Theme.groupbox),
            widget.Sep(**Theme.sep),
            widget.Spacer(),
            # widget.CPUGraph(graph_color='18BAEB', fill_color='1667EB.3', **Theme.graph),
            widget.Sep(**Theme.sep),
            widget.MemoryGraph(graph_color='00FE81', fill_color='00B25B.3', **Theme.graph),
            widget.Sep(**Theme.sep),
            widget.NetGraph(graph_color='ffff00', fill_color='4d4d00', interface='wlan0',  **Theme.graph),
            widget.HDDGraph(graph_color='ffff00', fill_color='4d4d00',  **Theme.graph),
            widget.Sep(**Theme.sep),
            widget.BatteryIcon(**Theme.battery),
            widget.Battery(**Theme.battery_text),
            widget.Sep(**Theme.sep),
            widget.Wlan(**Theme.wifi),
            widget.Sep(**Theme.sep),
            widget.KeyboardLayout(**Theme.keyboard),
            widget.Sep(**Theme.sep),
            widget.CurrentLayout(**Theme.widget),
            # widget.Backlight(**Theme.backlight),
            widget.Sep(**Theme.sep),
            widget.Systray(**Theme.systray),
            widget.Sep(**Theme.sep),
            widget.Clock(**Theme.clock),
        ], **Theme.bar))
]
