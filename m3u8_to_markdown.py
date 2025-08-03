#!/usr/bin/env python
# coding: utf-8

import os
import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} m3u8_file")
    sys.exit
    
else:
    file = sys.argv[1]
    m3u8_parser = "https://mtjiexi.cc:966/?url="
    outfile = os.path.splitext(os.path.basename(file))[0] + '.md'
    out = open(outfile, 'w')
    m3u8s = {}
    index = 0
    with open(file, 'r') as f:
        next(f)
        for l in f:
            if l.strip() != "":
                l = l.strip()
                if  index % 2 == 0:
                    if len(l.replace('#EXTINF:-1 ,', '').split()) > 1:
                        name, episode = tuple(l.replace('#EXTINF:-1 ,', '').split())
                    else:
                        name = l.replace('#EXTINF:-1 ,', '')
                else:
                    m3u8 = l
                    if name not in m3u8s:
                        m3u8s.setdefault(name, [m3u8])
                    else:
                        m3u8s[name].append(m3u8)
                index += 1

    for name in m3u8s:
        print("## "+name, file=out)
        strings = ""
        for i, url in enumerate(m3u8s[name]):
            if len(m3u8s[name]) == 1:
                 print(f"[播放]({m3u8_parser}{m3u8s[name][0]})", file=out)
            else:
                i+1
                strings += "[第{:02}集]".format(i+1) + f"({m3u8_parser}{url})    "
        print(strings, file=out)
    out.close()
