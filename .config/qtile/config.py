# FNC Corps Qtile Config 

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.widget import backlight
from libqtile.command import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration
import os.path
import subprocess

mod = "mod4"
#terminal = guess_terminal()
terminal = 'kitty'
browser = 'firefox'

# Color Palette
# Tokyo Night Theme: https://github.com/enkia/tokyo-night-vscode-theme
color1 = "#f7768e"  # This keyword, HTML elements, Regex Group Symbol, CSS Units
color2 = "#ff9e64"
color3 = "#e0af68"
color4 = "#9ece6a"
color5 = "#73daca"
color6 = "#b4f9f8"
color7 = "#2ac3de"
color8 = "#7dcfff"
color9 = "#7aa2f7"
color10 = "#bb9af7"
color11 = "#c0caf5"
color12 = "#a9b1d6"
color13 = "#9aa5ce"
color14 = "#cfc9c2"
color15 = "#565f89"
color16 = "#414868"
color17 = "#24283b" # Editor Background (Storm)
color18 = "#1a1b26" # Editor Background (Night)

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

    # Switch between windows:
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),

    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),

    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),

    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "shift"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "shift"], "Up", lazy.layout.grow_up(), desc="Grow window up"),

    # Toggle between different layouts as defined below
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),

    # Kill Focused Window
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    # Focus/Unfocus Window
    Key([mod], "w", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),

    # Reload/Shutdown Qtile
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Shortcuts to open applications:
    Key([mod], "t", lazy.spawn(terminal), desc="Launch terminal"), # Launches the Terminal
    Key([mod], "f", lazy.spawn(browser)), # Launches Firefox
    Key([mod], "e", lazy.spawn("dolphin")), # Launches Dolphin
    Key([mod], "d", lazy.spawn("obsidian")), # Launches Obsidian
    Key([mod], "x", lazy.spawn("rhythmbox")), # Launches Rhythmbox
    Key([mod], "s", lazy.spawn("rofi -show drun")), # Launches rofi
    Key([], "Print", lazy.spawn("flameshot gui")), # Launches Flameshot

]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
        )


layouts = [
    layout.Columns(border_focus=color10, 
                   border_focus_stack=color10,
                   border_width=2,
                   margin=4,
                   grow_amount=6),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
#   layout.MonadTall(border_focus_stack=["#d75f5f", "#8f3d3d"], 
#                  border_width=2,
#                  margin=4),
    layout.Max(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="FiraCode Nerd Font Mono",
    fontsize=15,
    padding=4,
)
extension_defaults = widget_defaults.copy()


powerline = {
        "decorations": [
            PowerLineDecoration(path="forward_slash", padding_y=4)
            ]
        }

screens = [
    Screen(
        wallpaper=os.path.join(os.path.expanduser("~"), ".config/qtile/wallpaper_qtile/wall2.jpg"),
        wallpaper_mode='fill',

        top=bar.Bar(
            [
                widget.CurrentLayout(background=color9, **powerline,
                                     foreground=color18),
                widget.GroupBox(background=color16, **powerline,
                                foreground=color9,
                                hide_unused=False,
                                borderwidth=2,
                                border=color9,
                                disable_drag=True,
                                highlight_method='block'),
                widget.Prompt(background=color16, **powerline,
                              foreground=color9),
                widget.WindowName(background=color18, **powerline,
                                  foreground=color12),

                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),

                widget.Systray(padding = 4,
                             background=color16, **powerline,
                             foreground=color9
                               ),
                widget.Battery(update_interval=45,
                               padding=4,
                               notification_timeout=4,
                               discharge_char='-',
                               charge_char='+',
                               format='{char} {percent:2.0%}',
                               background=color9, **powerline,
                               foreground=color18,
                               unknown_char='+'
                               ),
                widget.ThermalSensor(
                    fmt = 'CPU:{}',
                    padding=4,
                    background=color16, **powerline,
                    foreground=color9
                    ), 
                widget.Volume(fmt = 'Vol:{}',
                              background=color9, **powerline,
                              foreground=color18),
#               widget.Backlight(brightness_file='/sys/class/backlight/amdgpu_bl0/max_brightness'),
                widget.Clock(format="%Y年%m月%d日 [%I:%M]",
                             background=color16, **powerline,
                             foreground=color9
                             ),
#               widget.Wallpaper(directory='~/.config/qtile/wallpaper_qtile/'),
                widget.QuickExit(background=color9, **powerline,
                                 foreground=color18,
                                 default_text='',
                                 countdown_start=4,
                                 countdown_format='{}'),
            ],
            28,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="feh"),  # feh
        Match(wm_class="kate"),  # kate
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "focus"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# Bind Caps Lock to Escape:
subprocess.run(["xmodmap", "-e", "clear Lock", "-e", "keycode 0x42 = Escape"])

# Autostart apps such as Network Manager Applet.
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

