from django.contrib import admin
from django.urls import path
from askmeapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    # Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('signin/', views.signinuser, name='signinuser'),
    path('signout/', views.signoutuser, name='signoutuser'),

    #deleteも入れたい

    # Askme
    path('', views.home, name='home'),
    path('allquestions/', views.allquestions, name='allquestions'),
    path('askquestion/', views.askquestion, name='askquestion'),
    path('myquestions/', views.myquestions, name='myquestions'),
    path('checkmines/<int:mine_pk>/', views.checkmines, name='checkmines'),
    path('checkdetail/<int:detail_pk>/', views.checkdetail, name='checkdetail'),
    path('editquestion/<int:edit_pk>/', views.editquestion, name='editquestion'),
    path('question/<int:question_pk>/delete/', views.deletequestion, name='deletequestion'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)