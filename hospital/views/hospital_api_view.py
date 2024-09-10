from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.response import Response
from datetime import datetime, timedelta
from rest_framework.views import APIView
import doctor.models  as doctorModels
from django.http import JsonResponse
from rest_framework import status
from hospital import serializers
from hospital import models
import logging

logger = logging.getLogger(__name__)

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = serializers.RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'phone_number': user.phone_number,
                'message': 'Registration successful'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = serializers.LoginSerializer(data=request.data)

        if serializer.is_valid():
            print("Validated Data:", serializer.validated_data)
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            print(email)
            print(password)
            
            user = serializer.validated_data.get('user')


            if user:
                access_token = str(RefreshToken.for_user(user).access_token)
                return Response({
                    'email': user.email,
                    'access_token': access_token,
                    'message': 'Login successful'
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''
@api_view(['GET'])
@permission_classes([IsAuthenticated])  
@authentication_classes([JWTAuthentication])
def get_hospitals_list_api(request):
    logger.info(f"Request User: {request.user}, Auth: {request.auth}")
    hospitals = models.Hospital.objects.all().prefetch_related('doctors')
    serializer = serializers.HospitalSerializer(hospitals, many=True)
    return Response({"result": serializer.data, "message": "Success", "status": 1})

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''
@api_view(['GET'])
@permission_classes([IsAuthenticated])  
@authentication_classes([JWTAuthentication])
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
@permission_classes([IsAuthenticated])  
@authentication_classes([JWTAuthentication])
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
@permission_classes([IsAuthenticated])  
@authentication_classes([JWTAuthentication])
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
@permission_classes([IsAuthenticated])  
@authentication_classes([JWTAuthentication])
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
@permission_classes([IsAuthenticated])  
@authentication_classes([JWTAuthentication])
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
@api_view(['GET'])
@permission_classes([IsAuthenticated])  
@authentication_classes([JWTAuthentication])
def get_hospital_beds_api(request):
    # Validate request parameters
    ward_id = request.GET.get('ward_id')
    hospital_id = request.GET.get('hospital_id')
    
    if not ward_id or not hospital_id:
        return Response({"error": "ward_id and hospital_id are required."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        ward_id = int(ward_id)
        hospital_id = int(hospital_id)
    except ValueError:
        return Response({"error": "Invalid ward_id or hospital_id."}, status=status.HTTP_400_BAD_REQUEST)
    
    # Get the beds based on ward_id and hospital_id
    beds = models.Bed.objects.filter(ward_id=ward_id, hospital_id=hospital_id).values(
        'id', 'hospital_id', 'ward_id', 'bed_count', 'bed_type', 'sale_price', 'sale_bed_price'
    )

    result = []
    for bed in beds:
        booked_bed_count = get_booked_bed_count(bed)
        available_count = bed['bed_count'] - booked_bed_count
        
        bed_list = []
        for i in range(1, bed['bed_count'] + 1):
            is_available = i > booked_bed_count

            # Calculate discount percentage
            if bed['sale_price'] > 0:  # Ensure no division by zero
                discount = ( (bed['sale_bed_price'] - bed['sale_price'])  / bed['sale_bed_price']) * 100
            else:
                discount = 0

            bed_list.append({
                'bed_number': i,
                'price': bed['sale_bed_price'],
                'sale_price': bed['sale_price'],
                'discount': round(discount),
                'isAvailable': is_available
            })

        bed['available_count'] = available_count
        bed['bedlist'] = bed_list
        result.append(bed)

    return Response({
        "result": result,
        "message": "Success",
        "status": 1
    }, status=status.HTTP_200_OK)


def get_booked_bed_count(bed):
    # Query the number of booked beds
    booked_bed_count = models.BedBooking.objects.filter(
        hospital_id=bed['hospital_id'],
        ward_type=bed['ward_id'],
        bed_type=bed['id'],
        status='accepted'
    ).count()
    print(booked_bed_count)
    return booked_bed_count

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''
@api_view(['GET'])
@permission_classes([IsAuthenticated])  
@authentication_classes([JWTAuthentication])
def get_booking_time_slots(request):
    start_time = datetime.strptime("00:00", "%H:%M")
    end_time = datetime.strptime("23:00", "%H:%M")
    time_slots = []

    while start_time <= end_time:
        time_slots.append({
            "slot_time": start_time.strftime("%H:%M"),
        })
        start_time += timedelta(hours=1)

    return JsonResponse({
        "result": time_slots,
        "message": "Success",
        "status": 1
    })

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''
@api_view(['GET'])
@permission_classes([IsAuthenticated])  
@authentication_classes([JWTAuthentication])
def get_blood_group_api(request):
    blood_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-","Don't Know"]
    
    return JsonResponse({
        "result": blood_groups,
        "message": "Success",
        "status": 1
    })
'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['POST'])
@permission_classes([IsAuthenticated])  
@authentication_classes([JWTAuthentication])
def store_bed_booking(request):
    serializer = serializers.BedBookingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "success","status":status.HTTP_201_CREATED}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])  
@authentication_classes([JWTAuthentication])
def hospital_all_bed_status(request):
    beds = models.Bed.objects.all()
    serializer = serializers.HospitalBedStatusSerializer(beds, many=True)
    return Response({"result": serializer.data})

