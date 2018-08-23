import re
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

from vim import *

DEFAULT_EXTENSION = 'md'
MAX_LINE_LEN = 1024

def _extract_link_under_cursor():
    _, col = current.window.cursor
    line = current.line

    # skip long lines to stop hogging CPU in vim
    if len(line) >= MAX_LINE_LEN:
        return

    # find the markdown link substring from line
    start_pos = line[:col].rfind("[")
    if start_pos < 0: return

    end_pos = line[col:].rfind(")")
    if end_pos < 0: return

    end_pos += (col + 1)

    link = line[start_pos:end_pos]
    return link

def _is_local_link(link):
    link = urlparse(link)
    return not link.netloc

def _resolve_link(link):
    buf_path = os.path.dirname(current.buffer.name)
    return os.path.join(buf_path, link)

def _ensure_extension(link):
    name = os.path.basename(link)
    if '.' not in name:
        return link + '.' + DEFAULT_EXTENSION

    return link

def follow_link():
    link = _extract_link_under_cursor()
    if not link: return

    # extract link text and link url
    link = re.findall(r'^\[([^]]*)\]\(([^)]*)\)$', link)
    if not link: return

    # if not local link then stop
    text, link = link[0]
    if not _is_local_link(link): return

    # Support [Text]() cases; Assume Text as link
    # Also assume default extension
    if not link: link = text
    link = _ensure_extension(link)

    # Resolve link (if relative) with relation
    # to current file in buffer
    link = _resolve_link(link)

    # Open if exists
    if os.path.exists(link):
        return command('e %s' % link)

    # Directory path does not exist. Ask user to create it.
    dirpath = os.path.dirname(link)
    if not os.path.exists(dirpath):
        confirm_fn = Function('confirm')
        msg = '"%s" does not exist. create?' % dirpath
        result = confirm_fn(msg, "&Yes\n&No")
        if result != 1: return
        os.makedirs(dirpath)

    # Open as new file
    return command('e %s' % link)
