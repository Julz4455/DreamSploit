import sys
import time
import os
from termcolor import colored

class LoadSequence:

  def progressbar(it, prefix="", size=60, file=sys.stdout):
      count = len(it)

      def show(j):
          x = int(size * j / count)
          file.write(
              "%s[%s%s] %s/%s\r" % (colored(prefix, "red"), colored("#", "cyan") * x, "." * (size - x), colored(str(j), "green"), colored(count, "yellow")))
          file.flush()

      show(0)
      for i, item in enumerate(it):
          yield item
          show(i + 1)
      file.write("\n")
      file.flush()
  def loadAssets(assets, self):
    for i in self.progressbar(range(100), "Fetching Assets: ", 30):
      time.sleep(0.02)
    os.system('clear')
    for i in self.progressbar(range(100), "Compliling Assets: ", 30):
        time.sleep(0.09)
    os.system('clear')
    for i in self.progressbar(range(100), "Configuring Settings: ", 20):
        time.sleep(0.04)
    os.system('clear')
    for i in self.progressbar(range(100), "Loading: ", 20):
        time.sleep(0.01)
    print("\n\nOperations Complete. Starting Console...")
    time.sleep(3)
    os.system('clear')