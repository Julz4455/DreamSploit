# DreamSploit
## DreamSec Exploit Console

[![Run on Repl.it](https://repl.it/badge/github/Julz4455/DreamSploit)](https://repl.it/github/Julz4455/DreamSploit)
[![HitCount](http://hits.dwyl.io/julz4455/dreamsploit.svg)](http://hits.dwyl.io/julz4455/dreamsploit)
![Passing Build](https://camo.githubusercontent.com/cfcaf3a99103d61f387761e5fc445d9ba0203b01/68747470733a2f2f7472617669732d63692e6f72672f6477796c2f657374612e7376673f6272616e63683d6d6173746572)
![Contributes Welcome](https://camo.githubusercontent.com/926d8ca67df15de5bd1abac234c0603d94f66c00/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f6e747269627574696f6e732d77656c636f6d652d627269676874677265656e2e7376673f7374796c653d666c6174)

#### Alpha v1.0.0
Love metasploit but want to use python more than ruby? Well, you're in luck!
DreamSploit is:
- Metasploit Inspired
- Pluggable
- Customizable
- and Easy To Use!

With support for python2 and python3, you'll only need to install termcolor and get started!
Using DreamSploit is easy but there is also support for custom modules!
Custom modules are easy to make and require only minimal knowledge for the simplest of python modules.
Plus, with a modules.json file, you can turn on and turn off modules at your own discretion.

DreamSploit is easy, custom, and as always, not for educational purposes only.
So make the switch to DreamSploit. Make the switch to the Dream Team.

### Module Creation

1. First create a python file with a name of your choosing.
2. Next create an entry in modules.json (or modules3.json if using Python 3) based on modules.template.json or the example below:
```json
{
  "name": "name of module",
  "path": "/path/to/module",
  "color": "termcolor.colored color"
}
```
  - There is no default color.  Color is mandatory
  - The name is the name that will be called in the command prompt
    - Example: `{"name": "net/scan/port" ...}` transforms to `use net/scan/port` in the console
3. Run the module in the command prompt with the prefix: "use"
4. Profit!
# DreamSploit
## By DreamSec
#### Stable v1.0.0 Coming August 2020
