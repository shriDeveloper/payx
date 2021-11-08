from django.urls import path , include
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap
from . import views


sitemaps = {
    'post':PostSitemap
}


urlpatterns = [
	path('',views.homepage,name='home-page'),

	path('group/<int:group_id>',views.group , name='group-page'),
	path('group/add',views.create_group,name='create-group-page'),
	path('group/edit/<int:group_id>',views.update_group,name='update-group-page'),
	path('group/delete/<int:group_id>',views.delete_group,name='delete-group-page'),

	path('user/login',views.login_user,name='user-login-page'),
	path('user/logout',views.logout_user,name='user-logout-page'),
	path('user/signup',views.signup_user,name='user-signup-page'),
	path('post/<int:post_id>/<slug:post_slug>',views.view_post,name='view-post-page'),

	#sitemap here
	path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]