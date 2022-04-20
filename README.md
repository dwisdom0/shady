# Shady
Shady is a sketchy script to run a shell one-liner on every file on the filesystem using Python.
You can also use it on a different directory (i.e. not `/`) if you want.

# Quickstart

```shell
$ git clone https://github.com/dwisdom0/shady.git
. . .
$ python shady.py 'xxd <FILE>' .
00000000: 4d49 5420 4c69 6365 6e73 650a 0a43 6f70  MIT License..Cop
00000010: 7972 6967 6874 2028 6329 2032 3032 3220  yright (c) 2022
00000020: 4461 7669 6420 5769 7364 6f6d 0a0a 5065  David Wisdom..Pe
00000030: 726d 6973 7369 6f6e 2069 7320 6865 7265  rmission is here

. . .

00000000: 2320 5368 6164 790a 5368 6164 7920 6973  # Shady.Shady is
00000010: 2061 2073 6b65 7463 6879 2073 6372 6970   a sketchy scrip
00000020: 7420 746f 2072 756e 2061 2073 6865 6c6c  t to run a shell
00000030: 206f 6e65 2d6c 696e 6572 206f 6e20 6576   one-liner on ev
. . .
```

Shady will replace `<FILE>` in your command with each specific file and print any output.
It's like 10 lines of Python so if you want to make it do something else it shouldn't be too hard.

### Tips
* `sudo` just works and doesn't prompt you for a password or anything
    * Hence "sketchy"

