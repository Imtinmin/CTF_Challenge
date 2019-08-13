# C 语言作业

这道题的思路源自我之前玩过的一个 Wargame：Smash the Stack IO Level 2。

逆向这个二进制，发现它就是再平常不过的计算器程序了，而且考虑了除以 0 的情况。

仔细观察，在程序初始化的时候（main 函数执行之前），程序注册了几个 signal 的处理函数。这个实际上是用 gcc 的 `__attribute__((constructor))` 实现的。

SIGILL、SIGABRT、SIGFPE、SIGSEGV 几个信号被注册到了 `__err` 函数上面，也就是说发生这几种异常的时候 `__err` 函数会被执行。`__err` 函数会让你输入一个字符串，不能包含 `sh`，然后用 `execlp` 来执行这个字符串代表的程序。值得一提的是，`execlp` 限制了我们只能不带参数地执行程序。

根据 signal 的 man page，SIGILL、SIGABRT、SIGSEGV 在本程序中看起来应该不会发生，我们关注一下 SIGFPE：

> According to POSIX, the behavior of a process is undefined after it ignores a  SIGFPE,  SIGILL,
> or  SIGSEGV signal that was not generated by kill(2) or raise(3).  Integer division by zero has
> undefined result.  On some architectures it will generate a SIGFPE signal.  (Also dividing  the
> most  negative  integer by -1 may generate SIGFPE.)  Ignoring this signal might lead to an end‐
> less loop.

惊讶！不仅除以 0 可能会触发 SIGFPE，最小的 INT 除以 -1 也可能会触发！也就是说，写一个整数计算器，只考虑除以 0 的异常是不够的，最小的 INT 除以 -1 也可能会让程序崩掉。

所以第一步输入 `-2147483648/-1` 即可。

然后，我们需要找到一个程序，不带参数地运行可以帮我们拿到 shell，我能想到的是 vim，当然也可能有其他解法。

_注：我本想模拟一个新安装的 Ubuntu 环境，但是 Ubuntu 的 docker 镜像里面什么都没有，`ed`、`vi` 等命令也应该安装一下的，我对此表示抱歉。（有人提到 python，emmmm）_

第二步输入 `vim` ，然后进入了一个没有 tty 的 vim，很难受，不过也可以执行命令。我们在 vim 内输入 `!cat flag` 即可读取 flag。

然而 flag 告诉我们这个是假的，真的 flag 在一个叫 `-` 的文件里，我们执行 `!cat -` 就可以了。然后什么都没看到！

实际上，`cat -` 中的 `-` 表示标准输入，cat 会试图从你的标准输入中读取，并不能看到 `-` 文件的内容。绕过的办法有多种，最简单的就是 `cat ./-`。

至于 5 秒的限时嘛……复制粘贴都是来得及的，反正进入 vim 之后就没有了。

我们也可以把上面的过程写成一个 shell 脚本：

```bash
#!/bin/bash

echo -e "-2147483648/-1\nvim\n:!ls\n:!cat flag\n:!cat ./-" | nc 202.38.95.46 12008 | grep flag
```