import os

#color setting
C_END = "\033[0m"
C_YELLOW = "\033[33m"
C_BOLD    = "\033[1m"

#git add
os.system("git add *")
#commit
print(C_BOLD + C_YELLOW + "[+]" + C_END + "committing......")
commit_sh = "git commit -m 'commit'"
os.system(commit_sh)

#push
print(C_BOLD + C_YELLOW + "[+]" + C_END + "pushing......")
os.system("git push")
print(C_BOLD + C_YELLOW + "[+]" + C_END + "done")