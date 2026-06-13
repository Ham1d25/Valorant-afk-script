# Valorant Anti-AFK Script 🤖🎮

A lightweight Python script designed to simulate random player movement and actions to prevent being kicked for inactivity (AFK). It uses direct input simulation to ensure keystrokes register correctly in-game.

> ⚠️ **Disclaimer:** This project is for educational and personal use only. Using automation scripts or anti-AFK tools in competitive multiplayer games like *Valorant* violates Riot Games' Terms of Service and can result in a permanent account ban. Use at your own risk.

---

## ✨ Features

* **Direct Input Simulation:** Uses `pydirectinput` to simulate keyboard actions that standard GUI automation libraries often fail to register in games.
* **Randomized Movement:** Simulates realistic delays and randomly moves the character in four directions (`W`, `A`, `S`, `D`) for 1 to 3 seconds.
* **Randomized Actions:** Periodically simulates primary actions (like shooting or ability usage via `L` and `K` keys) to further mimic active gameplay.
* **Easy Safety Stop:** Instantly terminates the script loop at any time by pressing the `Esc` key.

---

## 🛠️ How It Works

1. **Initialization:** The script waits for you to press the `Alt` key.
2. **Countdown:** Once triggered, it gives you a **3-second window** to switch your window focus back into the game.
3. **Loop:** It enters a continuous loop of moving and "shouting" (shooting/actions) until stopped.
4. **Exit:** Pressing `Esc` cleanly breaks the loop and unhooks the keyboard listeners.

---

## 🚀 Prerequisites

Before running the script, make sure you have Python installed and the required dependencies:

```bash
pip install pydirectinput keyboard
