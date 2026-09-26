#coding:utf-8
import clc99

print(clc99.__version__)

print("1. 默认分隔符（空格）:")
clc99.print_status('项目', '进度', '50%')

print("\n2. 使用箭头分隔符:")
clc99.print_good('步骤1', '步骤2', '完成', sep=' → ')

print("\n3. 使用竖线分隔符:")
clc99.print_error('模块A', '模块B', '失败', sep=' | ')

print("\n4. 使用逗号分隔符:")
clc99.print_warning('警告1', '警告2', '警告3', sep=', ')

print("\n5. 使用连字符分隔符:")
clc99.print_ok('检查1', '检查2', '检查3', sep=' - ')

print("\n6. 无分隔符:")
clc99.print_finish('任务', '完成', sep='')

print("\n7. 使用换行符分隔:")
clc99.print_notrun('第一行信息', '第二行信息', '第三行信息', sep='\n    ')

print("\n8. 使用表情符号分隔:")
clc99.print_music('歌曲1', '歌曲2', '歌曲3', sep=' 🎵 ')

print("\n9. 文件路径样式分隔:")
clc99.print_fileok('文件夹', '子文件夹', '文件.txt', sep='/')

print("\n10. 多参数复杂分隔:")
clc99.print_admin('用户', 'admin', '执行了操作', '重启服务', sep=' → [动作] → ')

print("\n=== 测试 full 参数 ===")
clc99.print_status('全色模式', full=True)
clc99.print_good('全色成功', full=True)

print("\n=== 测试 end 参数 ===")
clc99.print_ok('不换行', end='')
clc99.print_ok('接着上一行')

print("\n=== 组合测试 ===")
clc99.print_good('多个', '参数', '测试', sep=' | ', end=' [结束]\\n', full=True)

print("\n=== 测试完成 ===")
clc99.print_finish('所有功能测试完成！')
