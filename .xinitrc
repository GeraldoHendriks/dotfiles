$HOME/.screenlayout/Work.sh
picom &
nitrogen --restore &
nm-applet &
blueberry-tray &

exec dbus-launch --exit-with-session qtile start
