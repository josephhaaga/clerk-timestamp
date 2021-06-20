# clerk-timestamp

A [clerk](https://github.com/josephhaaga/clerk) extension to append timestamps to your journal


## Setup

Install `clerk-timestamp` in the `venv` that `clerk` is installed in

```
$ pipx runpip josephhaaga-clerk install josephhaaga-clerk-timestamp
```

Then, in your `clerk.conf` config file:

```
...

[hooks]
JOURNAL_OPENED =
    timestamp
```

For more information, see `clerk` [hooks documentation](https://github.com/josephhaaga/clerk#hooks)
