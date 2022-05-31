# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.utils import guess_terminal 
from typing import List  # noqa: F401


mod = "mod1"
terminal = guess_terminal()

keys = [

    # Custom launch commands
    # Key([mod], "r", lazy.spawncmd(), desc="Launch Prompt"),
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Launch Prompt"),
    Key([mod], "w", lazy.spawn("firefox"), desc="Launch Brave"),
    Key([mod], "e", lazy.spawn("emacs"), desc="Launch emacs"),
    Key([mod], "f", lazy.spawn("pcmanfm"), desc="Launch Pcmanfm"),
    Key([], "Print", lazy.spawn("flameshot gui"), desc="Launch Flameshot"),

    # Custom floating toggle
    Key([mod, "shift"], "p", lazy.window.toggle_floating()),

    # Custom media commands
    Key([], "XF86AudioMute", lazy.spawn("amixer sset Master playback toggle"), desc="Mute"),
    # Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer sset Master playback 2%+"), desc="Volume up"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5"), desc="Volume up"),
    # Key([], "XF86AudioLowerVolume", lazy.spawn("amixer sset Master playback 2%-"), desc="Volume dowm"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5"), desc="Volume up"),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Play/Pause current playing media"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Play next media"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Pause next media"),


    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key(["mod4"], "l", lazy.spawn("xlock -mode space"), desc="Lock screen"),
]


#############################################################
# @hook.subscribe.startup_once                              #
# def start_once():                                         #
#     home = os.path.expanduser('~')                        #
#     subprocess.call([home + '/.config/polybar/start.sh']) #
#############################################################


group_names = [("I"),
               ("II"),
               ("III"),
               ("IV"),
               ("V"),
               ("VI")]

groups = [Group(name) for name in group_names]

for i, (name) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

colors = ["#282828", # 0 bg
          "#cc241d", # 1 red
          "#98971a", # 2 green
          "#d79921", # 3 yellow
          "#928374", # 4 grey
          "#ebdbb2", # 5 fg
          "#504945", # 6 bg2
          ]

layout_theme = {"border_width": 2,
                "margin": 15,
                "border_focus": colors[4],
                "border_normal": colors[6]
                }


layouts = [
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(**layout_theme),
    # layout.Matrix(),
    # layout.MonadTall(**layout_theme),
    # layout.MonadWide(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.Tile(**layout_theme),
    # layout.TreeTab(**layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Zoomy(**layout_theme),
]

widget_defaults = dict( font='sans',
    fontsize=12,
    padding=3,
    background=colors[0],
    foreground=colors[5]
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
    #     top=bar.Bar(
    #         [
    #             widget.CurrentLayoutIcon(
    #                 scale=0.5,
    #             ),
    #             widget.WindowName(),
    #             widget.GroupBox(
    #                 fontsize= 16,
    #                 active = colors[5],
    #                 inactive = colors[4],
    #                 rounded = False,
    #                 highlight_color = colors[6],
    #                 highlight_method = "line",
    #                 this_current_screen_border = colors[4],
    #                 this_screen_border = colors [4],
    #                 other_current_screen_border = colors[4],
    #                 other_screen_border = colors[4],
    #             ),
    #             widget.Spacer(),
    #             widget.WidgetBox(
    #                 font='FontAwesome',
    #                 fontsize= 16,
    #                 close_button_location="right",
    #                 text_closed='',
    #                 text_open='',
    #                 widgets=[
    #                     widget.Systray(),
    #                 ]
    #             ),
    #             widget.Spacer(
    #                 length=5
    #             ),
    #             widget.TextBox(
    #                 fontsize= 16,
    #                 text='墳 '
    #             ),
    #             widget.Volume(),
    #             widget.Spacer(
    #                 length=5,
    #             ),
    #             widget.TextBox(
    #                 text='  '
    #             ),
    #             widget.Battery(
    #                 format='{percent:2.0%}  {char}',
    #             ),
    #             widget.Spacer(
    #                 length=5
    #             ),
    #             widget.Clock(
    #                 format='%m-%d %H:%M',
    #             ),
    #             widget.Spacer(
    #                 length=5
    #             ),
    #         ],
    #         32,
    #         # margin=[15, 15, 0, 15],
    #     ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod, "shift"], "Button1", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "Qtile"
