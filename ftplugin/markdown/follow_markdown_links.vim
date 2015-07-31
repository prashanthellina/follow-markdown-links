if exists("*FollowLink")
    finish
endif

" --------------------------------
" Add plugin to the path
" --------------------------------
python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))

function! FollowLink()
python << endOfPython

from follow_markdown_links import follow_link
follow_link()

endOfPython
endfunction

command! FollowLink call FollowLink()
nnoremap <script> <CR> :FollowLink<CR>
nnoremap <script> <BS> :e#<CR>
