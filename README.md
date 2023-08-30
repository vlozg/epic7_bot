<div align="center">
<p align="center">
<img src="https://github.com/brunocordioli072/epic7_bot/assets/46489264/7733c50a-51ec-4b08-b31c-4ad97e3cca66">
</p>

<h1 align="center">
Epic7 Bot
</h1>

[![GitHub Stars](https://img.shields.io/github/stars/brunocordioli072/epic7_bot?style=flat-square)](https://github.com/brunocordioli072/epic7_bot/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/brunocordioli072/epic7_bot?style=flat-square)](https://github.com/brunocordioli072/epic7_bot/network)
[![GitHub Issues](https://img.shields.io/github/issues/brunocordioli072/epic7_bot?style=flat-square)](https://github.com/brunocordioli072/epic7_bot/issues)
[![GitHub Contributors](https://img.shields.io/github/contributors/brunocordioli072/epic7_bot?style=flat-square)](https://github.com/brunocordioli072/epic7_bot/graphs/contributors)
[![GitHub License](https://img.shields.io/github/license/brunocordioli072/epic7_bot?style=flat-square)](https://github.com/brunocordioli072/epic7_bot/blob/main/LICENSE)
</div>

Epic7 Bot is a [Epic 7](https://epic7.smilegatemegaport.com/) toolkit/bot used via cli to perform automated actions inside the game. All actions are **cheat detection proof** by doing only randomized click inputs inside the emulator screen.

## Future Goals

- [x] Secret shop refreshing.
- [x] Hunt battling.
- [ ] Labyrith.
- [ ] Automation Tower.
- [ ] Hunt Expedition
- [ ] Spirit Altar
- [x] Arena NPC battling.
- [x] All daily actions, like daily summon and pet summon, sanctuary daily rewards, guild donations, etc;
- [ ] GUI development.
- [ ] Create a .exe installer.

## Usage

- Enable Android Debug Bridge(ADB) on your emulator of choice. **(more stable on Bluestacks)**
    - Bluestacks: Settings > Advanced > Enable Android Debug Bridge
    - Nox: Settings > Device > Enable Network Bridge Mode

```
epic7 --help
Usage:
    epic7 <command> [options]

All commands should be run when the game screen is in the lobby!

The most commonly used commands are:
    shop            Start secret shop auto buy
    arena           Start arena npc auto battle
    hunt            Start hunt auto battle
    daily           Start daily actions

Options:
    -h --help       Show this help message and exit
    -v --version    Show version and exit
```


## Working
<div align="center">
    
![shop-mp4](https://github.com/brunocordioli072/epic7_bot/assets/46489264/bae8b85b-e08c-46d6-91d9-cf64369e4923)

*Bluestacks running Epic7 on top and Windows Powershell running the epic7-bot commands on the bottom.*

</div>

## Requirements
- [Chocolatey](https://chocolatey.org/)
- [Android Debug Bridge (adb)](https://community.chocolatey.org/packages/adb)
- [Python 3.4+](https://www.python.org/downloads/release/python-392/)

## Instalation

```bash
pip install epic7-bot
```
## Contributions

[Issue & Report a Bug](https://github.com/brunocordioli072/epic7_bot/issues/new/choose) | [Fork & Open a New PR](https://github.com/brunocordioli072/epic7_bot/compare)

All kinds of contributions including enhancements, new features, code improvements, issues and bugs reporting are welcome.

- The `main` branch of Epic7 Bot is the stable version, and all development is done in the `development` branch. So if you want to open a Pull Request, your commits need to be submitted to the `development` branch.

⭐ If you like it, give it a star~ ⭐

## Contributors

Thanks to the following contributors for their contributions to this project.

<a href="https://github.com/brunocordioli072/epic7_bot/graphs/contributors">

  <img src="https://contrib.rocks/image?repo=brunocordioli072/epic7_bot" />

</a>
