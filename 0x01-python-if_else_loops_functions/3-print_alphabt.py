#!/usr/bin/python3

print("{}".format(''.join([chr(alpha) for alpha in range(97, 123)])
      .replace("q", "").replace("e", "")), end="")
