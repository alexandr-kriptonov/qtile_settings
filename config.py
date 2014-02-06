from libqtile.config import Key, Screen, Group
from libqtile.command import lazy
from libqtile import layout, bar, widget

mod = "mod4"

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

groups = [
    Group("1"),
    Group("2"),
    Group("3"),
    Group("4"),
    Group("5"),
    Group("6"),
    Group("7"),
    Group("8"),
]
for i in groups:
    # mod1 + letter of group = switch to group
    keys.append(
        Key([mod], i.name, lazy.group[i.name].toscreen())
    )

    # mod1 + shift + letter of group = switch to & move focused window to group
    keys.append(
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name))
    )

dgroups_key_binder = None
dgroups_app_rules = []

layouts = [
    layout.Max(),
    layout.Stack(stacks=2)
]

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.TextBox("default config", name="default"),
                widget.Systray(),
                widget.Clock('%Y-%m-%d %a %I:%M %p'),
            ],
            30,
        ),
    ),
]

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
    Screen(top = bar.Bar([
        # This is a list of our virtual desktops.
        widget.GroupBox(urgent_alert_method='text'),

        # A prompt for spawning processes or switching groups. This will be
        # invisible most of the time.
        widget.Spacer(),
        widget.Prompt(),

        # Current window name.
        # widget.WindowName(),
        # widget.Volume(),
        # widget.Battery(
        #     energy_now_file='charge_now',
        #     energy_full_file='charge_full',
        #     power_now_file='current_now',
        # ),
        widget.Systray(),
        widget.Clock('%Y-%m-%d %a [%H:%M] %p'),
    ], 30)) # our bar is 30px high
]
