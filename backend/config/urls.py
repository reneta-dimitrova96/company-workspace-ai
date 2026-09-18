"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from ideas.views import IdeaListCreateView, IdeaVoteView, IdeaDetailView
from users.views import RegisterUserView, CurrentUserView
from tickets.views import TicketListCreateView, TicketDetailView, TicketCommentListCreateView

urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "api/auth/login/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "api/auth/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),

    path(
        "api/auth/register/",
        RegisterUserView.as_view(),
        name="register",
    ),

    path(
        "api/auth/me/",
        CurrentUserView.as_view(),
        name="get_current_user",
    ),

    path(
        "api/tickets/",
        TicketListCreateView.as_view(),
        name="ticket-list-create",
    ),

    path(
        "api/tickets/<int:pk>/",
        TicketDetailView.as_view(),
        name="ticket-detail",
    ),

    path(
        "api/tickets/<int:ticket_id>/comments/",
        TicketCommentListCreateView.as_view(),
        name="ticket-comment-list-create",
    ),

    path(
        "api/ideas/",
        IdeaListCreateView.as_view(),
        name="idea-list-create",
    ),

    path(
        "api/ideas/<int:idea_id>/vote/",
        IdeaVoteView.as_view(),
        name="idea-vote",
    ),

    path(
        "api/ideas/<int:pk>/",
        IdeaDetailView.as_view(),
        name="idea-detail",
    ),
]
