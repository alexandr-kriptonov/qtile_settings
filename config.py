from libqtile.config import Key, Screen, Group
from libqtile.manager import Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget
from theme import Theme

mod = "mod4"
alt = "mod1"
screenshot = 'scrot'
file_manager = 'pcmanfm'

#   Key shourtcuts Config
# -------------------
keys = [
    # Switch between windows in current stack pane
    Key(
        [mod], "k",
        lazy.layout.down()
    ),
    Key(
        [mod], "j",
        lazy.layout.up()
    ),

    # Move windows up or down in current stack
    Key(
        [mod, "control"], "k",
        lazy.layout.shuffle_down()
    ),
    Key(
        [mod, "control"], "j",
        lazy.layout.shuffle_up()
    ),

    # Switch window focus to other pane(s) of stack
    Key(
        [mod], "space",
        lazy.layout.next()
    ),

    Key([mod], 'e', lazy.spawn(file_manager)),
    Key([mod], 'p', lazy.spawn(screenshot)),

    # Swap panes of split stack
    Key(
        [mod, "shift"], "space",
        lazy.layout.rotate()
    ),

    Key(
        [alt], "r",
        lazy.spawn(
            "dmenu_run -b -fn 'Terminus:size=14' -nb '#000000' -nf '#fefefe'")
    ),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"], "Return",
        lazy.layout.toggle_split()
    ),
    Key([mod], "Return", lazy.spawn("rxvt-unicode")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab",    lazy.nextlayout()),
    Key([mod, "shift"], "c",      lazy.window.kill()),

    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod], "r", lazy.spawncmd()),
]

#   Group Config
# -------------------
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
    ('SUBL', {'layout': 'max', }),
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

#   Mouse Config
# -------------------
mouse = [
    Drag([alt], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([alt], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([alt], "Button2", lazy.window.bring_to_front())
]

main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating()
mouse = ()
auto_fullscreen = True
widget_defaults = {}

#   Widgets Config
# -------------------
screens = [
    Screen(
        top=bar.Bar([
            widget.GroupBox(**Theme.groupbox),
            widget.Sep(**Theme.sep),
            widget.Spacer(),
            # widget.CPUGraph(graph_color='18BAEB', fill_color='1667EB.3', **Theme.graph),
            widget.Prompt(),
            widget.Sep(**Theme.sep),
            widget.MemoryGraph(graph_color='00FE81', fill_color='00B25B.3', **Theme.graph),
            widget.Sep(**Theme.sep),
            widget.NetGraph(graph_color='ffff00', fill_color='4d4d00', interface='eth0',  **Theme.graph),
            widget.Sep(**Theme.sep),
            widget.ThermalSensor(**Theme.thermalsensor),
            widget.Sep(**Theme.sep),
            widget.HDDGraph(graph_color='f72900', fill_color='4d4d00',  **Theme.graph),
            widget.Sep(**Theme.sep),
            widget.KeyboardLayout(),
            widget.Sep(**Theme.sep),
            widget.CurrentLayout(**Theme.widget),
            widget.Sep(**Theme.sep),
            widget.Systray(**Theme.systray),
            widget.Sep(**Theme.sep),
            widget.Clock(**Theme.clock), ],
            **Theme.bar))]


#   Layouts Config
# -------------------

# Layout Theme
layout_theme = {
    "border_width": 2,
    "margin": 3,
    # "border_focus": "#5524555",
    # "border_normal": "#5534555"
}

layouts = [
    layout.Max(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Stack(stacks=2, **layout_theme),
    layout.Tile(shift_windows=True, **layout_theme),
    layout.Slice(
        'left',
        192,
        name='slice',
        role='gimp-toolbox',
        fallback=layout.Slice('right', 256, role='gimp-dock',
        fallback=layout.Stack(stacks=1, **layout_theme))),
]

floating_layout = layout.floating.Floating(float_rules=[{'wmclass': x} for x in (
    #'audacious',
    'Download',
    'dropbox',
    'file_progress',
    'file-roller',
    'gimp',
    'Komodo_confirm_repl',
    'Komodo_find2',
    'pidgin',
    'skype',
    'Update',
    'Xephyr',
    'Skype',
    'skype',
    'sublime-text', )],
    **layout_theme)
