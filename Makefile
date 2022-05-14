default: prepare install

clean:
	rm -rf ~/.config/qtile ~/.config/dunst ~/.config/picom ~/.config/alacritty ~/Pictures ~/.config/rofi

prepare:
	mkdir ~/Pictures ~/.config ~/.config/qtile ~/.config/dunst ~/.config/picom ~/.config/alacritty ~/Pictures ~/.config/rofi

install:
	cp ./wallpaper.png ~/Pictures/
