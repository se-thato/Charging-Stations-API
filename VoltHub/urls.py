from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import ( 
ChargingPointListCreateView,
ChargingPointDetailView,
ChargingSessionListCreateView,
ChargingSessionDetailView,
BookingListCreateView,
BookingDetailView,
ProfileListCreateView,
ProfileDetailView,
PaymentMethodListCreateView,
PaymentMethodDetailView,
PaymentListCreateView,
PaymentDetailView,
RatingListCreateView,
RatingDetailView,
IssueReportListCreateView,
IssueReportDetailView,
CommentListCreateView,
CommentDetailView,
SubscriptionPlanListCreateView,
SubscriptionPlanDetailView,
UserSubscriptionCreateListView,
UserSubscriptionDetailView,
ChargingStationAnaliticsCreateListView,
ChargingStationAnaliticsDetailView,
)





urlpatterns = [
    path('stations-list/', ChargingPointListCreateView.as_view(), name="stations-list"),
    path('stations-list/<int:pk>/', ChargingPointDetailView.as_view(), name="stations-list-details"), 
  

    path('charging-sessions/', ChargingSessionListCreateView.as_view(), name ="charging_session"),
    path('charging-sessions/<int:pk>/', ChargingSessionDetailView.as_view(), name="charging_sessions_details"),
    
    #bookings
    path('bookings/', BookingListCreateView.as_view(), name="bookings"),
    path('bookings/<int:pk>/', BookingDetailView.as_view(), name="bookings-details"),

    #profile
    path('profiles/', ProfileListCreateView.as_view(), name="profiles"),
    path('profiles/<int:pk>/', ProfileDetailView.as_view(), name="profiles-details"),

    #payment section
    path('payment-method/', PaymentMethodListCreateView.as_view(), name="payment-method"),
    path('payment-method/<int:pk>/',PaymentMethodDetailView.as_view(), name="payment-method-details"),


    path('payment/', PaymentListCreateView.as_view(), name="payment"),
    path('payment/<int:pk>/',PaymentDetailView.as_view(), name="payment-details"),

    #rating
    path('ratings/', RatingListCreateView.as_view(), name="ratings"),
     path('ratings/<int:pk>/', RatingDetailView.as_view(), name="ratings-details"),

    #issue report
    path('issue-reports/', IssueReportListCreateView.as_view(), name="issue-reports"),
    path('issue-reports/<int:pk>/', IssueReportDetailView.as_view(), name="issue-reports-details"),

    #comments
    path('comments/', CommentListCreateView.as_view(), name="comments"),
     path('comments/<int:pk>/', CommentDetailView.as_view(), name="comments-details"),

    #reset password
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="VoltHub/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="VoltHub/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="VoltHub/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="VoltHub/password_reset_done.html"), name="password_reset_complete"),

    #subscription plan
    path('subscription_plans/', SubscriptionPlanListCreateView.as_view(), name="subscription_plans"),
    path('subscription_plans/<int:pk>/', SubscriptionPlanDetailView.as_view(), name="subscription_plans_details"),

    path('user-subscription/', UserSubscriptionCreateListView.as_view(), name="user-subscription"),
    path('user-subscription/<int:pk>/', UserSubscriptionDetailView.as_view(), name="user-subscription-details"),

    #charging station analytics
    path('charging-station-analytics/', ChargingStationAnaliticsCreateListView.as_view(), name="charging-station-analytics"),
    path('charging-station-analytics<int:pk>/', ChargingStationAnaliticsDetailView.as_view(), name="charging-station-analytics-details"),


    
   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


