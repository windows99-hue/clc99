#coding:utf-8
import check as clc99
clc99.initsystem()
clc99.print_status('status',full=True)
clc99.print_good('ok!',full=True)
clc99.print_error('error!',full=True)
clc99.print_warning('warning!',full=True)
clc99.print_finish('finish',full=True)
clc99.print_os('os ok!',full=True)
clc99.print_notrun('This is a comment',full=True)
clc99.print_e('error!',full=True)
clc99.print_fileok('file ok!',full=True)
clc99.print_filerror('file error!',full=True)
clc99.print_time()
clc99.print_music('play 123.mp3',full=True)
clc99.print_video('play 1234.mp4',full=True)
clc99.print_ok('OK!',full=True)
clc99.print_over('system over;)',full=True)
clc99.print_admin('Successfully obtained administrator privileges!',full=True)
#clc99.input_str('input:',full=True)
print("'input_str'Parameters can return the user's input, which is not demonstrated here")
clc99.print_dirok('dirok',full=True)
clc99.print_direrror('direrror',full=True)
clc99.print_comok('The equipment is normal！',full=True)
clc99.print_comerror('equipment error！',full=True)
clc99.print_uquestion('Do you know Python？',full=True)
clc99.print_cquestion('There is a problem with the procedure！',full=True)
def zidingyicolor(str):
    user_c = clc99.user_color('[b]','YELLOW',full=True)
    print(user_c+str)
zidingyicolor('Custom symbols')