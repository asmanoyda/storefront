from django.urls import path
from . import views


# URLCONFIGRATION
urlpatterns = [
    path("members/", views.members, name="members"),
    path("peoples/", views.peoples,name="peoples"),
    path("companys/", views.companys,name="companys"),
    path("teachers/", views.teachers,name="teachers"),
    path("cold_drinks/", views.cold_drinks,name="cold_drinks"),




    path("cars/", views.cars, name="cars"),
    path("stocks/", views.stocks, name="stocks"),
    path("chocos/", views.chocos, name="chocos"),
    path("students/", views.students, name="students"),
    path("get-stock/<int:id>", views.get_stock, name="s_name"),
    path("get-choco/<int:id>", views.get_choco, name="ch_name"),
    path("get-company/<int:id>", views.get_comapny, name="co_name"),
    path("get-teacher/<int:id>", views.get_teacher, name="t_name"),
    path("get-cold-drink/<int:id>", views.get_cold_drink, name="cd_name"),



    path("get-car/<int:id>", views.get_car, name="c_name"),
    path("get-member/<int:id>", views.get_member, name="m_name"),
    path("get-student/<int:id>", views.get_student, name="st_name"),
    path("", views.home, name="home"),

    path("delete-choco/<int:id>", views.delete_choco, name="delete-choco"),
    path("delete-company/<int:id>", views.delete_comapny, name="delete-company"),
    path("delete-people/<int:id>", views.delete_people, name="delete-people"),
    path("delete-teacher/<int:id>", views.delete_teacher, name="delete-teacher"),
    path("delete-cold-drink/<int:id>", views.delete_cold_drink, name="delete-cold-drink"),





    path("delete-member/<int:id>", views.delete_member, name="delete-member"),
    path("delete-student/<int:id>", views.delete_student, name="delete-student"),
    path("delete-stock/<int:id>", views.delete_stock, name="delete-stock"),
    path("delete-car/<int:id>", views.delete_car, name="delete-car"),

    path("add-member/", views.add_member, name="add-member"),
    path("add-member-save/", views.add_member_save, name="add-member-save"),

    path("add-cold_drink/", views.add_cold_drink, name="add-cold_drink"),
    path("add-cold_drink-save/", views.add_cold_drink_save, name="add-cold_drink-save"),

    path("add-choco/", views.add_choco, name="add-choco"),
    path("add-choco-save/", views.add_choco_save, name="add-choco-save"),


    path("add-teacher/", views.add_teacher, name="add-teacher"),
    path("add-teacher-save/", views.add_teacher_save, name="add-teacher-save"),
    
    path("add-student/", views.add_student, name="add-student"),
    path("add-student-save/", views.add_student_save, name="add-student-save"),

    path("add-stock/", views.add_stock, name="add-stock"),
    path("add-stock-save/", views.add_stock_save, name="add-stock-save"),

    path("add-car/", views.add_car, name="add-car"),
    path("add-car-save/", views.add_car_save, name="add-car-save"),


    path("add-company/", views.add_company, name="add-company"),
    path("add-company-save/", views.add_company_save, name="add-company-save"),


    path("add-people/", views.add_people, name="add-people"),
    path("add-people-save/", views.add_people_save, name="add-people-save"),

  

    path("user/register/", views.register, name="register"),
    path("user/login/", views.login_user, name="login_user"),
    path("user/logout/", views.logout_user, name="logout"),
]
