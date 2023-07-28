import os
import re

import natsort

dirlist=["AudioClip", "Sprite", "Texture2D", "TextAsset/Raw"]
for i in dirlist:
    cnt=0
    name_list = {}
    files=natsort.natsorted(os.listdir(i))
    for file in files:
        try: 
            found=re.findall("(.*)#([0-9]+).*$", file)[0]

            if found[0] not in name_list:
                name_list[found[0]] = 1
                num = 1
            else:
                name_list[found[0]] = name_list[found[0]]+1
                num = name_list[found[0]]
            # print(name_list)
            # print(found)
            os.rename(f"{i}/{file}", f"{i}/{file}".replace(f"#{found[1]}", f"#{num}"))
            print(file)
            cnt+=1

        except Exception as e:
            pass

    print(f"Edit {cnt} files in {i} folder\n")
