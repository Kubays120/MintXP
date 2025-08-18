🪟🪟 **MintXP – Windows XP motiv pro Linux Mint** 🪟🪟
====================================================

💻 **Přeměňte svůj Linux Mint na Windows XP!**  
Zažijte ikonický vzhled Windows XP přímo na Linux Mint – autentické motivy, ikony, ukazatele myši a legendární „Winver“ pro kompletní retro zážitek.

✨ **Co projekt obsahuje:**
- 🎨 **Theme** – motivy, ikony a ukazatele myši pro autentický Windows XP vzhled.  
- 🪟 **Winver** – skript pro zobrazení informace o systému ve stylu Winver z Windows XP.  
- ⚡ **Install Script** – automatizovaný skript `install.sh`, který vše nastaví bez ručního kopírování souborů.

🔧 **Jak nastavit MintXP:**

1. Naklonujte repositář do vámi vybraného adresáře:
   ```bash
   git clone https://github.com/Kubays120/MintXP.git
   cd MintXP
   
2. Udělejte instalační skript spustitelný a spusťte ho:
   ```bash
   chmod +x install.sh
   ./install.sh
3. Skript automaticky:
   - Zkopíruje .icons a .themes do domovského adresáře /home/$USER.
   - Zkopíruje složku Winver do /home/$USER.
   - Nastaví motivy vzhledu Linux Mint:
      - Ukazatel myši: ModernXP
      - Aplikace: Windows XP Luna
      - Ikony: Windows-XP-3.1
   - Pracovní plocha: Windows XP Luna
   - Vytvoří spouštěč pro Winver, který jej spustí přes Python 3.
4. Winver lze kdykoli spustit přes příkaz:
      ```bash
      python3 ~/Winver/winner.py
   nebo z menu Linux Mint, pokud použijete spouštěč vytvořený skriptem.

  **‼️ VAROVÁNÍ ‼️**
----------------------

Nepřemisťujte soubory z jejich cílových adresářů – program by mohl přestat fungovat. 
Postupujte přesně podle instalačního skriptu a instrukcí.
