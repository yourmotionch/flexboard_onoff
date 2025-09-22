# Flexboard On/Off Installer

**Copyright © 2025 [Yourmotion.ch](https://yourmotion.ch) & [Flexboard.ch](https://flexboard.ch)**  
All rights reserved. Proprietary software – usage requires explicit authorization from Yourmotion.ch and Flexboard.ch.

---

## 📦 Installation

Clone this repository and run the installer script.  
This will automatically configure the autostart of your `ws.py` script via `cron`.

```bash
git clone https://github.com/yourmotionch/flexboard_onoff.git
python3 flexboard_onoff/installer.py
```

---

## ⚡ One-liner alternative

Run everything in one command:

```bash
git clone https://github.com/yourmotionch/flexboard_onoff.git && python3 flexboard_onoff/installer.py
```
## 🔘 Installation of the Power Button on Dakboard

To control your Flexboard screen from Dakboard, follow these steps:

1. **Open your Dakboard screen** (edit mode).
2. Click on **"Add a Block"**.
3. Search for **"Button/Link"**.
4. Configure the button:
   - **Type** → Select **URL**  
   - **URL** → `http://localhost:8881/poweroff`  
   - **Action** → Select **"Open In Background"**
5. **Icon**: Click to add, then search for the **"Power Off"** icon.
6. **Formatting Tab**:
   - **Style** → `Link`  
   - **Color** → `Grey`  
   - **Blur** → `Disabled`  
   - **Text Size** → `36`
7. **Position** → Move the button to your preferred location on the screen.

✅ After saving, you will have a **Power Off** button directly on your Dakboard screen, triggering the shutdown via your Flexboard On/Off service.


---

## 🔎 Verification

After reboot, check that the service is running by inspecting the log file:

```bash
tail -n 200 flexboard_onoff/ws.log
```

If the script started correctly, you will see timestamps and log entries from your application.

---

## ❌ Uninstall

To remove the autostart configuration, simply edit your crontab:

```bash
crontab -e
```

Delete the line starting with:

```
@reboot sh -c 'cd /path/to/flexboard_onoff; sleep 10; python3 ws.py >> ws.log 2>&1'
```

Save and exit.  
After the next reboot, the script will no longer start automatically.

---

## 🛡 License

This software is proprietary and confidential.  
Unauthorized copying, modification, distribution, or use of this software, in whole or in part, without prior written permission from **Yourmotion.ch** or **Flexboard.ch**, is strictly prohibited.

For licensing inquiries, please contact:

- Yourmotion.ch — contact@yourmotion.ch  
- Flexboard.ch  — contact@flexboard.ch
