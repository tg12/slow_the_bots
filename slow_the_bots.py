import re
import os
import errno

size_kb = 51200  # 10 MB
# commonly accessed files, php, js etc....
#regex = r"\b[^\s<>]*?.php\b"
regex = r"\b[^\s<>]*?.(php|js)\b"
base_dir = "/var/www/html/"

with open('/var/log/apache2/access.log', 'r') as access_log:
    access_txt = access_log.read()

matches = re.finditer(regex, access_txt)
uniq_match = []

for matchNum, match in enumerate(matches, start=1):
    if str(match.group()) not in uniq_match:
        uniq_match.append(str(match.group()))

for a in uniq_match:
    try:
        output_file = base_dir + str(a)
        if os.path.exists(output_file):
            os.remove(output_file)
        if not os.path.exists(os.path.dirname(output_file)):
            try:

                os.makedirs(os.path.dirname(output_file))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        print("[+]debug, creating... " + str(output_file))
        with open(output_file, 'wb') as fout:
            # replace with size_kb if not reasonably large
            fout.write(os.urandom(size_kb))
            # fout.write("rm -rf /\r\n") # if an attacker is silly enough to
            # run script's blindly, Then inject your own code here.
    except BaseException:
        pass
