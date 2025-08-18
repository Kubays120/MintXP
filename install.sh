#!/bin/bash
# MintXP Installer Script
# Tento skript nainstaluje motivy a Winver pro Linux Mint

echo "Spoustim instalaci MintXP..."

USER_HOME="$HOME"

# Kontrola, zda existuje složka MintXP
if [ ! -d "./MintXP" ]; then
    echo "Slozka MintXP nebyla nalezena! Spustte skript z adresare, kde je slozka MintXP."
    exit 1
fi

# Kopírování Theme (.icons a .themes)
echo "Kopiruji .icons a .themes do $USER_HOME..."
cp -r ./MintXP/Theme/.icons "$USER_HOME"/ 2>/dev/null
cp -r ./MintXP/Theme/.themes "$USER_HOME"/ 2>/dev/null

# Kopírování Winver
echo "Kopiruji slozku Winver do $USER_HOME..."
cp -r ./MintXP/Winver "$USER_HOME"/ 2>/dev/null

# Kontrola Python3
echo "Kontroluji instalaci Python3..."
if ! command -v python3 >/dev/null 2>&1; then
    echo "Python3 nebyl nalezen. Instaluji..."
    sudo apt update && sudo apt install -y python3
else
    echo "Python3 je jiz nainstalovan."
fi

# Nastavení motivů pomocí gsettings
echo "Nastavuji motivy..."
gsettings set org.cinnamon.desktop.interface cursor-theme "ModernXP"
gsettings set org.cinnamon.desktop.interface gtk-theme "Windows XP Luna"
gsettings set org.cinnamon.desktop.interface icon-theme "Windows-XP-3.1"
gsettings set org.cinnamon.desktop.wm.preferences theme "Windows XP Luna"

# Vytvoření spouštěče pro Winver
DESKTOP_FILE="$USER_HOME/.local/share/applications/winver.desktop"

echo "Vytvarim spoustec pro Winver..."
mkdir -p "$USER_HOME/.local/share/applications"

ICON_PATH="$USER_HOME/Winver/xp_icon.png"
if [ ! -f "$ICON_PATH" ]; then
    echo "Upozorneni: Ikona xp_icon.png nebyla nalezena. Pouziji vychozi ikonu."
    ICON_PATH="computer"
fi

cat > "$DESKTOP_FILE" <<EOL
[Desktop Entry]
Name=Winver
Comment=Windows XP About Simulator
Exec=python3 $USER_HOME/Winver/winver.py
Icon=$ICON_PATH
Terminal=false
Type=Application
Categories=Utility;
EOL

chmod +x "$DESKTOP_FILE"

echo "Instalace dokoncena."
echo "Winver lze spustit z menu (Start) nebo prikazem:"
echo "python3 ~/Winver/winver.py"