# rephp.nvim - Read and Evaluate PHP
![rephp](http://snow-dev.com/wp-content/uploads/2016/12/rephp.gif)
## Description
rephp.nvim is a python3 plugin for neovim, which reads different regions of your code, evaluates it and echo (if there are any outputs). The idea is inspired by great REPLs like Clojures Cider. 
This plugin tries to deliver a similar feeling, but in a far more basic fashion.  
### What is implemented so far  
&#x2713; Evaluate current line  
&#x2713; Evaluate all selected lines  
&#x2718; Evaluate the current buffer  

## Requirements
Neovim needs to be installed with if_python3. If ```:echo has("python3")``` returns 1, then you're good to go.

Otherwise you can enable the python3 interface with pip:

```pip3 install neovim```

## Installation
### vim-plug

```Plug 'snowiow/rephp.nvim', {'do': ':UpdateRemotePlugins'}```
## Configuration
The best way to use this plugin, is to create two new keybindings for the normal and visual mode calls:  
```
nnoremap <leader>l :call RePhp('n')<CR>
vnoremap <leader>l :<C-u>call RePhp('v')<CR>
```
Here you can set ```<leader>l``` to any other shortcut you like.  

If the PHP executable is not in your path, you also need to give the real path to the plugin  

```let g:rephp_executable = '/usr/bin/php'```  
Where the string after the equal sign should be the full path to your php executable.
