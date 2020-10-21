'''THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE AND
NON-INFRINGEMENT. IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR ANYONE
DISTRIBUTING THE SOFTWARE BE LIABLE FOR ANY DAMAGES OR OTHER LIABILITY,
WHETHER IN CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

# Bitcoin Cash (BCH)   qpz32c4lg7x7lnk9jg6qg7s4uavdce89myax5v5nuk
# Ether (ETH) -        0x843d3DEC2A4705BD4f45F674F641cE2D0022c9FB
# Litecoin (LTC) -     Lfk5y4F7KZa9oRxpazETwjQnHszEPvqPvu
# Bitcoin (BTC) -      34L8qWiQyKr8k4TnHDacfjbaSqQASbBtTd

# contact :- github@jamessawyer.co.uk



import re
import os
import errno

size_kb = 512000000  # 10 MB
# commonly accessed files, php, js etc....
#regex = r"\b[^\s<>]*?.php\b"
regex = r"\b[^\s<>]*?.(php|js|html|css|pdf|cgi|txt|xml)\b"
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
