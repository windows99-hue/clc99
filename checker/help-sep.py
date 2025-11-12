#coding:utf-8
import clc99
clc99.initsystem()

print("1. Default separator (space):")
clc99.print_status('Project', 'Progress', '50%')

print("\n2. Using arrow separator:")
clc99.print_good('Step1', 'Step2', 'Completed', sep=' → ')

print("\n3. Using vertical bar separator:")
clc99.print_error('ModuleA', 'ModuleB', 'Failed', sep=' | ')

print("\n4. Using comma separator:")
clc99.print_warning('Warning1', 'Warning2', 'Warning3', sep=', ')

print("\n5. Using hyphen separator:")
clc99.print_ok('Check1', 'Check2', 'Check3', sep=' - ')

print("\n6. No separator:")
clc99.print_finish('Task', 'Completed', sep='')

print("\n7. Using newline separator:")
clc99.print_notrun('First line info', 'Second line info', 'Third line info', sep='\n    ')

print("\n8. Using emoji separator:")
clc99.print_music('Song1', 'Song2', 'Song3', sep=' 🎵 ')

print("\n9. Using file path style separator:")
clc99.print_fileok('Folder', 'Subfolder', 'File.txt', sep='/')

print("\n10. Multiple parameters with complex separator:")
clc99.print_admin('User', 'admin', 'Performed action', 'Restart service', sep=' → [Action] → ')

print("\n=== Testing full parameter ===")
clc99.print_status('Full color mode', full=True)
clc99.print_good('Full color success', full=True)

print("\n=== Testing end parameter ===")
clc99.print_ok('No newline', end='')
clc99.print_ok('Continue from previous line')

print("\n=== Combination testing ===")
clc99.print_good('Multiple', 'Parameters', 'Test', sep=' | ', end=' [End]\\n', full=True)

print("\n=== Testing completed ===")
clc99.print_finish('All function tests completed!')