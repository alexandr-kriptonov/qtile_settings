from libqtile.config import Key, Screen, Group
from libqtile.command import lazy
from libqtile import layout, bar, widget
from theme import Theme

mod = "mod4"
MOD = 'mod4'

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

    # Swap panes of split stack
    Key(
        [mod, "shift"], "space",
        lazy.layout.rotate()
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

# groups = [
#     Group("1"),
#     Group("2"),
#     Group("3"),
#     Group("4"),
#     Group("5"),
#     Group("6"),
#     Group("7"),
#     Group("8"),
# ]
# for i in groups:
#     # mod1 + letter of group = switch to group
#     keys.append(
#         Key([mod], i.name, lazy.group[i.name].toscreen())
#     )

#     # mod1 + shift + letter of group = switch to & move focused window to group
#     keys.append(
#         Key([mod, "shift"], i.name, lazy.window.togroup(i.name))
#     )

##-> Groups
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
    keys.append(Key([MOD], hotkey, lazy.group[name].toscreen()))
    keys.append(Key([MOD, 'shift'], hotkey, lazy.window.togroup(name)))

dgroups_key_binder = None
dgroups_app_rules = []

# layouts = [
#     layout.Max(),
#     layout.Stack(stacks=2)
# ]

layouts = (
    layout.Tile(ratio=0.5),
    layout.Max(),
)

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
    #'skype',
    'Update',  # Komodo update window
    'Xephyr',
    'Skype',
    'skype',
    'sublime-text',
)])


# screens = [
#     Screen(
#         bottom=bar.Bar(
#             [
#                 widget.GroupBox(),
#                 widget.Prompt(),
#                 widget.WindowName(),
#                 widget.TextBox("default config", name="default"),
#                 widget.Systray(),
#                 widget.Clock('%Y-%m-%d %a %I:%M %p'),
#             ],
#             30,
#         ),
#     ),
# ]

main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating()
mouse = ()
auto_fullscreen = True
widget_defaults = {}


# screens = [
#     Screen(top=bar.Bar([
#         widget.GroupBox(),    # display the current Group
#         widget.Spacer(),
#         # widget.BatteryIcon(),
#         widget.CPUGraph(),
#         widget.Canto(),
#         # widget.Maildir(),R
#         widget.Prompt(),
#         widget.Notify(),
#         widget.Battery(),      # display the battery stateRR
#         widget.Sep(),
#         widget.Volume(),
#         widget.CurrentLayout(),
#         widget.Clock(),
#         widget.Systray(),
#        ], 30))
#    ]
screens = [
    Screen(
        top = bar.Bar([
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
            widget.ThermalSensor(),
            widget.Sep(**Theme.sep),
            widget.CurrentLayout(**Theme.widget),
            widget.Sep(**Theme.sep),
            widget.Systray(**Theme.systray),
            widget.Sep(**Theme.sep),
            widget.Clock(**Theme.clock),
    ], **Theme.bar)) # our bar is 35px high
]
