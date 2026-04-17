# Sigil of Uchma
[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

Sigil of Uchma is a work-in-progress tabletop role playing game. The game is currently in beta stage and actively in development.

You can start reading the rules from [this website](https://sigil.tyghsh.cc). If you want to read the in-development version instead, check out [the test website](https://sigil-test.tyghsh.cc).

You can send feedback from this form: https://forms.gle/7NwTYqGUWpBfBWNg8.

This repository is for keeping track of changes to the game rules between versions. It may or may not be up to date. Playable books will be posted in the releases page after they are made publicly available.

# Contributing
Feel free to submit a pull request, but you must read [the introduction](https://taygahoshi.github.io/tt-project/sigil-of-uchma/introduction.html). You can contribute to most of the places labeled with "#TODO". I use [Obsidian](https://obsidian.md/) to edit of these notes, so this project uses [Obsidian Flavored Markdown](https://help.obsidian.md/Editing+and+formatting/Obsidian+Flavored+Markdown) except for this README.md file.

To contribute, you can simply fork this repository, then clone your fork into Obsidian or any equivalent software:
```bash
cd /path/to/obsidian/vault
git clone your-fork
```

Then you can create a git branch, make your changes, and create a commit:
```bash
git checkout -b your-feature-name
# make your changes here
git add -A
git commit -m "useful commit mesage"
git push
```

Alternatively, you can go to your fork repository and press "." (dot). This opens your repository in a text editor, and you can commit directly from there. 

Lastly, you can send a pull request to my repository through GitHub.

# Project Structure
```
├── .hugo -> used for website generation
├── Character - Branches
├── Character - Paths
├── Content
├── Equipment
├── Items
├── Monsters
├── INTRODUCTION.md -> Starting point
├── LICENCE.md
└── README.md -> You are here
```

# Licence
This work is licensed under the
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

Sigil of Uchma consists of assets in the form of gameplay rules, art, music,
books, e-books and more. Assets may or may not be in this repository. Unless
explicitly stated otherwise, all assets share this licence. See
[LICENCE - Game Rules.md](LICENCE%20-%20Game%20Rules.md) for the full text.

Unless explicitly stated otherwise, files under the `.hugo/` directory, including website assets, code, scripts and
other files, are licensed under the GNU General Public License v3.0 or later.
See [LICENCE - Code.md](LICENCE%20-%20Code.md) for the full text.

Bundled third-party assets are distributed under their own licences:

| Asset              | Licence                                                                         | Directory                        |
| ------------------ | ------------------------------------------------------------------------------- | -------------------------------- |
| Liberation Serif   | [SIL Open Font License 1.1](https://scripts.sil.org/OFL)                        | .hugo/static/fonts               |
| Hugo Relearn Theme | [MIT License](https://github.com/McShelby/hugo-theme-relearn/blob/main/LICENSE) | .hugo/themes/hugo-theme-relearn/ |

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg