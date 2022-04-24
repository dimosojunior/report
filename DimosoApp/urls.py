
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('base/', views.base, name="base"),

    path('user_login/', views.user_login, name="user_login"),
    #path('user_register', views.user_register.as_view(), name="user_register"),
    path('user_logout/', views.user_logout, name="user_logout"),
    path('registration/', views.registration, name="registration"),
    path('ReportIssues/', views.ReportIssues, name="ReportIssues"),

    
    path('sending_email_to_form_one/', views.sending_email_to_form_one, name="sending_email_to_form_one"),
    path('all_form_one_reports/', views.all_form_one_reports, name="all_form_one_reports"),
    path('search_autoco_form_one_report', views.search_autoco_form_one_report, name="search_autoco_form_one_report"),
    path('search_autoco_form_one_student', views.search_autoco_form_one_student, name="search_autoco_form_one_student"),

    path('update_form_one_report/<str:pk>', views.update_form_one_report.as_view(), name="update_form_one_report"),
    path('delete_form_one_report/<int:pk>/', views.delete_form_one_report, name="delete_form_one_report"),
    path('view_form_one_report/<int:pk>/', views.view_form_one_report.as_view(), name="view_form_one_report"),
    path('all_form_one_students/', views.all_form_one_students, name="all_form_one_students"),
    path('add_form1_students/', views.add_form1_students.as_view(), name="add_form1_students"),

    path('update_form_one_student/<str:pk>', views.update_form_one_student.as_view(), name="update_form_one_student"),
    path('delete_form_one_student/<int:pk>/', views.delete_form_one_student, name="delete_form_one_student"),

    #hizi urls kwa ajili ya classes zinazopatikana form 1
    path('form1_A_students/', views.form1_A_students, name="form1_A_students"),

    path('search_form1_student/', views.search_form1_student, name="search_form1_student"),
    path('search_autoco_form_one_student2', views.search_autoco_form_one_student2, name="search_autoco_form_one_student2"),
    path('form1_B_students/', views.form1_B_students, name="form1_B_students"),
    path('form1_C_students/', views.form1_C_students, name="form1_C_students"),
    path('form1_D_students/', views.form1_D_students, name="form1_D_students"),
    path('form1_E_students/', views.form1_E_students, name="form1_E_students"),



    #FORM TWO URLS
    path('sending_email_to_form_two/', views.sending_email_to_form_two, name="sending_email_to_form_two"),
    path('all_form_two_reports/', views.all_form_two_reports, name="all_form_two_reports"),
    path('search_autoco_form_two_report', views.search_autoco_form_two_report, name="search_autoco_form_two_report"),
    path('search_autoco_form_two_student', views.search_autoco_form_two_student, name="search_autoco_form_two_student"),

    path('update_form_two_report/<str:pk>', views.update_form_two_report.as_view(), name="update_form_two_report"),
    path('delete_form_two_report/<int:pk>/', views.delete_form_two_report, name="delete_form_two_report"),
    path('view_form_two_report/<int:pk>/', views.view_form_two_report.as_view(), name="view_form_two_report"),
    path('all_form_two_students/', views.all_form_two_students, name="all_form_two_students"),
    path('add_form2_students/', views.add_form2_students.as_view(), name="add_form2_students"),

    path('update_form_two_student/<str:pk>', views.update_form_two_student.as_view(), name="update_form_two_student"),
    path('delete_form_two_student/<int:pk>/', views.delete_form_two_student, name="delete_form_two_student"),

    #hizi urls kwa ajili ya classes zinazopatikana form 2
    path('form2_A_students/', views.form2_A_students, name="form2_A_students"),

    path('search_form2_student/', views.search_form2_student, name="search_form2_student"),
    path('search_autoco_form_two_student2', views.search_autoco_form_two_student2, name="search_autoco_form_two_student2"),
    path('form2_B_students/', views.form2_B_students, name="form2_B_students"),
    path('form2_C_students/', views.form2_C_students, name="form2_C_students"),
    path('form2_D_students/', views.form2_D_students, name="form2_D_students"),
    path('form2_E_students/', views.form2_E_students, name="form2_E_students"),





    #FORM THREE URLS
    path('sending_email_to_form_three/', views.sending_email_to_form_three, name="sending_email_to_form_three"),
    path('all_form_three_reports/', views.all_form_three_reports, name="all_form_three_reports"),
    path('search_autoco_form_three_report', views.search_autoco_form_three_report, name="search_autoco_form_three_report"),
    path('search_autoco_form_three_student', views.search_autoco_form_three_student, name="search_autoco_form_three_student"),

    path('update_form_three_report/<str:pk>', views.update_form_three_report.as_view(), name="update_form_three_report"),
    path('delete_form_three_report/<int:pk>/', views.delete_form_three_report, name="delete_form_three_report"),
    path('view_form_three_report/<int:pk>/', views.view_form_three_report.as_view(), name="view_form_three_report"),
    path('all_form_three_students/', views.all_form_three_students, name="all_form_three_students"),
    path('add_form3_students/', views.add_form3_students.as_view(), name="add_form3_students"),

    path('update_form_three_student/<str:pk>', views.update_form_three_student.as_view(), name="update_form_three_student"),
    path('delete_form_three_student/<int:pk>/', views.delete_form_three_student, name="delete_form_three_student"),

    #hizi urls kwa ajili ya classes zinazopatikana form 3
    path('form3_A_students/', views.form3_A_students, name="form3_A_students"),

    path('search_form3_student/', views.search_form3_student, name="search_form3_student"),
    path('search_autoco_form_three_student2', views.search_autoco_form_three_student2, name="search_autoco_form_three_student2"),
    path('form3_B_students/', views.form3_B_students, name="form3_B_students"),
    path('form3_C_students/', views.form3_C_students, name="form3_C_students"),
    path('form3_D_students/', views.form3_D_students, name="form3_D_students"),
    path('form3_E_students/', views.form3_E_students, name="form3_E_students"),






    #FORM FOUR URLS
    path('sending_email_to_form_four/', views.sending_email_to_form_four, name="sending_email_to_form_four"),
    path('all_form_four_reports/', views.all_form_four_reports, name="all_form_four_reports"),
    path('search_autoco_form_four_report', views.search_autoco_form_four_report, name="search_autoco_form_four_report"),
    path('search_autoco_form_four_student', views.search_autoco_form_four_student, name="search_autoco_form_four_student"),

    path('update_form_four_report/<str:pk>', views.update_form_four_report.as_view(), name="update_form_four_report"),
    path('delete_form_four_report/<int:pk>/', views.delete_form_four_report, name="delete_form_four_report"),
    path('view_form_four_report/<int:pk>/', views.view_form_four_report.as_view(), name="view_form_four_report"),
    path('all_form_four_students/', views.all_form_four_students, name="all_form_four_students"),
    path('add_form4_students/', views.add_form4_students.as_view(), name="add_form4_students"),

    path('update_form_four_student/<str:pk>', views.update_form_four_student.as_view(), name="update_form_four_student"),
    path('delete_form_four_student/<int:pk>/', views.delete_form_four_student, name="delete_form_four_student"),

    #hizi urls kwa ajili ya classes zinazopatikana form 4
    path('form4_A_students/', views.form4_A_students, name="form4_A_students"),

    path('search_form4_student/', views.search_form4_student, name="search_form4_student"),
    path('search_autoco_form_four_student2', views.search_autoco_form_four_student2, name="search_autoco_form_four_student2"),
    path('form4_B_students/', views.form4_B_students, name="form4_B_students"),
    path('form4_C_students/', views.form4_C_students, name="form4_C_students"),
    path('form4_D_students/', views.form4_D_students, name="form4_D_students"),
    path('form4_E_students/', views.form4_E_students, name="form4_E_students"),





    #PCM FORM FIVE URLS

    path('sending_email_to_form_five_pcm/', views.sending_email_to_form_five_pcm, name="sending_email_to_form_five_pcm"),
    path('all_form_five_reports_pcm/', views.all_form_five_reports_pcm, name="all_form_five_reports_pcm"),
    path('search_autoco_form_five_report_pcm', views.search_autoco_form_five_report_pcm, name="search_autoco_form_five_report_pcm"),
    path('search_autoco_form_five_student_pcm', views.search_autoco_form_five_student_pcm, name="search_autoco_form_five_student_pcm"),

    path('update_form_five_report_pcm/<str:pk>', views.update_form_five_report_pcm.as_view(), name="update_form_five_report_pcm"),
    path('delete_form_five_report_pcm/<int:pk>/', views.delete_form_five_report_pcm, name="delete_form_five_report_pcm"),
    path('view_form_five_report_pcm/<int:pk>/', views.view_form_five_report_pcm.as_view(), name="view_form_five_report_pcm"),
    path('all_form_five_students_pcm/', views.all_form_five_students_pcm, name="all_form_five_students_pcm"),
    path('add_form5_students_pcm/', views.add_form5_students_pcm.as_view(), name="add_form5_students_pcm"),

    path('update_form_five_student_pcm/<str:pk>', views.update_form_five_student_pcm.as_view(), name="update_form_five_student_pcm"),
    path('delete_form_five_student_pcm/<int:pk>/', views.delete_form_five_student_pcm, name="delete_form_five_student_pcm"),

    

    path('search_form5_student_pcm/', views.search_form5_student_pcm, name="search_form5_student_pcm"),
    path('search_autoco_form_five_student2_pcm', views.search_autoco_form_five_student2_pcm, name="search_autoco_form_five_student2_pcm"),
    

    #PCB FORM 5 URLS
    path('sending_email_to_form_five_pcb/', views.sending_email_to_form_five_pcb, name="sending_email_to_form_five_pcb"),
    path('all_form_five_reports_pcb/', views.all_form_five_reports_pcb, name="all_form_five_reports_pcb"),
    path('search_autoco_form_five_report_pcb', views.search_autoco_form_five_report_pcb, name="search_autoco_form_five_report_pcb"),
    path('search_autoco_form_five_student_pcb', views.search_autoco_form_five_student_pcb, name="search_autoco_form_five_student_pcb"),

    path('update_form_five_report_pcb/<str:pk>', views.update_form_five_report_pcb.as_view(), name="update_form_five_report_pcb"),
    path('delete_form_five_report_pcb/<int:pk>/', views.delete_form_five_report_pcb, name="delete_form_five_report_pcb"),
    path('view_form_five_report_pcb/<int:pk>/', views.view_form_five_report_pcb.as_view(), name="view_form_five_report_pcb"),
    path('all_form_five_students_pcb/', views.all_form_five_students_pcb, name="all_form_five_students_pcb"),
    path('add_form5_students_pcb/', views.add_form5_students_pcb.as_view(), name="add_form5_students_pcb"),

    path('update_form_five_student_pcb/<str:pk>', views.update_form_five_student_pcb.as_view(), name="update_form_five_student_pcb"),
    path('delete_form_five_student_pcb/<int:pk>/', views.delete_form_five_student_pcb, name="delete_form_five_student_pcb"),

    

    path('search_form5_student_pcb/', views.search_form5_student_pcb, name="search_form5_student_pcb"),
    path('search_autoco_form_five_student2_pcb', views.search_autoco_form_five_student2_pcb, name="search_autoco_form_five_student2_pcb"),


    #PGM FORM 5 URLS
    path('sending_email_to_form_five_pgm/', views.sending_email_to_form_five_pgm, name="sending_email_to_form_five_pgm"),
    path('all_form_five_reports_pgm/', views.all_form_five_reports_pgm, name="all_form_five_reports_pgm"),
    path('search_autoco_form_five_report_pgm', views.search_autoco_form_five_report_pgm, name="search_autoco_form_five_report_pgm"),
    path('search_autoco_form_five_student_pgm', views.search_autoco_form_five_student_pgm, name="search_autoco_form_five_student_pgm"),

    path('update_form_five_report_pgm/<str:pk>', views.update_form_five_report_pgm.as_view(), name="update_form_five_report_pgm"),
    path('delete_form_five_report_pgm/<int:pk>/', views.delete_form_five_report_pgm, name="delete_form_five_report_pgm"),
    path('view_form_five_report_pgm/<int:pk>/', views.view_form_five_report_pgm.as_view(), name="view_form_five_report_pgm"),
    path('all_form_five_students_pgm/', views.all_form_five_students_pgm, name="all_form_five_students_pgm"),
    path('add_form5_students_pgm/', views.add_form5_students_pgm.as_view(), name="add_form5_students_pgm"),

    path('update_form_five_student_pgm/<str:pk>', views.update_form_five_student_pgm.as_view(), name="update_form_five_student_pgm"),
    path('delete_form_five_student_pgm/<int:pk>/', views.delete_form_five_student_pgm, name="delete_form_five_student_pgm"),

    

    path('search_form5_student_pgm/', views.search_form5_student_pgm, name="search_form5_student_pgm"),
    path('search_autoco_form_five_student2_pgm', views.search_autoco_form_five_student2_pgm, name="search_autoco_form_five_student2_pgm"),




    #HGL FORM 5 URLS
    path('sending_email_to_form_five_hgl/', views.sending_email_to_form_five_hgl, name="sending_email_to_form_five_hgl"),
    path('all_form_five_reports_hgl/', views.all_form_five_reports_hgl, name="all_form_five_reports_hgl"),
    path('search_autoco_form_five_report_hgl', views.search_autoco_form_five_report_hgl, name="search_autoco_form_five_report_hgl"),
    path('search_autoco_form_five_student_hgl', views.search_autoco_form_five_student_hgl, name="search_autoco_form_five_student_hgl"),

    path('update_form_five_report_hgl/<str:pk>', views.update_form_five_report_hgl.as_view(), name="update_form_five_report_hgl"),
    path('delete_form_five_report_hgl/<int:pk>/', views.delete_form_five_report_hgl, name="delete_form_five_report_hgl"),
    path('view_form_five_report_hgl/<int:pk>/', views.view_form_five_report_hgl.as_view(), name="view_form_five_report_hgl"),
    path('all_form_five_students_hgl/', views.all_form_five_students_hgl, name="all_form_five_students_hgl"),
    path('add_form5_students_hgl/', views.add_form5_students_hgl.as_view(), name="add_form5_students_hgl"),

    path('update_form_five_student_hgl/<str:pk>', views.update_form_five_student_hgl.as_view(), name="update_form_five_student_hgl"),
    path('delete_form_five_student_hgl/<int:pk>/', views.delete_form_five_student_hgl, name="delete_form_five_student_hgl"),

    

    path('search_form5_student_hgl/', views.search_form5_student_hgl, name="search_form5_student_hgl"),
    path('search_autoco_form_five_student2_hgl', views.search_autoco_form_five_student2_hgl, name="search_autoco_form_five_student2_hgl"),





    #HGK FORM 5 URLS
    path('sending_email_to_form_five_hgk/', views.sending_email_to_form_five_hgk, name="sending_email_to_form_five_hgk"),
    path('all_form_five_reports_hgk/', views.all_form_five_reports_hgk, name="all_form_five_reports_hgk"),
    path('search_autoco_form_five_report_hgk', views.search_autoco_form_five_report_hgk, name="search_autoco_form_five_report_hgk"),
    path('search_autoco_form_five_student_hgk', views.search_autoco_form_five_student_hgk, name="search_autoco_form_five_student_hgk"),

    path('update_form_five_report_hgk/<str:pk>', views.update_form_five_report_hgk.as_view(), name="update_form_five_report_hgk"),
    path('delete_form_five_report_hgk/<int:pk>/', views.delete_form_five_report_hgk, name="delete_form_five_report_hgk"),
    path('view_form_five_report_hgk/<int:pk>/', views.view_form_five_report_hgk.as_view(), name="view_form_five_report_hgk"),
    path('all_form_five_students_hgk/', views.all_form_five_students_hgk, name="all_form_five_students_hgk"),
    path('add_form5_students_hgk/', views.add_form5_students_hgk.as_view(), name="add_form5_students_hgk"),

    path('update_form_five_student_hgk/<str:pk>', views.update_form_five_student_hgk.as_view(), name="update_form_five_student_hgk"),
    path('delete_form_five_student_hgk/<int:pk>/', views.delete_form_five_student_hgk, name="delete_form_five_student_hgk"),

    

    path('search_form5_student_hgk/', views.search_form5_student_hgk, name="search_form5_student_hgk"),
    path('search_autoco_form_five_student2_hgk', views.search_autoco_form_five_student2_hgk, name="search_autoco_form_five_student2_hgk"),


    #CBG FORM 5 URLS
    path('sending_email_to_form_five_cbg/', views.sending_email_to_form_five_cbg, name="sending_email_to_form_five_cbg"),
    path('all_form_five_reports_cbg/', views.all_form_five_reports_cbg, name="all_form_five_reports_cbg"),
    path('search_autoco_form_five_report_cbg', views.search_autoco_form_five_report_cbg, name="search_autoco_form_five_report_cbg"),
    path('search_autoco_form_five_student_cbg', views.search_autoco_form_five_student_cbg, name="search_autoco_form_five_student_cbg"),

    path('update_form_five_report_cbg/<str:pk>', views.update_form_five_report_cbg.as_view(), name="update_form_five_report_cbg"),
    path('delete_form_five_report_cbg/<int:pk>/', views.delete_form_five_report_cbg, name="delete_form_five_report_cbg"),
    path('view_form_five_report_cbg/<int:pk>/', views.view_form_five_report_cbg.as_view(), name="view_form_five_report_cbg"),
    path('all_form_five_students_cbg/', views.all_form_five_students_cbg, name="all_form_five_students_cbg"),
    path('add_form5_students_cbg/', views.add_form5_students_cbg.as_view(), name="add_form5_students_cbg"),

    path('update_form_five_student_cbg/<str:pk>', views.update_form_five_student_cbg.as_view(), name="update_form_five_student_cbg"),
    path('delete_form_five_student_cbg/<int:pk>/', views.delete_form_five_student_cbg, name="delete_form_five_student_cbg"),

    

    path('search_form5_student_cbg/', views.search_form5_student_cbg, name="search_form5_student_cbg"),
    path('search_autoco_form_five_student2_cbg', views.search_autoco_form_five_student2_cbg, name="search_autoco_form_five_student2_cbg"),



    #HKL FORM 5  URLS
    path('sending_email_to_form_five_hkl/', views.sending_email_to_form_five_hkl, name="sending_email_to_form_five_hkl"),
    path('all_form_five_reports_hkl/', views.all_form_five_reports_hkl, name="all_form_five_reports_hkl"),
    path('search_autoco_form_five_report_hkl', views.search_autoco_form_five_report_hkl, name="search_autoco_form_five_report_hkl"),
    path('search_autoco_form_five_student_hkl', views.search_autoco_form_five_student_hkl, name="search_autoco_form_five_student_hkl"),

    path('update_form_five_report_hkl/<str:pk>', views.update_form_five_report_hkl.as_view(), name="update_form_five_report_hkl"),
    path('delete_form_five_report_hkl/<int:pk>/', views.delete_form_five_report_hkl, name="delete_form_five_report_hkl"),
    path('view_form_five_report_hkl/<int:pk>/', views.view_form_five_report_hkl.as_view(), name="view_form_five_report_hkl"),
    path('all_form_five_students_hkl/', views.all_form_five_students_hkl, name="all_form_five_students_hkl"),
    path('add_form5_students_hkl/', views.add_form5_students_hkl.as_view(), name="add_form5_students_hkl"),

    path('update_form_five_student_hkl/<str:pk>', views.update_form_five_student_hkl.as_view(), name="update_form_five_student_hkl"),
    path('delete_form_five_student_hkl/<int:pk>/', views.delete_form_five_student_hkl, name="delete_form_five_student_hkl"),

    

    path('search_form5_student_hkl/', views.search_form5_student_hkl, name="search_form5_student_hkl"),
    path('search_autoco_form_five_student2_hkl', views.search_autoco_form_five_student2_hkl, name="search_autoco_form_five_student2_hkl"),


    #ECA FORM5 URLS
    path('sending_email_to_form_five_eca/', views.sending_email_to_form_five_eca, name="sending_email_to_form_five_eca"),
    path('all_form_five_reports_eca/', views.all_form_five_reports_eca, name="all_form_five_reports_eca"),
    path('search_autoco_form_five_report_eca', views.search_autoco_form_five_report_eca, name="search_autoco_form_five_report_eca"),
    path('search_autoco_form_five_student_eca', views.search_autoco_form_five_student_eca, name="search_autoco_form_five_student_eca"),

    path('update_form_five_report_eca/<str:pk>', views.update_form_five_report_eca.as_view(), name="update_form_five_report_eca"),
    path('delete_form_five_report_eca/<int:pk>/', views.delete_form_five_report_eca, name="delete_form_five_report_eca"),
    path('view_form_five_report_eca/<int:pk>/', views.view_form_five_report_eca.as_view(), name="view_form_five_report_eca"),
    path('all_form_five_students_eca/', views.all_form_five_students_eca, name="all_form_five_students_eca"),
    path('add_form5_students_eca/', views.add_form5_students_eca.as_view(), name="add_form5_students_eca"),

    path('update_form_five_student_eca/<str:pk>', views.update_form_five_student_eca.as_view(), name="update_form_five_student_eca"),
    path('delete_form_five_student_eca/<int:pk>/', views.delete_form_five_student_eca, name="delete_form_five_student_eca"),

    

    path('search_form5_student_eca/', views.search_form5_student_eca, name="search_form5_student_eca"),
    path('search_autoco_form_five_student2_eca', views.search_autoco_form_five_student2_eca, name="search_autoco_form_five_student2_eca"),





    #FORM SIX URLS

    path('sending_email_to_form_six_pcm/', views.sending_email_to_form_six_pcm, name="sending_email_to_form_six_pcm"),
    path('all_form_six_reports_pcm/', views.all_form_six_reports_pcm, name="all_form_six_reports_pcm"),
    path('search_autoco_form_six_report_pcm', views.search_autoco_form_six_report_pcm, name="search_autoco_form_six_report_pcm"),
    path('search_autoco_form_six_student_pcm', views.search_autoco_form_six_student_pcm, name="search_autoco_form_six_student_pcm"),

    path('update_form_six_report_pcm/<str:pk>', views.update_form_six_report_pcm.as_view(), name="update_form_six_report_pcm"),
    path('delete_form_six_report_pcm/<int:pk>/', views.delete_form_six_report_pcm, name="delete_form_six_report_pcm"),
    path('view_form_six_report_pcm/<int:pk>/', views.view_form_six_report_pcm.as_view(), name="view_form_six_report_pcm"),
    path('all_form_six_students_pcm/', views.all_form_six_students_pcm, name="all_form_six_students_pcm"),
    path('add_form6_students_pcm/', views.add_form6_students_pcm.as_view(), name="add_form6_students_pcm"),

    path('update_form_six_student_pcm/<str:pk>', views.update_form_six_student_pcm.as_view(), name="update_form_six_student_pcm"),
    path('delete_form_six_student_pcm/<int:pk>/', views.delete_form_six_student_pcm, name="delete_form_six_student_pcm"),

    

    path('search_form6_student_pcm/', views.search_form6_student_pcm, name="search_form6_student_pcm"),
    path('search_autoco_form_six_student2_pcm', views.search_autoco_form_six_student2_pcm, name="search_autoco_form_six_student2_pcm"),
    

    #PCB FORM 5 URLS
    path('sending_email_to_form_six_pcb/', views.sending_email_to_form_six_pcb, name="sending_email_to_form_six_pcb"),
    path('all_form_six_reports_pcb/', views.all_form_six_reports_pcb, name="all_form_six_reports_pcb"),
    path('search_autoco_form_six_report_pcb', views.search_autoco_form_six_report_pcb, name="search_autoco_form_six_report_pcb"),
    path('search_autoco_form_six_student_pcb', views.search_autoco_form_six_student_pcb, name="search_autoco_form_six_student_pcb"),

    path('update_form_six_report_pcb/<str:pk>', views.update_form_six_report_pcb.as_view(), name="update_form_six_report_pcb"),
    path('delete_form_six_report_pcb/<int:pk>/', views.delete_form_six_report_pcb, name="delete_form_six_report_pcb"),
    path('view_form_six_report_pcb/<int:pk>/', views.view_form_six_report_pcb.as_view(), name="view_form_six_report_pcb"),
    path('all_form_six_students_pcb/', views.all_form_six_students_pcb, name="all_form_six_students_pcb"),
    path('add_form6_students_pcb/', views.add_form6_students_pcb.as_view(), name="add_form6_students_pcb"),

    path('update_form_six_student_pcb/<str:pk>', views.update_form_six_student_pcb.as_view(), name="update_form_six_student_pcb"),
    path('delete_form_six_student_pcb/<int:pk>/', views.delete_form_six_student_pcb, name="delete_form_six_student_pcb"),

    

    path('search_form6_student_pcb/', views.search_form6_student_pcb, name="search_form6_student_pcb"),
    path('search_autoco_form_six_student2_pcb', views.search_autoco_form_six_student2_pcb, name="search_autoco_form_six_student2_pcb"),


    #PGM FORM 5 URLS
    path('sending_email_to_form_six_pgm/', views.sending_email_to_form_six_pgm, name="sending_email_to_form_six_pgm"),
    path('all_form_six_reports_pgm/', views.all_form_six_reports_pgm, name="all_form_six_reports_pgm"),
    path('search_autoco_form_six_report_pgm', views.search_autoco_form_six_report_pgm, name="search_autoco_form_six_report_pgm"),
    path('search_autoco_form_six_student_pgm', views.search_autoco_form_six_student_pgm, name="search_autoco_form_six_student_pgm"),

    path('update_form_six_report_pgm/<str:pk>', views.update_form_six_report_pgm.as_view(), name="update_form_six_report_pgm"),
    path('delete_form_six_report_pgm/<int:pk>/', views.delete_form_six_report_pgm, name="delete_form_six_report_pgm"),
    path('view_form_six_report_pgm/<int:pk>/', views.view_form_six_report_pgm.as_view(), name="view_form_six_report_pgm"),
    path('all_form_six_students_pgm/', views.all_form_six_students_pgm, name="all_form_six_students_pgm"),
    path('add_form6_students_pgm/', views.add_form6_students_pgm.as_view(), name="add_form6_students_pgm"),

    path('update_form_six_student_pgm/<str:pk>', views.update_form_six_student_pgm.as_view(), name="update_form_six_student_pgm"),
    path('delete_form_six_student_pgm/<int:pk>/', views.delete_form_six_student_pgm, name="delete_form_six_student_pgm"),

    

    path('search_form6_student_pgm/', views.search_form6_student_pgm, name="search_form6_student_pgm"),
    path('search_autoco_form_six_student2_pgm', views.search_autoco_form_six_student2_pgm, name="search_autoco_form_six_student2_pgm"),




    #HGL FORM 5 URLS
    path('sending_email_to_form_six_hgl/', views.sending_email_to_form_six_hgl, name="sending_email_to_form_six_hgl"),
    path('all_form_six_reports_hgl/', views.all_form_six_reports_hgl, name="all_form_six_reports_hgl"),
    path('search_autoco_form_six_report_hgl', views.search_autoco_form_six_report_hgl, name="search_autoco_form_six_report_hgl"),
    path('search_autoco_form_six_student_hgl', views.search_autoco_form_six_student_hgl, name="search_autoco_form_six_student_hgl"),

    path('update_form_six_report_hgl/<str:pk>', views.update_form_six_report_hgl.as_view(), name="update_form_six_report_hgl"),
    path('delete_form_six_report_hgl/<int:pk>/', views.delete_form_six_report_hgl, name="delete_form_six_report_hgl"),
    path('view_form_six_report_hgl/<int:pk>/', views.view_form_six_report_hgl.as_view(), name="view_form_six_report_hgl"),
    path('all_form_six_students_hgl/', views.all_form_six_students_hgl, name="all_form_six_students_hgl"),
    path('add_form6_students_hgl/', views.add_form6_students_hgl.as_view(), name="add_form6_students_hgl"),

    path('update_form_six_student_hgl/<str:pk>', views.update_form_six_student_hgl.as_view(), name="update_form_six_student_hgl"),
    path('delete_form_six_student_hgl/<int:pk>/', views.delete_form_six_student_hgl, name="delete_form_six_student_hgl"),

    

    path('search_form6_student_hgl/', views.search_form6_student_hgl, name="search_form6_student_hgl"),
    path('search_autoco_form_six_student2_hgl', views.search_autoco_form_six_student2_hgl, name="search_autoco_form_six_student2_hgl"),





    #HGK FORM 5 URLS
    path('sending_email_to_form_six_hgk/', views.sending_email_to_form_six_hgk, name="sending_email_to_form_six_hgk"),
    path('all_form_six_reports_hgk/', views.all_form_six_reports_hgk, name="all_form_six_reports_hgk"),
    path('search_autoco_form_six_report_hgk', views.search_autoco_form_six_report_hgk, name="search_autoco_form_six_report_hgk"),
    path('search_autoco_form_six_student_hgk', views.search_autoco_form_six_student_hgk, name="search_autoco_form_six_student_hgk"),

    path('update_form_six_report_hgk/<str:pk>', views.update_form_six_report_hgk.as_view(), name="update_form_six_report_hgk"),
    path('delete_form_six_report_hgk/<int:pk>/', views.delete_form_six_report_hgk, name="delete_form_six_report_hgk"),
    path('view_form_six_report_hgk/<int:pk>/', views.view_form_six_report_hgk.as_view(), name="view_form_six_report_hgk"),
    path('all_form_six_students_hgk/', views.all_form_six_students_hgk, name="all_form_six_students_hgk"),
    path('add_form6_students_hgk/', views.add_form6_students_hgk.as_view(), name="add_form6_students_hgk"),

    path('update_form_six_student_hgk/<str:pk>', views.update_form_six_student_hgk.as_view(), name="update_form_six_student_hgk"),
    path('delete_form_six_student_hgk/<int:pk>/', views.delete_form_six_student_hgk, name="delete_form_six_student_hgk"),

    

    path('search_form6_student_hgk/', views.search_form6_student_hgk, name="search_form6_student_hgk"),
    path('search_autoco_form_six_student2_hgk', views.search_autoco_form_six_student2_hgk, name="search_autoco_form_six_student2_hgk"),


    #CBG FORM 5 URLS
    path('sending_email_to_form_six_cbg/', views.sending_email_to_form_six_cbg, name="sending_email_to_form_six_cbg"),
    path('all_form_six_reports_cbg/', views.all_form_six_reports_cbg, name="all_form_six_reports_cbg"),
    path('search_autoco_form_six_report_cbg', views.search_autoco_form_six_report_cbg, name="search_autoco_form_six_report_cbg"),
    path('search_autoco_form_six_student_cbg', views.search_autoco_form_six_student_cbg, name="search_autoco_form_six_student_cbg"),

    path('update_form_six_report_cbg/<str:pk>', views.update_form_six_report_cbg.as_view(), name="update_form_six_report_cbg"),
    path('delete_form_six_report_cbg/<int:pk>/', views.delete_form_six_report_cbg, name="delete_form_six_report_cbg"),
    path('view_form_six_report_cbg/<int:pk>/', views.view_form_six_report_cbg.as_view(), name="view_form_six_report_cbg"),
    path('all_form_six_students_cbg/', views.all_form_six_students_cbg, name="all_form_six_students_cbg"),
    path('add_form6_students_cbg/', views.add_form6_students_cbg.as_view(), name="add_form6_students_cbg"),

    path('update_form_six_student_cbg/<str:pk>', views.update_form_six_student_cbg.as_view(), name="update_form_six_student_cbg"),
    path('delete_form_six_student_cbg/<int:pk>/', views.delete_form_six_student_cbg, name="delete_form_six_student_cbg"),

    

    path('search_form6_student_cbg/', views.search_form6_student_cbg, name="search_form6_student_cbg"),
    path('search_autoco_form_six_student2_cbg', views.search_autoco_form_six_student2_cbg, name="search_autoco_form_six_student2_cbg"),



    #HKL FORM 5  URLS
    path('sending_email_to_form_six_hkl/', views.sending_email_to_form_six_hkl, name="sending_email_to_form_six_hkl"),
    path('all_form_six_reports_hkl/', views.all_form_six_reports_hkl, name="all_form_six_reports_hkl"),
    path('search_autoco_form_six_report_hkl', views.search_autoco_form_six_report_hkl, name="search_autoco_form_six_report_hkl"),
    path('search_autoco_form_six_student_hkl', views.search_autoco_form_six_student_hkl, name="search_autoco_form_six_student_hkl"),

    path('update_form_six_report_hkl/<str:pk>', views.update_form_six_report_hkl.as_view(), name="update_form_six_report_hkl"),
    path('delete_form_six_report_hkl/<int:pk>/', views.delete_form_six_report_hkl, name="delete_form_six_report_hkl"),
    path('view_form_six_report_hkl/<int:pk>/', views.view_form_six_report_hkl.as_view(), name="view_form_six_report_hkl"),
    path('all_form_six_students_hkl/', views.all_form_six_students_hkl, name="all_form_six_students_hkl"),
    path('add_form6_students_hkl/', views.add_form6_students_hkl.as_view(), name="add_form6_students_hkl"),

    path('update_form_six_student_hkl/<str:pk>', views.update_form_six_student_hkl.as_view(), name="update_form_six_student_hkl"),
    path('delete_form_six_student_hkl/<int:pk>/', views.delete_form_six_student_hkl, name="delete_form_six_student_hkl"),

    

    path('search_form6_student_hkl/', views.search_form6_student_hkl, name="search_form6_student_hkl"),
    path('search_autoco_form_six_student2_hkl', views.search_autoco_form_six_student2_hkl, name="search_autoco_form_six_student2_hkl"),


    #ECA form6 URLS
    path('sending_email_to_form_six_eca/', views.sending_email_to_form_six_eca, name="sending_email_to_form_six_eca"),
    path('all_form_six_reports_eca/', views.all_form_six_reports_eca, name="all_form_six_reports_eca"),
    path('search_autoco_form_six_report_eca', views.search_autoco_form_six_report_eca, name="search_autoco_form_six_report_eca"),
    path('search_autoco_form_six_student_eca', views.search_autoco_form_six_student_eca, name="search_autoco_form_six_student_eca"),

    path('update_form_six_report_eca/<str:pk>', views.update_form_six_report_eca.as_view(), name="update_form_six_report_eca"),
    path('delete_form_six_report_eca/<int:pk>/', views.delete_form_six_report_eca, name="delete_form_six_report_eca"),
    path('view_form_six_report_eca/<int:pk>/', views.view_form_six_report_eca.as_view(), name="view_form_six_report_eca"),
    path('all_form_six_students_eca/', views.all_form_six_students_eca, name="all_form_six_students_eca"),
    path('add_form6_students_eca/', views.add_form6_students_eca.as_view(), name="add_form6_students_eca"),

    path('update_form_six_student_eca/<str:pk>', views.update_form_six_student_eca.as_view(), name="update_form_six_student_eca"),
    path('delete_form_six_student_eca/<int:pk>/', views.delete_form_six_student_eca, name="delete_form_six_student_eca"),

    

    path('search_form6_student_eca/', views.search_form6_student_eca, name="search_form6_student_eca"),
    path('search_autoco_form_six_student2_eca', views.search_autoco_form_six_student2_eca, name="search_autoco_form_six_student2_eca")

    

]