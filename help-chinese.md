# clc99 帮助文档

> 完整教程请看 **[wiki](https://github.com/windows99-hue/clc99/wiki)**，本文档是放在仓库里的快速参考。

## 安装

clc99 需要 **Python 3.7 或更高版本**（依赖 `colorama>=0.4.6`）。

~~~bash
pip install clc99
~~~

## 导入

~~~python
import clc99          # 保留命名空间，用 clc99.print_status(...) 调用
from clc99 import *   # 直接调用 print_status(...)
~~~

clc99 在被导入时会自动执行 `colorama` 的 `just_fix_windows_console()` 来修复 Windows 终端，所以不需要手动初始化（`initsystem()` 已在 2.4.0 中移除）。

## 默认输出函数

~~~python
clc99.print_status('[*] 状态')
clc99.print_good('[+] 成功')
clc99.print_error('[-] 错误')
clc99.print_warning('[!] 警告')
clc99.print_finish('[FINISH] 完成')
clc99.print_os('[$] 系统')
clc99.print_notrun('[#] 注释')
clc99.print_e('[ERROR] 错误')
clc99.print_fileok('[.] 文件正常')
clc99.print_filerror('[.] 文件错误')
clc99.print_music('[playmusic] 播放音乐')
clc99.print_video('[playvideo] 播放视频')
clc99.print_ok('[OK] 成功')
clc99.print_over('[OVER] 结束')
clc99.print_admin('[Admin] 管理员')
clc99.print_dirok('[/] 目录正常')
clc99.print_direrror('[/] 目录错误')
clc99.print_comok('[C] 设备正常')
clc99.print_comerror('[C] 设备错误')
clc99.print_uquestion('[?] 用户提问')
clc99.print_cquestion('[?] 程序问题')
~~~

它们的参数完全一样：

参数 | 类型 | 默认值 | 说明
-- | -- | -- | --
args | 任意 | 无 | 要输出的内容，和 `print` 一样可以传多个，不限类型
full | bool | False | 颜色是否填满整行
end | str | "\n" | 同 `print(end=)`
file | file | None | 同 `print(file=)`
sep | str | " " | 同 `print(sep=)`

## 特殊输出函数

### print_time

在输出里插入当前时间：

~~~python
print_time()                               # [TIME] 2026-09-27 21:00:00
print_time("TIME: ", position="front")     # [TIME] TIME: 2026-09-27 21:00:00
print_time(" <- now", position="before")   # [TIME] 2026-09-27 21:00:00 <- now
print_time("-", position="middle")         # [TIME] -2026-09-27 21:00:00-
~~~

参数：`text`、`timeformat`（格式同 `time` 模块）、`position`（`front` / `before` / `middle`，默认 `front`）、`full`、`end`、`file`、`sep`。

> **2.4.0 的变化**：`text` 以前叫 `str`，`position` 以前叫 `title`，这两个旧名字仍然可用；`position` 传了不认识的值现在会抛出 `ValueError`（以前是静默不输出）；`end` 以前被忽略，现在生效（`sep` 对 `print_time` 没有实际作用，因为它只输出一段内容）。

### input_str

`input` 的封装函数：

~~~python
name = input_str("请输入你的名字：")
~~~

### make_printer（2.4.0 新增）

做出属于自己的符号输出函数：

~~~python
upload = clc99.make_printer("[UPLOAD]", color="cyan")
upload("foo.png")             # [UPLOAD] foo.png
upload("bar.png", full=True)  # 颜色填满整行
~~~

返回的函数和 `print_status` 用法完全一样，`full` / `end` / `file` / `sep` 都支持。

### user_color

创建自定义符号：

~~~python
user_c = clc99.user_color('[b]', 'YELLOW')
print(user_c + '自定义符号')
~~~

`make_printer` 和 `user_color` 用的是同一套颜色写法：八个基础色 `BLACK` `RED` `GREEN` `YELLOW` `BLUE` `MAGENTA` `CYAN` `WHITE`，`LIGHTRED` 这类亮色，`RESET`，也可以直接传 colorama 的 `Fore.RED`。大小写和 `_`、`-` 都不敏感；颜色名不认识时会抛出 `ValueError`。

## loading99 装饰器

~~~python
@loading99(text="正在处理...", success_text="OK")
def work():
    print("这一行不会被显示")
    return 1

work()
~~~

参数 | 类型 | 默认值 | 说明
-- | -- | -- | --
text | str | "" | 加载时显示的文本，为空则自动用函数名 + "is running"
success_text | str | "OK" | 函数成功执行后显示的文本
except_text | str | "EXCEPTION OCCURRED!" | 函数发生异常时显示的文本
suppress_output | bool | True | 是否屏蔽函数内部的 print 输出
output_success_text | bool | True | 是否显示成功文本

出错时可以用 `err99()` 在任何位置中断函数并输出提示：

~~~python
@loading99()
def check(age):
    if age < 18:
        err99("年龄不足")                    # 显示 FAILED: 年龄不足
    if age > 100:
        err99("INVALID_AGE", "年龄不合理")   # 显示 INVALID_AGE: 年龄不合理
~~~

`err99(error_text="FAILED", text="")` 抛出 `FAILEDException`，它会被 `loading99` 捕获并显示，不会让程序崩掉。

## 2.4.0 的变化

* 新增 `make_printer()`。
* `print_time`：参数改名 `str`→`text`、`title`→`position`（旧名保留），位置传错改为抛 `ValueError`，`end` 生效。
* `user_color`：颜色支持大小写不敏感、亮色、`RESET` 和 `Fore.*` 转义码。
* `loading99`：`except_text` 默认值改为 `"EXCEPTION OCCURRED!"`，并且在 `suppress_output` 的两种模式下都生效。
* 移除 `initsystem()`，改为导入时自动修复终端。
* 最低支持 Python 3.7（依赖 `colorama>=0.4.6`）。
