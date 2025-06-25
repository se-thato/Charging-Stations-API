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
Comment, SubscriptionPlan, 
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
ChargingStationAnaliticsSerializer
)

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

import stripe
from django.conf import settings
from django.http import JsonResponse
from rest_framework.views import APIView



#charging points views 
class ChargingPointListCreateView(generics.ListCreateAPIView):
    queryset = ChargingPoint.objects.all()
    serializer_class = ChargingPointSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    #search filter
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['location', 'name']



class ChargingPointDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChargingPoint.objects.all()
    serializer_class = ChargingPointSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]

   


#charging session 
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

    def create(self, request, *args, **kwargs):       
        stripe.api_key = settings.STRIPE_SECRET_KEY

        try:
            stripe_price_id = request.data.get('stripe_price_id')

            # Optional: You might extract `quantity` from request.data
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price': stripe_price_id,
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=settings.my_DOMAIN + '/success/',
                cancel_url=settings.my_DOMAIN + '/cancel/',
            )

            # Optionally, create a Payment record in your DB
            payment = Payment.objects.create(
                user=request.user.profile,  # or just request.user if no profile
                amount=0,
                status='pending',  # later update this via Stripe webhook
                stripe_checkout_url=checkout_session.url,  # If you add this field
            )

            return JsonResponse({'checkout_url': checkout_session.url})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)





class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination



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

 

#Subcribtion plan views
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

  

class SubscriptionPlanCheckoutSession(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        plan_id = request.data.get('plan_id')

        if not plan_id:
            return JsonResponse({'error': 'Missing plan_id'}, status=400)

        try:
            plan = SubscriptionPlan.objects.get(id=plan_id)
            stripe_price_id = plan.stripe_price_id
        except SubscriptionPlan.DoesNotExist:
            return JsonResponse({'error': 'Subscription plan not found'}, status=404)

        try:
            YOUR_DOMAIN = "http://localhost:8000" 

            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price': stripe_price_id,
                        'quantity': 1,
                    },
                ],
                mode='subscription',
                success_url=YOUR_DOMAIN + '/success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=YOUR_DOMAIN + '/cancel',
                customer_email=request.user.email,
            )

            return JsonResponse({'checkout_url': checkout_session.url})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)



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

    


class ChargingStationAnaliticsCreateListView(generics.ListCreateAPIView):
    queryset = ChargingStationAnalitics.objects.all()
    serializer_class = ChargingStationAnaliticsSerializer
    permission_classes = [IsAuthenticated]

 


class ChargingStationAnaliticsDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ChargingStationAnalitics.objects.all()
    serializer_class = ChargingStationAnaliticsSerializer

    




