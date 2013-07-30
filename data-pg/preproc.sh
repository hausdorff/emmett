cat *.log | grep -e "web_exec_py[23]\(-1\)\?.py" | grep -oP "user_script=.*? " > all.txt
