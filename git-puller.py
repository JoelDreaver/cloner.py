import os
import git

import config

for dir in next(os.walk(config.PROJPATH))[1]:
    g = git.cmd.Git(os.path.join(config.PROJPATH, dir))
    message = g.pull()
    print(dir, ": ", message)
