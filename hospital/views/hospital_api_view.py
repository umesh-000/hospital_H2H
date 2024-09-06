from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import generics, status
from hospital import serializers
from hospital import models
import doctor.models  as doctorModels

class RegisterView(generics.CreateAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        customer = serializer.save()
        if customer:
            # Generate JWT tokens for the customer
            refresh = RefreshToken.for_user(customer)
            headers = self.get_success_headers(serializer.data)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "message": "Registration Successful",
                "status": 1
            }, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'error': 'Customer creation failed'}, status=status.HTTP_400_BAD_REQUEST)

class LoginView(generics.GenericAPIView):
    serializer_class = serializers.LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        customer = serializer.validated_data['customer']

        if customer:
            # Generate JWT tokens for the customer
            refresh = RefreshToken.for_user(customer)
            return Response({
                "result": {
                    "id": customer.id,
                    "customer_name": customer.customer_name,
                    "phone_number": customer.phone_number,
                    "email": customer.email,
                },
                "refresh": str(refresh),
                "access_token": str(refresh.access_token),
                "message": "Login Successful",
                "status": 1
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        
'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''
@api_view(['GET'])
@permission_classes([AllowAny])  # This line allows unauthenticated access
def get_hospitals_api(request):
    hospitals = models.Hospital.objects.all().prefetch_related('doctors')
    print(hospitals)
    serializer = serializers.HospitalSerializer(hospitals, many=True)
    return Response({"result": serializer.data})
    
'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''
@api_view(['GET'])
@permission_classes([AllowAny])
def hospital_all_facilities(request):
    hospital_id = request.GET.get('hospital_id')

    if not hospital_id:
        return Response({"error": "hospital_id query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        hospital = models.Hospital.objects.get(id=hospital_id)
        hospital_facilities = models.HospitalFacility.objects.filter(hospital=hospital)
        serializer = serializers.HospitalFacilitySerializer(hospital_facilities, many=True)
        return Response({"result": serializer.data}, status=status.HTTP_200_OK)
    except models.Hospital.DoesNotExist:
        return Response({"error": "Hospital not found."}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
@permission_classes([AllowAny])
def get_hospital_details(request):
    hospital_id = request.GET.get('hospital_id')  # Extract hospital_id from the GET parameters
    
    if not hospital_id:
        return Response({"error": "hospital_id is required."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        # Correctly use the related_name for prefetch_related
        hospital = models.Hospital.objects.prefetch_related('facilities', 'services').get(id=hospital_id)
        serializer = serializers.HospitalDetailsSerializer(hospital)
        return Response({"result": serializer.data}, status=status.HTTP_200_OK)
    except models.Hospital.DoesNotExist:
        return Response({"error": "Hospital not found."}, status=status.HTTP_404_NOT_FOUND)
'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['GET'])
@permission_classes([AllowAny])
def get_specialities_api(request):
    specialities = doctorModels.DoctorSpecialistCategory.objects.all()
    serializer = serializers.SpecialistCategorySerializer(specialities, many=True, context={'request': request})
    return Response({
        "result": serializer.data,
        "count": specialities.count(),
        "message": "Success",
        "status": 1
    }, status=status.HTTP_200_OK)

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''
@api_view(['GET'])
@permission_classes([AllowAny])
def get_symptoms_api(request):
    specialist_id = request.GET.get('specialist_id')
    print(specialist_id)

    if not specialist_id:
        return Response({"error": "specialist_id is required."}, status=status.HTTP_400_BAD_REQUEST)

    symptoms = doctorModels.Symptom.objects.filter(specialist_id=specialist_id, status=1)
    serializer = serializers.SymptomSerializer(symptoms, many=True, context={'request': request})
    
    return Response({
        "result": serializer.data,
        "count": symptoms.count(),
        "message": "Success",
        "status": 1
    }, status=status.HTTP_200_OK)


'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['GET'])
@permission_classes([AllowAny])
def get_hospital_wards_api(request):
    hospital_id = request.GET.get('hospital_id')
    if not hospital_id:
        return Response({"error": "hospital_id is required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        hospital = models.Hospital.objects.get(id=hospital_id)
        wards = models.Ward.objects.filter(hospital=hospital, status=1)
        serializer = serializers.WardSerializer(wards, many=True)
        return Response({
            "result": serializer.data,
            "count": wards.count(),
            "message": "Success",
            "status": 1
        }, status=status.HTTP_200_OK)
    except models.Hospital.DoesNotExist:
        return Response({"error": "Hospital not found."}, status=status.HTTP_404_NOT_FOUND)
'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''





'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['POST'])
@permission_classes([AllowAny])
def store_bed_booking(request):
    serializer = serializers.BedBookingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "success","status":status.HTTP_201_CREATED}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def hospital_all_bed_status(request):
    beds = models.Bed.objects.all()
    serializer = serializers.HospitalBedStatusSerializer(beds, many=True)
    return Response({"result": serializer.data})

