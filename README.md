# follow-markdown-links

This vim plugin enables browsing through your markdown files by using links between them (like a personal wiki). You just have to move the cursor to a link and press ENTER.

Example of links

- `[Notes](Notes.md)` or `[Notes]()` or `[Notes](Notes)` will open Notes.md
- `[SubNotes](sub/Notes.md)` or `[sub/Notes]()` or `[Notes](sub/Notes)` will open sub/Notes.md (if `sub` directory does not exist, the plugin will prompt for confirmation and create)

You can press BACKSPACE to navigate to previous file (like "e#").

## Installation

Use your plugin manager of choice.

- [Pathogen](https://github.com/tpope/vim-pathogen)
  - `git clone https://github.com/prashanthellina/follow-markdown-links ~/.vim/bundle/follow-markdown-links`
- [Vundle](https://github.com/gmarik/vundle)
  - Add `Bundle 'https://github.com/prashanthellina/follow-markdown-links'` to .vimrc
  - Run `:BundleInstall`
- [NeoBundle](https://github.com/Shougo/neobundle.vim)
  - Add `NeoBundle 'https://github.com/prashanthellina/follow-markdown-links'` to .vimrc
  - Run `:NeoBundleInstall`
- [vim-plug](https://github.com/junegunn/vim-plug)
  - Add `Plug 'https://github.com/prashanthellina/follow-markdown-links'` to .vimrc
  - Run `:PlugInstall`
