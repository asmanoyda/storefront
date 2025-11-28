from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import datetime
from playground.models import (
    Member,
    Cars,
    Stocks,
    Chocos,
    Students,
    Peoples,
    User,
    Companys,
    Teachers,
    Cold_drinks,
)
from django.urls import reverse
from django.template import loader
from django.shortcuts import redirect
from django.contrib import messages


# Create your views here.
# request  -> response
# request  handler
# action
def home(request):
    return render(request, "home.html", {})


def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    if request.method == "POST":
        name = request.POST.get("name")
        username = request.POST.get("username")
        mobile = request.POST.get("mobile_no")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            print("send a error method from i got called")
            messages.error(request, "Username already exists")
            return redirect("login_user")

        if User.objects.filter(email=email).exists():
            return JsonResponse({"error": "Email already exisis"}, status=400)

        user = User(name=name, username=username,
                    mobile_no=mobile, email=email)
        user.set_password(password)
        user.save()
        return JsonResponse({"message": "User registered succesfully"})
    return JsonResponse({"error": "Invalid method"}, status=400)


def login_user(request):
    if request.method == "GET":
        return render(request, "login.html")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            print("send a error method from i got called")
            messages.error(request, " username does not exist! ")
            return redirect("login_user")

        if user.check_password(password):
            request.session["user_id"] = user.id
            request.session["username"] = user.username
            return redirect("home")
        else:

            messages.error(request, "Invalid password! ")
            return redirect("login_user")

    messages.error(request, "Invalid method! ")
    return redirect("login_user")


def logout_user(request):

    request.session.flush()
    return render(request, "logout.html")


def say_hello(request):
    # pull data frome db
    # Transform
    # send email
    x = 1
    y = 2
    x = "jamil"
    return render(request, "hello.html", {"name": "Asma", "name_2": x})


def peoples(request):
    peoples = Peoples.objects.all()
    return render(request, "peoples.html", {"peoples": peoples})


def cold_drinks(request):
    cold_drinks = Cold_drinks.objects.all()
    return render(request, "cold_drinks.html", {"cold_drinks": cold_drinks})


def members(request):
    members = Member.objects.all()
    return render(request, "members.html", {"members": members})


def cars(request):
    cars = Cars.objects.all()
    return render(request, "cars.html", {"cars": cars})


def teachers(request):
    teachers = Teachers.objects.all()
    print("hello")
    return render(request, "teachers.html", {"teachers": teachers})


def stocks(request):
    stocks = Stocks.objects.all()
    return render(request, "stocks.html", {"stocks": stocks})


def chocos(request):
    chocolates = Chocos.objects.all()
    text = """Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi molestiae, illo animi veniam ea repellendus, omnis reiciendis adipisci quasi dolore accusantium sit magnam, eos dolor! Magnam tenetur reiciendis similique esse?"""
    return render(request, "chocos.html", {"chocos": chocolates, "text": text})


def students(request):
    students = Students.objects.all()

    return render(request, "students.html", {"students": students})


def companys(request):
    companys = Companys.objects.all()
    return render(request, "companys.html", {"companys": companys})


def get_stock(request, id):
    s_one = Stocks.objects.get(id=id)
    print(s_one)
    return render(request, "s_detail.html", {"stock": s_one})


def get_cold_drink(request, id):
    cd_one = Cold_drinks.objects.get(id=id)
    print(cd_one)
    return render(request, "cd_detail.html", {"cold_drink": cd_one})


def get_teacher(request, id):
    t_one = Teachers.objects.get(id=id)
    print(t_one)
    return render(request, "t_detail.html", {"teacher": t_one})


def get_choco(request, id):
    ch_one = Chocos.objects.get(id=id)
    print(ch_one)
    return render(request, "c_detail.html", {"choco": ch_one})


def get_comapny(request, id):

    co_one = Companys.objects.get(id=id)
    print(co_one.name)
    print(co_one.sector)

    return render(request, "company_detail.html", {"company": co_one})


def get_car(request, id):
    c_one = Cars.objects.get(id=id)
    print(c_one)
    return render(request, "car_detail.html", {"car": c_one})


def get_member(request, id):
    m_one = Member.objects.get(id=id)
    print(m_one)
    return render(request, "m_detail.html", {"member": m_one})


def get_student(request, id):
    st_one = Students.objects.get(id=id)
    print(st_one)
    return render(request, "st_detail.html", {"student": st_one})


def delete_choco(request, id):
    choco = Chocos.objects.get(id=id)
    choco.delete()
    return HttpResponseRedirect(reverse("chocos"))


def delete_cold_drink(request, id):
    cold_drink = Cold_drinks.objects.get(id=id)
    cold_drink.delete()
    return HttpResponseRedirect(reverse("cold_drinks"))


def delete_teacher(request, id):
    teacher = Teachers.objects.get(id=id)
    teacher.delete()
    return HttpResponseRedirect(reverse("teachers"))


def delete_comapny(request, id):
    comapny = Companys.objects.get(id=id)
    comapny.delete()
    return HttpResponseRedirect(reverse("companys"))


def delete_people(request, id):
    people = Peoples.objects.get(id=id)
    people.delete()
    return HttpResponseRedirect(reverse("peoples"))


def delete_member(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse("members"))


def delete_student(request, id):
    student = Students.objects.get(id=id)
    student.delete()
    return HttpResponseRedirect(reverse("students"))


def delete_stock(request, id):
    stock = Stocks.objects.get(id=id)
    stock.delete()
    return HttpResponseRedirect(reverse("stocks"))


def delete_car(request, id):
    car = Cars.objects.get(id=id)
    car.delete()
    return HttpResponseRedirect(reverse("cars"))


def add_member(request):
    template = loader.get_template("add_member.html")
    return HttpResponse(template.render({}, request))


def add_member_save(request):
    x = request.POST["first"]
    y = request.POST["last"]
    member = Member(firstname=x, lastname=y)
    member.save()
    return HttpResponseRedirect(reverse("members"))


def add_teacher(request):
    template = loader.get_template("add_teacher.html")
    return HttpResponse(template.render({}, request))


def add_teacher_save(request):
    x = request.POST["name"]
    y = request.POST["subject"]
    print("hello stupid")

    teacher = Teachers(name=x, subject=y)
    teacher.save()
    return HttpResponseRedirect(reverse("teachers"))


def add_choco(request):
    template = loader.get_template("add_choco.html")
    return HttpResponse(template.render({}, request))


def add_choco_save(request):
    x = request.POST["brand"]
    y = request.POST["type"]
    a = request.POST["cocoa_percentage"]
    b = request.POST["price"]
    c = request.POST["sugar_percentage"]

    choco = Chocos(brand=x, type=y, cocoa_percentage=a,
                   price=b, sugar_percentage=c)
    choco.save()
    return HttpResponseRedirect(reverse("chocos"))


def add_student(request):
    template = loader.get_template("add_student.html")
    return HttpResponse(template.render({}, request))


def add_student_save(request):
    x = request.POST["name"]
    y = request.POST["age"]
    a = request.POST["major"]
    b = request.POST["grades"]

    student = Students(name=x, age=y, major=a, grades=b)
    student.save()
    return HttpResponseRedirect(reverse("students"))


def add_stock(request):
    template = loader.get_template("add_stock.html")
    return HttpResponse(template.render({}, request))


def add_stock_save(request):
    x = request.POST["name"]
    y = request.POST["price"]
    a = request.POST["sector"]

    stock = Stocks(name=x, price=y, sector=a)
    stock.save()
    return HttpResponseRedirect(reverse("stocks"))


def add_car(request):
    template = loader.get_template("add_car.html")
    return HttpResponse(template.render({}, request))


def add_car_save(request):
    x = request.POST["model"]
    y = request.POST["year"]
    a = request.POST["color"]

    car = Cars(model=x, year=y, color=a)
    car.save()
    return HttpResponseRedirect(reverse("cars"))


def add_company(request):
    template = loader.get_template("add_company.html")
    return HttpResponse(template.render({}, request))


def add_company_save(request):
    x = request.POST["name"]
    y = request.POST["sector"]
    a = request.POST["location"]

    company = Companys(name=x, sector=y, location=a)
    company.save()
    return HttpResponseRedirect(reverse("companys"))


def add_people(request):
    template = loader.get_template("add_people.html")
    return HttpResponse(template.render({}, request))


def add_people_save(request):
    x = request.POST["name"]
    y = request.POST["age"]
    a = request.POST["surname"]


    people = Peoples(
        name=x,
        surname=a,
        age=y,
    )
    people.save()
    return HttpResponseRedirect(reverse("peoples"))


def add_cold_drink(request):
    template = loader.get_template("add_cold_drink.html")
    return HttpResponse(template.render({}, request))


def add_cold_drink_save(request):
    x = request.POST["name"]
    y = request.POST["brand"]

    a = request.POST["flavor"]

    cold_drink = Cold_drinks(
        name=x,
        brand=y,
        flavor=a,


    )
    cold_drink.save()
    return HttpResponseRedirect(reverse("cold_drinks"))
