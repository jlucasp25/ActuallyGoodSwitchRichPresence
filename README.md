# ActuallyGoodSwitchRichPresence

An application to display Nintendo Switch games on the Discord Rich Presence service. 

It contains a graphical interface to choose the game. 

All the supported games are included in the database.json file.

Because of the way Discord RP works, the game images need to be uploaded manually.

### Requirements
- Python
- Tkinter
- Discord

### Compatibility Notes

macOS comes bundled with a deprecated version of Tkinter. To use this app you need to install Python directly from https://python.org/. The Python installers from <i>brew</i> mantain the deprecated Tkinter version.

(Tested on macOS 11.0.1 w/ Python 3.9.1)

### Instructions
-     pip install -r requirements.txt
      python3 main.py

### Future changes
<ul>
<li>Raise exception when the app can't connect to Discord.</li>
<li>Improved GUI.</li>
<li>Code Documentation.</li>
<li>More games and pictures added to the database.</li>
</ul>
<hr/>
<b>Goals</b>
<ul>
    <li>v1.0 - Choose games from a preset list.</li>
    <li>v2.0 - Detect the game using some sort of NSO API (if possible).</li>
    <li>v3.0 - Switch Port as a sysmodule to automate the task.</li>
</ul>
<hr/>
Game titles will be placed on the database.json file with the following format:

```
{
  "games": {
    "51 Worldwide Games": {
      "image_code": "51wg",
      "title": "51 Worldwide Games",
      "description": "Nintendo"
    },
    "Super Mario 3D All-Stars": {
      "image_code": "sm3as",
      "title": "Super Mario 3D All-Stars",
      "description": "Nintendo"
    }
  }
}
```
You can add new entries manually but the image code is limited to the ones submitted on the Discord Developer Portal.
The title must be present on the key for each entry.

I'll add a placeholder picture to use on other games later.
