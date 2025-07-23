from rest_framework import generics
from .models import (
    ChargingPoint,
    ChargingSession,
    Booking,
    Profile,
    PaymentMethod,
    Payment,
    Rating,
    IssueReport,
    Comment,
    SubscriptionPlan,
    UserSubscription,
    ChargingStationAnalitics,
)

from .serializers import (
    ChargingPointSerializer,
    ChargingSessionSerializer,
    BookingSerializer,
    ProfileSerializer,
    PaymentMethodSerializer,
    PaymentSerializer,
    RatingSerializer,
    IssueReportSerializer,
    CommentSerializer,
    SubscriptionPlanSerializer,
    UserSubscriptionSerializer,
    ChargingStationAnaliticsSerializer,
)

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import send_session_complete_email

# Charging Points
class ChargingPointListCreateView(generics.ListCreateAPIView):
    queryset = ChargingPoint.objects.all()
    serializer_class = ChargingPointSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['location', 'name']


class ChargingPointDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChargingPoint.objects.all()
    serializer_class = ChargingPointSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]


# Charging Session
class ChargingSessionListCreateView(generics.ListCreateAPIView):
    queryset = ChargingSession.objects.all()
    serializer_class = ChargingSessionSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]


class ChargingSessionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChargingSession.objects.all()
    serializer_class = ChargingSessionSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]


# Charging Session Completion Notification
class ChargingSessionCompleteView(APIView):
    def post(self, request):
        user_email = request.data.get('email')
        station_name = request.data.get('station')

        send_session_complete_email.delay(user_email, station_name)
        return Response({"message": "Charging session marked complete. Email will be sent shortly."})


# Booking
class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]


class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]


# Profile
class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]


class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]


# Payment Method
class PaymentMethodListCreateView(generics.ListCreateAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination


class PaymentMethodDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination



class PaymentListCreateView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]


class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination


# Rating
class RatingListCreateView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]


class RatingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]


# Issue Report
class IssueReportListCreateView(generics.ListCreateAPIView):
    queryset = IssueReport.objects.all()
    serializer_class = IssueReportSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]


class IssueReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IssueReport.objects.all()
    serializer_class = IssueReportSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]


# Comment
class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]


class SubscriptionPlanListCreateView(generics.ListCreateAPIView):
    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination


class SubscriptionPlanDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]




# User Subscription
class UserSubscriptionCreateListView(generics.ListCreateAPIView):
    queryset = UserSubscription.objects.all()
    serializer_class = UserSubscriptionSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination


class UserSubscriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserSubscription.objects.all()
    serializer_class = UserSubscriptionSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination


# Charging Station Analytics
class ChargingStationAnaliticsCreateListView(generics.ListCreateAPIView):
    queryset = ChargingStationAnalitics.objects.all()
    serializer_class = ChargingStationAnaliticsSerializer
    permission_classes = [IsAuthenticated]


class ChargingStationAnaliticsDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ChargingStationAnalitics.objects.all()
    serializer_class = ChargingStationAnaliticsSerializer
