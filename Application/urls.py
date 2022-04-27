from django.urls import path


from Application.views import *

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('login', LogIn.as_view(), name="login"),
    path('home', MainBody.as_view(), name="MainBody"),
    path('detail/<int:id>', DetailBlog.as_view(), name="Detailed_Blog"),
    path('addblog', AddBlog.as_view(), name="Add_Blog"),
    path('addcategory', AddCategory.as_view(), name="Add_Category"),
    path('profile/<str:username>', Profile.as_view(), name="Profile"),
    path('logout', Logout.as_view(), name="Logout"),
    # path('signup', Signup.as_view(), name="Signup"),
    path('loggedinProf/update/<int:pk>', UpdatePost.as_view(), name="updateblog"),
    path('loggedinProf/<str:username>', LoggedInUser.as_view(), name="LoggedInUser"),
    path('category/<str:catergories>',CategoryView.as_view(), name="category"),
    path('searchblog',SearchBlog.as_view(), name="searchblog"),
    path('loggedinProf/<int:pk>/delete', DeletePost.as_view(), name="deleteblog"),
]