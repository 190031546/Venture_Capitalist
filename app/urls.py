from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.loginPage,name="login"),
    path('register/',views.registerPage,name="register"),
    path('logout/',views.logoutPage,name="logout"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('services/',views.services,name="services"),
    path('apply/',views.apply,name="apply"),
    path('portfolio/',views.portfolio,name="portfolio"),
    path('faqs/',views.faqs,name="faqs"),
    path('news/',views.news,name="news"),
    path('userpage/',views.userPage,name="user-page"),
    path('dashboard/',views.main,name="dashboard"),
    path('customer/<str:pk_test>/', views.customer, name="customer"),
    path('application/',views.application,name="application"),
    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    path('settings/',views.accountSettings,name="accountSettings"),
    path('membership/',views.membership,name="membership"),
    path('applymembership/',views.applymembership,name="applymembership"),
    path('payment/',views.payment,name="payment"),
    path('ask-question/', views.ask_question_view,name='ask-question'),
    path('question-history/', views.question_history_view,name='question-history'),
    path('admin-question/', views.admin_question_view,name='admin-question'),
    path('update-question/<int:pk>/', views.update_question_view,name='update-question'),
    path('admin-view-customer/', views.admin_view_customer_view,name='admin-view-customer'),
    path('update-customer/<int:pk>/', views.update_customer_view,name='update-customer'),
    path('delete-customer/<int:pk>/', views.delete_customer_view,name='delete-customer'),
    path('invest/<int:pk>/',views.invest,name="invest"),
    path('feed/', views.feed,name='feed'),
    path('feedhistory/', views.feedhistory,name='feedhistory'),
    path('investoridea/', views.investoridea,name='investoridea'),
    path('feedupdate/<int:pk>/', views.feedupdate,name='feedupdate'),

 path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="app/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="app/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="app/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="app/password_reset_done.html"), 
        name="password_reset_complete"),
]


