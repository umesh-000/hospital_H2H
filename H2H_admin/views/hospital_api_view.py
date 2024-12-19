from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.exceptions import ObjectDoesNotExist
from H2H_admin import serializers as API_serializers
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta ,timezone
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404
from math import radians, cos, sin, asin, sqrt
from accounts import models as account_models
from H2H_admin import models as admin_models
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Prefetch
from django.http import JsonResponse
from django.db.models import Count
from rest_framework import status
from django.conf import settings
from django.db import models
import logging
import random
import json


logger = logging.getLogger(__name__)

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print("Received form-data:", request.data)
        serializer = API_serializers.RegisterSerializer(data=request.data)
        if serializer.is_valid():
            customer = serializer.save()
            return Response(
                {
                    'message': 'Registration successful',
                    'email': customer.user.email,
                    'customer_name': customer.customer_name,
                    'phone_number': customer.phone_number,
                },
                status=status.HTTP_201_CREATED,
            )
        logger.error("Validation errors: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = API_serializers.LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data.get('user')
            if user:
                refresh = RefreshToken.for_user(user)
                access_token_expiry = datetime.now() + settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME']
                # Calculate expiry time in minutes
                access_token_expiry_minutes = int(settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'].total_seconds() // 60)
                return Response({
                    'email': user.email,
                    'user_type': user.user_type,
                    'access_token': str(refresh.access_token),
                    'access_token_expiry': f"{access_token_expiry_minutes} minutes",
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
    try:
        # Retrieve all hospitals and their associated doctors
        hospitals = account_models.Hospital.objects.prefetch_related( Prefetch('doctors', queryset=account_models.DoctorDetails.objects.filter(status=1)) ).filter(status=1)
        serializer = API_serializers.HospitalSerializer(hospitals, many=True)

        return Response({
            "result": serializer.data,
            "message": "Success",
            "status": 1
        }, status=status.HTTP_200_OK)

    except Exception as e:
        logger.error(f"Error fetching hospitals list: {e}")
        return Response({
            "message": "An error occurred while fetching hospital data.",
            "status": 0
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''
 

@api_view(['GET'])
@permission_classes([AllowAny])
@permission_classes([IsAuthenticated])  
@authentication_classes([JWTAuthentication])
def get_hospital_details(request):
    hospital_id = request.GET.get('hospital_id')
    
    if not hospital_id:
        return Response({"error": "hospital_id is required."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        # Correctly use the related_name for prefetch_related
        hospital = account_models.Hospital.objects.prefetch_related('facilities', 'services').get(id=hospital_id)
        serializer = API_serializers.HospitalDetailsSerializer(hospital)
        return Response({"result": serializer.data}, status=status.HTTP_200_OK)
    except account_models.Hospital.DoesNotExist:
        return Response({"error": "Hospital not found."}, status=status.HTTP_404_NOT_FOUND)
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
        time_slots.append({ "slot_time": start_time.strftime("%H:%M"), })
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
def get_specialities_api(request):
    specialities = admin_models.SpecialistCategory.objects.all()
    serializer = API_serializers.SpecialistCategorySerializer(specialities, many=True, context={'request': request})
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

    symptoms = admin_models.Symptom.objects.filter(specialist_id=specialist_id, status=1)
    serializer = API_serializers.SymptomSerializer(symptoms, many=True, context={'request': request})
    
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
        hospital = account_models.Hospital.objects.get(id=hospital_id)
        wards = admin_models.Ward.objects.filter(hospital=hospital, status=1)
        serializer = API_serializers.WardSerializer(wards, many=True)
        return Response({
            "result": serializer.data,
            "count": wards.count(),
            "message": "Success",
            "status": 1
        }, status=status.HTTP_200_OK)
    except account_models.Hospital.DoesNotExist:
        return Response({"error": "Hospital not found."}, status=status.HTTP_404_NOT_FOUND)

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['GET'])
@permission_classes([IsAuthenticated])  
@authentication_classes([JWTAuthentication])
def get_hospital_beds_api(request):
    ward_id = request.GET.get('ward_id')
    hospital_id = request.GET.get('hospital_id')
    if not ward_id or not hospital_id:
        return Response({"error": "ward_id and hospital_id are required."}, status=status.HTTP_400_BAD_REQUEST)
    try:
        ward_id = int(ward_id)
        hospital_id = int(hospital_id)
    except ValueError:
        return Response({"error": "Invalid ward_id or hospital_id."}, status=status.HTTP_400_BAD_REQUEST)
    beds = admin_models.Bed.objects.filter(ward_id=ward_id, hospital_id=hospital_id).values( 'id', 'hospital_id', 'ward_id', 'bed_count', 'bed_type', 'sale_price', 'sale_bed_price' )
    result = []
    for bed in beds:
        booked_bed_count = get_booked_bed_count(bed)
        available_count = bed['bed_count'] - booked_bed_count
        
        bed_list = []
        for i in range(1, bed['bed_count'] + 1):
            is_available = i > booked_bed_count
            if bed['sale_price'] > 0:
                discount = ( (bed['sale_bed_price'] - bed['sale_price'])  / bed['sale_bed_price']) * 100
            else:
                discount = 0
            bed_list.append({ 'bed_number': i, 'price': bed['sale_bed_price'], 'sale_price': bed['sale_price'], 'discount': round(discount), 'isAvailable': is_available })
        bed['available_count'] = available_count
        bed['bedlist'] = bed_list
        result.append(bed)
    return Response({
        "result": result,
        "message": "Success",
        "status": 1
    }, status=status.HTTP_200_OK)


def get_booked_bed_count(bed):
    booked_bed_count = admin_models.BedBooking.objects.filter( hospital_id=bed['hospital_id'], ward_type=bed['ward_id'], bed_type=bed['id'], status='accepted' ).count()
    return booked_bed_count

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
# Helper function for validating booking data
def validate_booking_data(customer_id, hospital_id, **kwargs):
    customer = account_models.Customer.objects.filter(pk=customer_id, status=1).first()
    if not customer:
        raise ValidationError(f"Customer with ID {customer_id} does not exist or is inactive.")
    hospital = account_models.Hospital.objects.filter(pk=hospital_id, status=1).first()
    if not hospital:
        raise ValidationError(f"Hospital with ID {hospital_id} does not exist or is inactive.")

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def store_bed_booking(request):
    try:
        data = request.data
        serializer = API_serializers.BedBookingSerializer(data=data)
        if not serializer.is_valid():
            return Response({"message": "Validation failed.", "errors": serializer.errors},status=status.HTTP_400_BAD_REQUEST,)
        validate_booking_data(customer_id=data.get('customer_id'),hospital_id=data.get('hospital'),admission_date=data.get('admission_date'))

        booking = admin_models.BedBooking.objects.create(
            customer_id=data.get('customer_id'),
            hospital_id=data.get('hospital'),
            ward_type=data.get('ward_type'),
            bed_type=data.get('bed_type'),
            booking_type=data.get('booking_type'),
            booking_date=data.get('booking_date'),
            admission_date=data.get('admission_date'),
            time_slot=data.get('time_slot'),
            patient_name=data.get('patient_name'),
            age=data.get('age'),
            blood_group=data.get('blood_group'),
            email=data.get('email'),
            contact_number=data.get('contact_number'),
            emergency_contact=data.get('emergency_contact'),
            medical_history=data.get('medical_history'),
            booking_reason=data.get('booking_reason'),
            insurance_info=data.get('insurance_info'),
            notes=data.get('notes'),
            status=data.get('status'),
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )

        # Prepare the response payload
        result = {
            "id": booking.id,
            "customer_id": booking.customer.id,
            "hospital_id": booking.hospital.id,
            "ward_type": booking.ward_type,
            "bed_type": booking.bed_type,
            "booking_type": booking.booking_type,
            "booking_date": booking.booking_date,
            "admission_date": booking.admission_date,
            "time_slot": booking.time_slot,
            "patient_name": booking.patient_name,
            "age": booking.age,
            "blood_group": booking.blood_group,
            "email": booking.email,
            "contact_number": booking.contact_number,
            "emergency_contact": booking.emergency_contact,
            "medical_history": booking.medical_history,
            "booking_reason": booking.booking_reason,
            "insurance_info": booking.insurance_info,
            "status": booking.status,
            "notes": booking.notes,
            "bed_price": 800,  # Replace with the actual value or calculation logic
            "base_rate": 800,  # Replace with the actual value or calculation logic
            "tax": 0,  # Replace with the actual value or calculation logic
            "additional_charges": 0,  # Replace with the actual value or calculation logic
            "discount": 0,  # Replace with the actual value or calculation logic
            "total": 800,  # Replace with the actual value or calculation logic
            "final_total": 800,  # Replace with the actual value or calculation logic
            "booking_number": "H2H241200",  # Replace with the actual booking number logic
            "created_at": booking.created_at.isoformat(),
            "updated_at": booking.updated_at.isoformat(),
        }
        return Response({"success": True, "message": "Booking created successfully", "result": result},status=status.HTTP_201_CREATED,)
    except ValidationError as ve:
        return Response({"message": "Validation error.", "errors": str(ve)},status=status.HTTP_400_BAD_REQUEST,)
    except Exception as e:
        return Response({"message": f"An error occurred: {str(e)}"},status=status.HTTP_400_BAD_REQUEST,)

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def get_doctors_api(request):
    try:
        # Parse the JSON payload
        payload = json.loads(request.body) if request.body else {}

        # Extract parameters from JSON

        speciality_id = payload.get('speciality_id')
        hospital_id = payload.get('hospital_id')
        is_recommended = payload.get('is_recommended')
        clinic_category_id = payload.get('clinic_category_id')

        # Base queryset
        doctors = account_models.DoctorDetails.objects.prefetch_related('specialist').filter(status=1)

        # Apply filters dynamically
        if is_recommended is not None:
            doctors = doctors.filter(is_recommended=is_recommended)
        if speciality_id:
            doctors = doctors.filter(specialist_id=speciality_id)
        if hospital_id:
            doctors = doctors.filter(hospital_id=hospital_id)
        if clinic_category_id:
            doctors = doctors.filter(hospital__clinic_category_id=clinic_category_id)

        # Serialize data
        serializer = API_serializers.DoctorSerializer(doctors, many=True, context={'request': request})

        # Return response
        return Response({
            "result": serializer.data,
            "total": doctors.count(),
            "message": "Success",
            "status": 1
        }, status=status.HTTP_200_OK)

    except json.JSONDecodeError:
        return Response({
            "message": "Invalid JSON payload.",
            "status": 0
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logger.error(f"Error fetching doctor data: {e}")
        return Response({
            "message": "An error occurred while fetching doctor data.",
            "status": 0
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def get_doctors_details(request):
    try:
        payload = json.loads(request.body) if request.body else {}
        dr_id = payload.get('doctor_id')
        if not dr_id:
            return Response({ "message": "doctor_id is required.", "status": 0 }, status=status.HTTP_400_BAD_REQUEST)

        doctor = account_models.DoctorDetails.objects.prefetch_related('specialist').get(id=dr_id)
        serializer = API_serializers.DoctorDetailsSerializer(doctor, context={'request': request})
        # Return the doctor data
        return Response({
            "result": serializer.data,
            "message": "Success",
            "status": 1
        }, status=status.HTTP_200_OK)

    except account_models.DoctorDetails.DoesNotExist:
        return Response({
            "result": None,
            "message": "Doctor not found.",
            "status": 0
        }, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({
            "message": "An error occurred while fetching doctor details.",
            "status": 0
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def getClinicCategories(request):
    # Query all clinic categories
    categories = admin_models.ClinicCategory.objects.filter(status=1)
    serializer = API_serializers.ClinicCategorySerializer(categories, many=True)
    
    # Return serialized data
    return Response({
        "result": serializer.data,
        "message": "Success",
        "status": 1
    }, status=200)
    



'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''
@api_view(['GET'])  # Change to POST for body data
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def getHospitalDoctors(request):
    hospital_id = request.data.get("hospital_id")
    
    if not hospital_id:
        return Response({"message": "Hospital ID is required."}, status=400)

    # Fetch the hospital and validate its existence
    try:
        hospital = account_models.Hospital.objects.get(id=hospital_id)
    except account_models.Hospital.DoesNotExist:
        return Response({"message": "Hospital not found."}, status=404)

    # Fetch doctors linked to the hospital
    hospital_doctors = admin_models.HospitalDoctors.objects.filter(hospital_id=hospital_id, status=1).select_related('doctor')
    doctors = [hd.doctor for hd in hospital_doctors if hd.doctor]

    # Serialize doctor details
    serializer = API_serializers.HospitalDoctorDetailsSerializer(doctors, many=True)
    
    return Response({
        "hospital": {
            "id": hospital.id,
            "name": hospital.hospital_name,
            "address": hospital.address,
            "phone": hospital.phone_number,
            "email": hospital.user.email,
            "hospital_doctors": serializer.data,
        },
        
        "message": "Success",
        "status": 1
    }, status=200)


'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def getExpertTalk(request):
    expert_talks = admin_models.ExpertTalk.objects.select_related('doctor').all()
    serializer = API_serializers.ExpertTalkSerializer(expert_talks, many=True, context={'request': request})
    return Response({
        "result": serializer.data,
        "message": "Success",
        "status": 1
    }, status=200)

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def getDoctorclinics(request):
    try:
        doctor_id = request.data.get("doctor_id")
        # Validate the input
        if not doctor_id:
            return JsonResponse({"message": "Doctor ID is required", "status": 0}, status=400)

        # Fetch the doctor
        try:
            doctor = account_models.DoctorDetails.objects.get(id=doctor_id)
        except account_models.DoctorDetails.DoesNotExist:
            return JsonResponse({"message": "Doctor not found", "status": 0}, status=404)

        # Fetch clinics for the doctor
        clinics = admin_models.DoctorClinics.objects.filter(doctor=doctor)

        # Build the response
        result = [
            {
                "id": clinic.id,
                "doctor_id": doctor.id,
                "clinic_name": clinic.clinic_name,
                "phone": clinic.phone,
                "email": clinic.email,
                "address": clinic.address,
                "latitude": clinic.latitude,
                "longitude": clinic.longitude,
                "start_time": str(clinic.start_time),
                "end_time": str(clinic.end_time),
            }
            for clinic in clinics
        ]

        # Return the response
        return JsonResponse({"result": result, "message": "Success", "status": 1}, status=200)

    except json.JSONDecodeError:
        return JsonResponse({"message": "Invalid JSON input", "status": 0}, status=400)
    except Exception as e:
        return JsonResponse({"message": "An error occurred", "status": 0, "error": str(e)}, status=500)


'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def getClinicTimeSlots(request):
    try:
        clinic_id = request.data.get("clinic_id")
        booking_date = request.data.get("booking_date")
        print(request.data)

         # If no booking_date is provided, use today's date
        if not booking_date:
            booking_date = datetime.now().strftime("%Y-%m-%d")

        # Validate input
        if not clinic_id:
            return JsonResponse({"message": "Clinic ID is require", "status": 0}, status=400)
        

        # Fetch the clinic details
        clinic = admin_models.DoctorClinics.objects.filter(id=clinic_id, status=1).first()
        if not clinic:
            return JsonResponse({"message": "Clinic not found", "status": 0}, status=404)

        # Prepare response
        result = {
            "id": clinic.id,
            "doctor_id": clinic.doctor.id,
            "clinic_name": clinic.clinic_name,
            "phone": clinic.phone,
            "email": clinic.email,
            "address": clinic.address,
            "start_time": str(clinic.start_time),
            "end_time": str(clinic.end_time),
        }

        # Generate time slots
        start_time = datetime.combine(datetime.strptime(booking_date, "%Y-%m-%d").date(), clinic.start_time)
        end_time = datetime.combine(datetime.strptime(booking_date, "%Y-%m-%d").date(), clinic.end_time)
        consultation_minutes = int(clinic.consultation_minutes)
        time_slots = []

        while start_time <= end_time:
            slot_time = start_time.strftime("%H:%M")
            time_slots.append({"slot_time": slot_time, "isAvailable": True})
            start_time += timedelta(minutes=consultation_minutes)

        result["time_slots"] = time_slots

        return JsonResponse({"result": result, "message": "Success", "status": 1}, status=200)

    except Exception as e:
        return JsonResponse({"message": f"Error: {str(e)}", "status": 0}, status=500)



'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def getDoctorBanners(request):
    try:
        doctor_id = request.GET.get("doctor_id")
        position = request.GET.get("position")
        if not doctor_id or not position:
            return Response({"message": "Invalid input data. 'doctor_id' and 'position' are required.", "status": 0}, status=status.HTTP_400_BAD_REQUEST)

        if position not in ['T', 'B']:
            return Response({"message": "Invalid position value, it should be 'T' or 'B'.", "status": 0}, status=status.HTTP_400_BAD_REQUEST)

        try:
            doctor = account_models.DoctorDetails.objects.get(id=doctor_id)
        except ObjectDoesNotExist:
            return Response({"message": "Doctor not found", "status": 0}, status=status.HTTP_404_NOT_FOUND)

        banners = admin_models.DoctorBanner.objects.filter(doctor=doctor, position=position, status=1)
        if not banners.exists():
            return Response({"message": "No banners found for the given doctor and position", "status": 0}, status=status.HTTP_404_NOT_FOUND)
        serializer = API_serializers.DoctorBannerSerializer(banners, many=True, context={'request': request})
        return Response({"result": serializer.data, "message": "Success", "status": 1}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": f"Error: {str(e)}", "status": 0}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def getHomeBanners(request):
    try:
        app_module_id = 2
        position = 'top'
        if not app_module_id or not position:
            return Response({"message": "Invalid input data. 'app_module_id' and 'position' are required.", "status": 0},status=status.HTTP_400_BAD_REQUEST)
        if position not in ['top', 'bottom']:
            return Response({"message": "Invalid position value. It must be 'top' or 'bottom'.", "status": 0},status=status.HTTP_400_BAD_REQUEST)
        try:
            app_module = admin_models.AppModule.objects.get(id=app_module_id)
        except admin_models.AppModule.DoesNotExist:
            return Response({"message": "App module not found.", "status": 0}, status=status.HTTP_404_NOT_FOUND)
        banners = admin_models.Banner.objects.filter(app_module=app_module, position=position, status=1)
        if not banners.exists():
            return Response({"message": "No banners found for the given app module and position.", "status": 0}, status=status.HTTP_404_NOT_FOUND)
        serializer = API_serializers.BannerSerializer(banners, many=True, context={'request': request})
        return Response({"result": serializer.data, "message": "Success", "status": 1}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": f"Error: {str(e)}", "status": 0}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

# Function to calculate distance using the Haversine formula
def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of Earth in kilometers
    return c * r

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def getRecommendedHospitals(request):
    try:
        latitude = request.GET.get('lat')
        longitude = request.GET.get('lng')
        radius = float(request.GET.get('radius', 10))  # Radius in kilometers (default 10km)
        if not latitude or not longitude:
            return Response(
                {
                    "message": "Latitude and longitude are required.", 
                    "status": 0
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        latitude = float(latitude)
        longitude = float(longitude)
        hospitals = account_models.Hospital.objects.filter(is_recommended=1, status=1)
        nearby_hospitals = []
        for hospital in hospitals:
            if hospital.latitude and hospital.longitude:
                distance = haversine(latitude, longitude, float(hospital.latitude), float(hospital.longitude))
                if distance <= radius:
                    nearby_hospitals.append(hospital)
        serializer = API_serializers.RecommentedHospitalSerializer(nearby_hospitals, many=True, context={'request': request})
        return Response({"result": serializer.data, "message": "Success", "status": 1}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": f"Error: {str(e)}", "status": 0}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def getBlogs(request):
    try:
        active_blogs = admin_models.Blog.objects.filter(status=1).order_by('-created_at')
        if not active_blogs.exists():
            return Response(
                {
                    "success": False,
                    "message": "No blogs found.",
                    "result": [],
                    "total": 0,
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = API_serializers.BlogSerializer(active_blogs, many=True, context={'request': request})
        response_data = {
            "success": True,
            "message": "Blogs retrieved successfully",
            "result": serializer.data,
            "total": len(serializer.data),
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {
                "success": False,
                "message": f"An error occurred: {str(e)}",
                "result": [],
                "total": 0,
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def getBlogDetails(request, id):
    try:
        blog = admin_models.Blog.objects.filter(id=id, status=1).first()
        if not blog:
            return Response( { "success": False, "message": "Blog not found or inactive.", "result": None, }, status=status.HTTP_404_NOT_FOUND, )
        serializer = API_serializers.BlogSerializer(blog, context={'request': request})
        return Response(
            {
                "success": True,
                "message": "Blog retrieved successfully.",
                "result": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
    except Exception as e:
        return Response( { "success": False,  "message": f"An error occurred: {str(e)}", "result": None, }, status=status.HTTP_500_INTERNAL_SERVER_ERROR, )

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def getServices(request):
    try:
        active_services = admin_models.Service.objects.filter(status=1).order_by('created_at')
        if not active_services.exists():
            return Response(
                { "success": False, "message": "No active services found.", "result": [], "total": 0, },
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = API_serializers.ServiceSerializer(active_services, many=True, context={'request': request})
        return Response(
            {
                "success": True,
                "message": "Services retrieved successfully.",
                "result": serializer.data,
                "total": len(serializer.data),
            },
            status=status.HTTP_200_OK,
        )
    except Exception as e:
        return Response(
            {
                "success": False,
                "message": f"An error occurred: {str(e)}",
                "result": None,
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def sendQuery(request):
    # Extract data from the request
    name = request.data.get('name')
    email = request.data.get('email')
    message = request.data.get('message')
    customer_id = request.data.get('customer_id')

    # Validate required fields
    if not name or not email or not message:
        return Response(
            {
                "success": False,
                "message": "Name, email, and message are required.",
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Validate email format
    if not email.endswith('@gmail.com'):
        return Response(
            {
                "success": False,
                "message": "Email must be from @gmail.com.",
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Validate message length
    if len(message) < 10:
        return Response(
            {
                "success": False,
                "message": "The message must be at least 10 characters long.",
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    # Validate customer ID
    if customer_id:
        try:
            customer = account_models.Customer.objects.get(id=customer_id)
        except account_models.Customer.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": "Customer with this ID does not exist.",
                },
                status=status.HTTP_400_BAD_REQUEST
            )
    else:
        customer = None

    # Create the HelpDeskQuery record
    try:
        query = admin_models.HelpDeskQuery.objects.create(name=name, email=email, message=message, customer=customer)
        return Response(
            {
                "success": True,
                "message": "Query created successfully",
                "data": {
                    "name": query.name,
                    "email": query.email,
                    "message": query.message,
                    "customer": query.customer.id if query.customer else None,
                },
            },
            status=status.HTTP_201_CREATED
        )
    except ValidationError as e:
        return Response(
            {
                "success": False,
                "message": f"Validation error: {str(e)}",
            },
            status=status.HTTP_400_BAD_REQUEST
        )

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def getReminderCategories(request):
    # Fetch all categories from the database
    categories = admin_models.ReminderCategory.objects.filter(status=1).values('id', 'name')
    
    # Format the response
    response_data = {
        "message": "Success",
        "status": 1,
        "result": list(categories)  # Convert QuerySet to a list of dictionaries
    }
    
    return Response(response_data, status=200)

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def getReminders(request):
    customer_id = request.GET.get('customer_id')  # Retrieve customer_id from query params

    if not customer_id:
        return Response({"message": "Customer ID is required.","status": 0}, status=400)
    
    try:
        
        reminders = admin_models.Reminder.objects.filter(customer_id=customer_id)
        if reminders.exists():
            serialized_reminders = API_serializers.ReminderSerializer(reminders, many=True).data
            return Response({
                "message": "Success",
                "status": 1,
                "result": serialized_reminders
            }, status=200)
        else:
            return Response({
                "message": "No reminders found for this customer.",
                "status": 1,
                "result": []
            }, status=200)
    except Exception as e:
        return Response({
            "message": f"Error occurred: {str(e)}",
            "status": 0
        }, status=500)


'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def get_counts(request):
    try:
        users_count = account_models.User.objects.filter(user_type='customer').count()
        doctors_count = account_models.User.objects.filter(user_type='doctor').count()
        hospitals_count = account_models.User.objects.filter(user_type='hospital').count()
        labs_count = account_models.User.objects.filter(user_type='lab').count()

        data = {
            "users": users_count,
            "doctors": doctors_count,
            "hospitals": hospitals_count,
            "labs": labs_count,
        }

        response = {
            "result": data,
            "message": "Success",
            "status": 1,
        }
        return JsonResponse(response, status=200)

    except Exception as e:
        return JsonResponse({
            "message": f"An error occurred: {str(e)}",
            "status": 0,
        }, status=500)


'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def getAllergies(request):
    try:
        active_allergies = admin_models.Allergy.objects.filter(status=1).order_by('-created_at')
        if not active_allergies.exists():
            return Response(
                {
                    "success": False,
                    "message": "No allergies found.",
                    "result": [],
                    "total": 0,
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = API_serializers.AllergySerializer(active_allergies, many=True, context={'request': request})
        response_data = {
            "success": True,
            "message": "Allergies retrieved successfully",
            "result": serializer.data,
            "total": len(serializer.data),
        }
        return Response(response_data, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response(
            {
                "success": False,
                "message": f"An error occurred: {str(e)}",
                "result": [],
                "total": 0,
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def getMedications(request):
    try:
        active_medications = admin_models.Medication.objects.filter(status=1).order_by('-created_at')
        if not active_medications.exists():
            return Response(
                {
                    "success": False,
                    "message": "No active medications found.",
                    "result": [],
                    "total": 0,
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        
        # Serialize the data
        serializer = API_serializers.MedicationSerializer(active_medications, many=True, context={'request': request})
        
        response_data = {
            "success": True,
            "message": "Active medications retrieved successfully",
            "result": serializer.data,
            "total": len(serializer.data),
        }
        
        return Response(response_data, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response(
            {
                "success": False,
                "message": f"An error occurred: {str(e)}",
                "result": [],
                "total": 0,
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def getHelpDeskQueryDetails(request):
    try:
        customer_id = request.GET.get('customer_id')
        query_id = request.GET.get('query_id')
        help_desk_query = admin_models.HelpDeskQuery.objects.filter(customer_id=customer_id, id=query_id).first()
        if not help_desk_query:
            return Response(
                {
                    "success": False,
                    "message": "No help desk query found with the provided customer ID and query ID.",
                    "result": None,
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = API_serializers.HelpDeskQuerySerializer(help_desk_query, context={'request': request})
        
        response_data = {
            "success": True,
            "message": "Help desk query details retrieved successfully.",
            "result": serializer.data,
        }
        
        return Response(response_data, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response(
            {
                "success": False,
                "message": f"An error occurred: {str(e)}",
                "result": None,
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def addReminder(request):
    try:
        user = request.user
        customer = getattr(user, "customer_profile", None)
        if not customer:
            return Response(
                {
                    "message": "Customer profile not found for the authenticated user.",
                    "status": 0,
                    "result": None,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        # Parse input data
        data = request.data
        category_id = data.get("category_id")
        title = data.get("title")
        description = data.get("description")
        reminder_date = data.get("reminder_date")

        # Validate required fields
        if not (category_id and title and reminder_date):
            return Response(
                {
                    "message": "Missing required fields: category_id, title, or reminder_date.",
                    "status": 0,
                    "result": None,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Validate the category
        category = admin_models.ReminderCategory.objects.filter(id=category_id, status=1).first()
        if not category:
            return Response(
                {
                    "message": "Invalid category ID or category is inactive.",
                    "status": 0,
                    "result": None,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Create the reminder
        reminder = admin_models.Reminder.objects.create(
            customer=customer,
            category=category,
            title=title,
            description=description,
            reminder_date=datetime.strptime(reminder_date, "%Y-%m-%d"),
        )

        # Prepare response data
        result = {
            "id": reminder.id,
            "customer_id": reminder.customer.id,
            "category_id": reminder.category.id,
            "title": reminder.title,
            "description": reminder.description,
            "reminder_date": reminder.reminder_date.isoformat(),
            "created_at": reminder.created_at.isoformat(),
            "updated_at": reminder.updated_at.isoformat(),
        }

        return Response(
            {
                "message": "Reminder added successfully",
                "status": 1,
                "result": result,
            },
            status=status.HTTP_201_CREATED,
        )

    except Exception as e:
        return Response(
            {
                "message": f"An error occurred: {str(e)}",
                "status": 0,
                "result": None,
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def addFeedback(request):
    try:
        user = request.user
        customer = getattr(user, 'customer_profile', None)

        if not customer:
            return Response(
                {
                    "message": "User is not associated with a customer profile.",
                    "status": 0,
                    "feedback": None
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # Parse request data
        data = request.data
        hospital_id = data.get("hospital_id")
        doctor_id = data.get("doctor_id")
        feedback_text = data.get("feedback")
        rating = data.get("rating")

        # Validate required fields
        if not (hospital_id or doctor_id):
            return Response(
                {
                    "message": "Either hospital_id or doctor_id is required.",
                    "status": 0,
                    "feedback": None
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        if not feedback_text or rating is None:
            return Response(
                {
                    "message": "Feedback text and rating are required.",
                    "status": 0,
                    "feedback": None
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # Fetch related objects
        hospital = account_models.Hospital.objects.filter(id=hospital_id).first() if hospital_id else None
        doctor = account_models.DoctorDetails.objects.filter(id=doctor_id).first() if doctor_id else None

        if hospital_id and not hospital:
            return Response(
                {
                    "message": "Invalid hospital ID.",
                    "status": 0,
                    "feedback": None
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if doctor_id and not doctor:
            return Response(
                {
                    "message": "Invalid doctor ID.",
                    "status": 0,
                    "feedback": None
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create feedback
        feedback = admin_models.Feedback.objects.create(
            customer=customer,
            doctor=doctor,
            hospital=hospital,
            feedback=feedback_text,
            rating=rating
        )

        # Prepare response
        response_data = {
            "customer_id": customer.id,
            "hospital_id": hospital.id if hospital else None,
            "doctor_id": doctor.id if doctor else None,
            "feedback": feedback.feedback,
            "rating": feedback.rating,
            "admin_approved": feedback.admin_approved,
            "updated_at": feedback.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            "created_at": feedback.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            "id": feedback.id,
            "date": feedback.created_at.strftime("%d-%b-%y, %I:%M %p")
        }

        return Response(
            {
                "message": "Feedback added successfully",
                "status": 1,
                "feedback": response_data
            },
            status=status.HTTP_201_CREATED
        )

    except Exception as e:
        return Response(
            {
                "message": f"An error occurred: {str(e)}",
                "status": 0,
                "feedback": None
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def updateProfile(request):
    try:
        user = request.user
        customer = getattr(user, 'customer_profile', None)
        if not customer:
            return Response({"message": "User is not associated with a customer profile.","status": 0,"result": None},status=status.HTTP_400_BAD_REQUEST)

        data = request.data

        serializer = API_serializers.CustomerProfileSerializer( customer, data=data, partial=True, context={"request": request} )
        if serializer.is_valid():
            updated_customer = serializer.save()
            user.updated_at = models.DateTimeField(auto_now=True)
            user.email = data['email']
            user.username = data['email']
            user.save()

            # Prepare response data
            response_data = {
                "id": updated_customer.id,
                "customer_name": updated_customer.customer_name,
                "phone_number": updated_customer.phone_number,
                "email": updated_customer.user.email,
                "profile_picture": updated_customer.profile_picture.url if updated_customer.profile_picture else None,
                "pre_existing_disease": updated_customer.pre_existing_disease,
                "blood_group": updated_customer.blood_group,
                "gender": updated_customer.gender,
                "wallet": updated_customer.wallet,
                "overall_ratings": updated_customer.overall_ratings,
                "no_of_ratings": updated_customer.no_of_ratings,
                "status": updated_customer.status,
                "dob": updated_customer.dob,
                "age": updated_customer.age,
                "height": updated_customer.height,
                "weight": updated_customer.weight,
                "emergency_contact_no": updated_customer.emergency_contact_no,
                "allergies": updated_customer.allergies,
                "current_medications": updated_customer.current_medications,
                "created_at": updated_customer.user.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                "updated_at": updated_customer.user.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            }

            return Response( { "message": "Profile updated successfully", "status": 1, "result": response_data }, status=status.HTTP_200_OK )
        else:
            return Response( { "message": "Validation error", "status": 0, "result": None, "errors": serializer.errors }, status=status.HTTP_400_BAD_REQUEST )

    except Exception as e:
        return Response( { "message": f"An error occurred: {str(e)}", "status": 0, "result": None }, status=status.HTTP_500_INTERNAL_SERVER_ERROR )

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def mark_As_Done_Reminder(request):
    try:
        reminder_id = request.data.get('reminder_id')

        if not reminder_id:
            return Response({"message": "Reminder ID is required.","status": 0,"result": None}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch the reminder object
        reminder = admin_models.Reminder.objects.filter(id=reminder_id).first()

        if not reminder:
            return Response({
                "message": "Reminder not found.",
                "status": 0,
                "result": None
            }, status=status.HTTP_404_NOT_FOUND)

        # Mark the reminder as done by updating its status
        reminder.status = 1 
        reminder.save()

        # Serialize the reminder data for the response
        serializer = API_serializers.markAs_Read_ReminderSerializer(reminder)

        return Response({
            "message": "Reminder marked as done successfully",
            "status": 1,
            "result": serializer.data
        }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({
            "message": f"An error occurred: {str(e)}",
            "status": 0,
            "result": None
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def getTopCities(request):
    try:
        top_cities = account_models.Hospital.objects.values('city').annotate(hospital_count=Count('id')).order_by('-hospital_count')
        # Format the results to return city and hospital count
        result = [{'city': city['city'], 'hospital_count': city['hospital_count']} for city in top_cities]
        return Response({'result': result,'message': 'Success','status': 1}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': f"An error occurred: {str(e)}",'status': 0,'result': None}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def addCustomerInsurance(request):
    customer_id = request.data.get('customer_id')
    customer = get_object_or_404(account_models.Customer, id=customer_id)

    serializer = API_serializers.CustomerInsuranceSerializer(data=request.data)
    if serializer.is_valid():
        insurance = serializer.save(customer=customer)

        response_data = {
            "message": "Customer insurance added successfully",
            "status": 1,
            "result": {
                "customer_id": customer.id,
                "insurance_company_id": insurance.insurance_company_id,
                "insurance_company_name": insurance.insurance_company_name,
                "insurance_type": insurance.insurance_type,
                "start_date": insurance.start_date,
                "end_date": insurance.end_date,
                "updated_at": insurance.updated_at,
                "created_at": insurance.created_at,
                "id": insurance.id
            }
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_Customer_Insurance(request):
    customer_id = request.data.get('customer_id')
    insurance_id = request.data.get('insurance_id')

    if not customer_id or not insurance_id:
        return Response({"error": "Both customer_id and insurance_id are required."}, status=status.HTTP_400_BAD_REQUEST)
    customer = get_object_or_404(account_models.Customer, id=customer_id)
    try:
        insurance = admin_models.CustomerInsurance.objects.get(id=insurance_id, customer=customer)
    except admin_models.CustomerInsurance.DoesNotExist:
        return Response({"error": "Insurance record not found for the given customer."}, status=status.HTTP_404_NOT_FOUND)

    insurance.delete()
    return Response({
        "message": "Customer insurance deleted successfully",
        "status": 1,
    }, status=status.HTTP_200_OK)


'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def getCustomerInsurance(request):
    try:
        user = request.user
        customer = getattr(user, 'customer_profile', None)
        customer_id= customer.id
        
        # Validate if the user has a customer profile
        if not customer_id:
            return Response({
                "message": "User is not associated with a customer profile.",
                "status": 0,
                "result": None
            }, status=status.HTTP_400_BAD_REQUEST)

        # Retrieve customer insurances
        insurances = admin_models.CustomerInsurance.objects.filter(customer=customer_id).order_by('-created_at')

        # Format the response data
        insurance_list = [
            {
                "id": insurance.id,
                "customer_id": insurance.customer.id,
                "insurance_company_id": insurance.insurance_company_id,
                "insurance_company_name": insurance.insurance_company_name,
                "insurance_type": insurance.insurance_type,
                "start_date": insurance.start_date.isoformat(),
                "end_date": insurance.end_date.isoformat(),
                "created_at": insurance.created_at.isoformat(),
                "updated_at": insurance.updated_at.isoformat(),
            }
            for insurance in insurances
        ]

        return Response({
            "message": "Customer insurance records retrieved successfully",
            "status": 1,
            "result": insurance_list
        }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({
            "message": f"An error occurred: {str(e)}",
            "status": 0,
            "result": None
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def updateReminder(request):
    try:
        data = request.data
        reminder_id = data.get("reminder_id")
        category_id = data.get("category_id")
        title = data.get("title")
        description = data.get("description")
        reminder_date = data.get("reminder_date")
        
        if not reminder_id or not title or not reminder_date:
            return Response({ "message": "Missing required fields: reminder_id, title, or reminder_date.","status": 0,"result": None}, status=status.HTTP_400_BAD_REQUEST)

        try:
            reminder = admin_models.Reminder.objects.get(id=reminder_id)
        except admin_models.Reminder.DoesNotExist:
            return Response({"message": "Reminder not found.","status": 0,"result": None}, status=status.HTTP_404_NOT_FOUND)

        
        reminder.category_id = category_id
        reminder.title = title
        reminder.description = description
        reminder.reminder_date = reminder_date
        reminder.updated_at = datetime.now()
        reminder.save()

        # Prepare the response data
        result = {
            "id": reminder.id,
            "customer_id": reminder.customer.id,
            "category_id": reminder.category_id,
            "title": reminder.title,
            "description": reminder.description,
            "reminder_date": reminder.reminder_date,
            "status": reminder.status,
            "created_at": reminder.created_at,
            "updated_at": reminder.updated_at
        }
        return Response({ "message": "Reminder updated successfully", "status": 1, "result": result }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({ "message": f"An error occurred: {str(e)}", "status": 0, "result": None }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def deleteReminder(request):
    try:
        data = request.data
        reminder_id = data.get("reminder_id")
        if not reminder_id:
            return Response({ "message": "Missing required field: reminder_id.", "status": 0 }, status=status.HTTP_400_BAD_REQUEST)
        try:
            reminder = admin_models.Reminder.objects.get(id=reminder_id)
        except admin_models.Reminder.DoesNotExist:
            return Response({ "message": "Reminder not found.", "status": 0 }, status=status.HTTP_404_NOT_FOUND)
        reminder.delete()
        return Response({
            "message": "Reminder deleted successfully",
            "status": 1
        }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({ "message": f"An error occurred: {str(e)}", "status": 0 }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def familyMemberAdd(request):
    try:
        customer = request.user.customer_profile 
        data = request.data
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        mobile_no = data.get('mobile_no')
        email = data.get('email')
        relation = data.get('relation')
        dob = data.get('dob')
        blood_group = data.get('blood_group')
        is_minor = bool(data.get('is_minor', 0))  # Convert to boolean
        gender = data.get('gender')
        medical_history = data.get('medical_history', '')

        # Validate mandatory fields
        if not first_name or not mobile_no or not relation:
            return Response(
                {"message": "First name, mobile number, and relation are required fields.", "status": 0}, status=status.HTTP_404_NOT_FOUND
            )

        # Create FamilyMember instance
        family_member = admin_models.FamilyMember.objects.create(
            customer=customer, first_name=first_name, last_name=last_name,
            mobile_no=mobile_no, email=email, relation=relation,
            dob=dob, blood_group=blood_group, is_minor=is_minor,
            gender=gender, medical_history=medical_history,
        )

        return Response( {"message": "Member added successfully", "status": 1}, status=status.HTTP_201_CREATED )
    except Exception as e:
        return Response( {"message": f"An error occurred: {str(e)}", "status": 0}, status=status.HTTP_404_NOT_FOUND )

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def familyMemberUpdate(request):
    try:
        data = request.data
        member_id = data.get('member_id')
        try:
            family_member = admin_models.FamilyMember.objects.get(id=member_id)
        except admin_models.FamilyMember.DoesNotExist:
            return Response( {"message": "Family member not found with the provided member ID.", "status": 0}, status=status.HTTP_400_BAD_REQUEST )

        # Update the fields with the provided data
        family_member.first_name = data.get('first_name', family_member.first_name)
        family_member.last_name = data.get('last_name', family_member.last_name)
        family_member.mobile_no = data.get('mobile_no', family_member.mobile_no)
        family_member.email = data.get('email', family_member.email)
        family_member.relation = data.get('relation', family_member.relation)
        family_member.dob = data.get('dob', family_member.dob)
        family_member.blood_group = data.get('blood_group', family_member.blood_group)
        family_member.is_minor = bool(data.get('is_minor', family_member.is_minor))
        family_member.gender = data.get('gender', family_member.gender)
        family_member.medical_history = data.get('medical_history', family_member.medical_history)

        # Save the updated instance
        family_member.save()

        # Prepare the response data
        updated_data = {
            "member_id": family_member.id,
            "first_name": family_member.first_name,
            "last_name": family_member.last_name,
            "mobile_no": family_member.mobile_no,
            "email": family_member.email,
            "relation": family_member.relation,
            "dob": family_member.dob,
            "blood_group": family_member.blood_group,
            "is_minor": family_member.is_minor,
            "gender": family_member.gender,
            "medical_history": family_member.medical_history,
        }

        return Response(
            {"message": "Family member updated successfully", "status": 1, "updated_data": updated_data}, status=status.HTTP_200_OK )
    except Exception as e:
        return Response( {"message": f"An error occurred: {str(e)}", "status": 0}, status=status.HTTP_400_BAD_REQUEST )


'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def familyMemberDelete(request):
    try:
        member_id = request.data.get('member_id')
        if not member_id:
            return Response( {"message": "Member ID is required.", "status": 0}, status=status.HTTP_400_BAD_REQUEST )
        try:
            family_member = admin_models.FamilyMember.objects.get(id=member_id)
        except admin_models.FamilyMember.DoesNotExist:
            return Response( {"message": "Family member not found.", "status": 0}, status=status.HTTP_400_BAD_REQUEST )
        family_member.delete()
        return Response( {"message": "Family member deleted successfully.", "status": 1}, status=status.HTTP_200_OK )
    except Exception as e:
        return Response( {"message": f"An error occurred: {str(e)}", "status": 0}, status=status.HTTP_400_BAD_REQUEST )



'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def familyMemberLists(request):
    try:
        user = request.user
        if not hasattr(user, 'customer_profile'):
            return Response( {"message": "Only customers can view family member lists.", "status": 0}, status=400 )
        family_members = admin_models.FamilyMember.objects.filter(customer_id=user.customer_profile.id)
        serialized_data = API_serializers.FamilyMemberSerializer(family_members, many=True).data
        return Response( {"message": "Family members fetched successfully.", "status": 1, "result": serialized_data}, status=200 )
    except Exception as e:
        return Response( {"message": f"An error occurred: {str(e)}", "status": 0}, status=400 )

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def fetchFamilyMemberDetails(request, member_id):
    try:
        user = request.user
        if not hasattr(user, 'customer_profile'):
            return Response( {"message": "Only customers can fetch family member details.", "status": 0}, status=400 )
        family_member = admin_models.FamilyMember.objects.filter( customer_id=user.customer_profile.id, id=member_id ).first()
        if not family_member:
            return Response( {"message": "Family member not found or does not belong to this user.", "status": 0}, status=404 )
        serialized_data = API_serializers.FamilyMemberSerializer(family_member).data
        return Response( {"message": "Family member details fetched successfully.", "status": 1, "result": serialized_data}, status=200 )
    except Exception as e:
        return Response( {"message": f"An error occurred: {str(e)}", "status": 0}, status=400 )

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def labLists(request):
    try:
        labs = account_models.Laboratory.objects.filter(status=1)
        serialized_data = API_serializers.LaboratorySerializer(labs, many=True).data
        return Response(
            {
                "result": serialized_data,
                "count": labs.count(),
                "message": "Success",
                "status": 1,
            },
            status=200,
        )
    except Exception as e:
        return Response(
            {
                "message": f"An error occurred: {str(e)}",
                "status": 0,
            },
            status=400,
        )
    

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def labServicesList(request):
    try:
        lab_services = admin_models.LabService.objects.filter(status=1).select_related('service', 'laboratory')
        result = [
            {
                "id": lab_service.id,
                "name": lab_service.service.service_name,
                "display_name": lab_service.service.service_name,
            }
            for lab_service in lab_services
        ]
        return Response( { "result": result, "count": len(result), "message": "Success", "status": 1, }, status=200, )
    except Exception as e:
        return Response( { "message": f"An error occurred: {str(e)}", "status": 0, }, status=400, )


'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''
@api_view(['GET'])
@permission_classes([IsAuthenticated])  
@authentication_classes([JWTAuthentication])
def labBookingTimeSlot(request):
    start_time = datetime.strptime("00:00", "%H:%M")
    end_time = datetime.strptime("23:00", "%H:%M")
    time_slots = []

    while start_time <= end_time:
        time_slots.append({ "slot_time": start_time.strftime("%H:%M"), })
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
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def labDetails(request):
    try:
        lab_id = request.GET.get('lab_id')
        if lab_id:
            lab = account_models.Laboratory.objects.filter(id=lab_id, status=1).first()
            if not lab:
                return Response({"message": "Lab not found or inactive.", "status": 0}, status=404)
            data = API_serializers.LaboratoryDetailsSerializer(lab, context={'request': request}).data
        else:
            labs = account_models.Laboratory.objects.filter(status=1)
            data = API_serializers.LaboratoryDetailsSerializer(labs, many=True, context={'request': request}).data

        return Response({"result": data, "message": "Success", "status": 1}, status=200)
    except Exception as e:
        return Response({"message": f"An error occurred: {str(e)}", "status": 0}, status=400)


'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def labPackages(request):
    lab_packages = admin_models.LabPackage.objects.filter(status=1)
    serializer = API_serializers.LabPackageSerializer( lab_packages, many=True, context={'request': request})
    response_data = {"result": serializer.data,"count": len(serializer.data),"message": "Success","status": 1}
    return Response(response_data, status=status.HTTP_200_OK)

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def labPackageDetails(request):
    try:
        package_id = request.GET.get('package_id')
        lab_package = admin_models.LabPackage.objects.get(id=package_id)
        serializer = API_serializers.LabPackageDetailsSerializer(lab_package, context={'request': request})
        return Response({ "result": serializer.data,"message": "Success", "status": 1}, status=status.HTTP_200_OK)
    except admin_models.LabPackage.DoesNotExist:
        return Response({ "result": None, "message": "Lab Package not found", "status": 0}, status=status.HTTP_404_NOT_FOUND)

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def addAddress(request):
    try:
        data = request.data
        customer_id = data.get('customer_id')
        try:
            customer = account_models.Customer.objects.get(id=customer_id)
        except account_models.Customer.DoesNotExist:
            return Response(
                {"message": "Customer not found with the provided customer ID.", "status": 0}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Extract and validate address details
        address = data.get('address')
        landmark = data.get('landmark')
        lat = data.get('lat')
        lng = data.get('lng')
        status_value = data.get('status', 1)  # Default status is 1 (Active)

        if not all([address, landmark, lat, lng]):
            return Response(
                {"message": "All fields (address, landmark, lat, lng) are required.", "status": 0}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Create a new address
        new_address = admin_models.Address.objects.create(customer=customer,address=address,landmark=landmark,lat=lat,lng=lng,status=status_value,created_at=datetime.now(),updated_at=datetime.now())
        response_data = {
            "id": new_address.id,"customer_id": customer.id,"address": new_address.address,
            "landmark": new_address.landmark,"lat": new_address.lat,"lng": new_address.lng,
            "status": new_address.status,"created_at": new_address.created_at,"updated_at": new_address.updated_at,
        }

        return Response(
            {"message": "Address added successfully.", "status": 1, "data": response_data}, 
            status=status.HTTP_201_CREATED
        )
    except Exception as e:
        return Response(
            {"message": f"An error occurred: {str(e)}", "status": 0}, 
            status=status.HTTP_400_BAD_REQUEST
        )

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def updateAddress(request):
    try:
        # Extract data from request
        data = request.data
        address_id = data.get('id')
        customer_id = data.get('customer_id')
        address = data.get('address')
        landmark = data.get('landmark')
        lat = data.get('lat')
        lng = data.get('lng')
        if not all([address_id, customer_id, address, landmark, lat, lng]):
            return Response({"message": "All fields (id, customer_id, address, landmark, lat, lng) are required.", "status": 0},status=status.HTTP_400_BAD_REQUEST)
        try:
            customer = account_models.Customer.objects.get(id=customer_id)
        except account_models.Customer.DoesNotExist:
            return Response({"message": "Customer not found with the provided customer ID.", "status": 0},status=status.HTTP_400_BAD_REQUEST)
        try:
            address_obj = admin_models.Address.objects.get(id=address_id, customer=customer)
        except admin_models.Address.DoesNotExist:
            return Response({"message": "Address not found with the provided ID for this customer.", "status": 0},status=status.HTTP_400_BAD_REQUEST)
        address_obj.address = address
        address_obj.landmark = landmark
        address_obj.lat = lat
        address_obj.lng = lng
        address_obj.updated_at = datetime.now()
        address_obj.save()
        updated_data = {
            "id": address_obj.id,
            "customer_id": customer.id,
            "address": address_obj.address,
            "landmark": address_obj.landmark,
            "lat": address_obj.lat,
            "lng": address_obj.lng,
            "updated_at": address_obj.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        }
        return Response({"message": "Updated Successfully", "status": 1,"updated_data": updated_data},status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": f"An error occurred: {str(e)}", "status": 0},status=status.HTTP_400_BAD_REQUEST)

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def editAddress(request):
    try:
        data = request.data
        address_id = data.get('address_id')
        if not address_id:
            return Response({"message": "field ID is required.", "status": 0}, status=status.HTTP_400_BAD_REQUEST)
        user = request.user
        try:
            customer = account_models.Customer.objects.get(user=user)
        except account_models.Customer.DoesNotExist:
            return Response({"message": "Customer not found for the logged-in user.", "status": 0}, status=status.HTTP_400_BAD_REQUEST)

        try:
            address_obj = admin_models.Address.objects.get(id=address_id, customer=customer)
        except admin_models.Address.DoesNotExist:
            return Response({"message": "Address not found with the provided ID for this customer.", "status": 0}, status=status.HTTP_400_BAD_REQUEST)

        # Prepare the response data
        data = {
            "id": address_obj.id,
            "customer_id": customer.id,
            "address": address_obj.address,
            "landmark": address_obj.landmark,
            "lat": address_obj.lat,
            "lng": address_obj.lng,
            "status": address_obj.status,
            "created_at": address_obj.created_at.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
            "updated_at": address_obj.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        }

        return Response(
            {
                "result": data,
                "message": "Success",
                "status": 1
            },
            status=status.HTTP_200_OK
        )

    except Exception as e:
        return Response(
            {"message": f"An error occurred: {str(e)}", "status": 0},
            status=status.HTTP_400_BAD_REQUEST
        )

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def listCustomerAddresses(request):
    try:
        data = request.data
        customer_id = data.get('customer_id')
        if not customer_id:
            return Response({"message": "Customer ID is required.", "status": 0}, status=status.HTTP_400_BAD_REQUEST)
        try:
            customer = account_models.Customer.objects.get(id=customer_id)
        except account_models.Customer.DoesNotExist:
            return Response({"message": "Customer not found.", "status": 0}, status=status.HTTP_400_BAD_REQUEST)
        addresses = admin_models.Address.objects.filter(customer=customer)
        if not addresses:
            return Response({"message": "No addresses found for the customer.", "status": 0}, status=status.HTTP_404_NOT_FOUND)

        address_data = []
        for address in addresses:
            address_data.append({
                "id": address.id,
                "address": address.address,
                "landmark": address.landmark,
                "lat": address.lat,
                "lng": address.lng,
                "status": address.status,
                "created_at": address.created_at.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                "updated_at": address.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            })

        return Response(
            {
                "result": address_data,
                "message": "Success",
                "status": 1
            },
            status=status.HTTP_200_OK
        )

    except Exception as e:
        return Response(
            {"message": f"An error occurred: {str(e)}", "status": 0},
            status=status.HTTP_400_BAD_REQUEST
        )

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def deleteAddresses(request):
    try:
        data = request.data
        address_id = data.get('address_id')
        customer_id = data.get('customer_id')
        if not address_id or not customer_id:
            return Response({"message": "Both address_id and customer_id are required.", "status": 0}, status=status.HTTP_400_BAD_REQUEST)
        try:
            customer = account_models.Customer.objects.get(id=customer_id)
        except account_models.Customer.DoesNotExist:
            return Response({"message": "Customer not found.", "status": 0}, status=status.HTTP_400_BAD_REQUEST)
        try:
            address_obj = admin_models.Address.objects.get(id=address_id, customer=customer)
        except admin_models.Address.DoesNotExist:
            return Response({"message": "Address not found with the provided ID for this customer.", "status": 0}, status=status.HTTP_400_BAD_REQUEST)
        address_obj.delete()
        return Response( {"message": "Address deleted successfully.", "status": 1},status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": f"An error occurred: {str(e)}", "status": 0},status=status.HTTP_400_BAD_REQUEST)

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def addWalletAmount(request):
    try:
        data = request.data
        customer_id = data.get('customer_id')
        transaction_type = data.get('transaction_type')
        transaction_type_chioce = data.get('transaction_type_chioce')
        message = data.get('message')
        amount = data.get('amount')
        try:
            customer = account_models.Customer.objects.get(id=customer_id)
        except account_models.Customer.DoesNotExist:
            return Response({"message": "Customer not found with the provided customer ID.", "status": 0},status=status.HTTP_400_BAD_REQUEST)
        
        if not all([transaction_type, message, amount,transaction_type_chioce,]):
            return Response({"message": "All fields (transaction_type, transaction_type_chioce , message, amount) are required.", "status": 0},status=status.HTTP_400_BAD_REQUEST)
        
        if transaction_type == 'credit':
            customer.wallet += float(amount)
        elif transaction_type == 'debit':
            if customer.wallet < float(amount):
                return Response({"message": "Insufficient wallet balance.", "status": 0},status=status.HTTP_400_BAD_REQUEST)
            customer.wallet -= float(amount)
        else:
            return Response({"message": "Invalid transaction type provided.", "status": 0},status=status.HTTP_400_BAD_REQUEST)
        customer.save()

        wallet_history = admin_models.CustomerWalletHistory.objects.create(customer=customer,transaction_type=transaction_type,transaction_type_choices=transaction_type_chioce,message=message,amount=amount,created_at=datetime.now(),updated_at=datetime.now())
        response_data = {
            "id": wallet_history.id,
            "customer_id": customer.id,
            "transaction_type": wallet_history.transaction_type,
            "transaction_type_chioce": wallet_history.transaction_type_choices,
            "message": wallet_history.message,
            "amount": wallet_history.amount,
            "created_at": wallet_history.created_at,
            "updated_at": wallet_history.updated_at,
        }

        return Response({"message": "Wallet updated successfully.", "status": 1, "data": response_data},status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"message": f"An error occurred: {str(e)}", "status": 0},status=status.HTTP_400_BAD_REQUEST)


'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def getAllTransactionHistory(request):
    try:
        user = request.user
        customer = getattr(user, 'customer_profile', None)
        if not customer:
            return Response({"message": "Customer profile is required for the logged-in user.", "status": 0}, status=status.HTTP_400_BAD_REQUEST)
        
        customer_id = customer.id
        transactions = admin_models.CustomerWalletHistory.objects.filter(customer=customer).order_by('-created_at')
        
        # If no transactions found
        if not transactions:
            return Response({"message": "No transaction history found for the customer.", "status": 0}, status=status.HTTP_404_NOT_FOUND)
        
        
        transaction_data = [
            {
                "id": transaction.id,
                "customer_id": transaction.customer.id,
                "transaction_type": transaction.transaction_type,  
                "message": transaction.message,
                "transaction_type_choices": transaction.transaction_type_choices,  
                "amount": transaction.amount,
                "created_at": transaction.created_at.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                "updated_at": transaction.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
            }
            for transaction in transactions
        ]
        
        # Return the response with transaction data
        return Response(
            {
                "message": "Wallet transaction history retrieved successfully",
                "status": 1,
                "result": transaction_data
            },
            status=status.HTTP_200_OK
        )
    
    except Exception as e:
        return Response({"message": f"An error occurred: {str(e)}", "status": 0},status=status.HTTP_400_BAD_REQUEST)

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def getProfileDetails(request):
    try:
        user = request.user
        customer = getattr(user, 'customer_profile', None)
        if not customer:
            return Response({"message": "Customer profile not found for the logged-in user.", "status": 0}, status=status.HTTP_404_NOT_FOUND)

        # Customer Data
        customer_data = {
            "customer_id": customer.id,
            "customer_name": customer.customer_name,
            "phone_number": customer.phone_number,
            "profile_picture": customer.profile_picture.url if customer.profile_picture else None,
            "pre_existing_disease": customer.pre_existing_disease,
            "blood_group": customer.blood_group,
            "gender": customer.gender,
            "dob": customer.dob,
            "age": customer.age,
            "height": customer.height,
            "weight": customer.weight,
            "emergency_contact_no": customer.emergency_contact_no,
            "allergies": customer.allergies,
            "current_medications": customer.current_medications,
            "status": customer.status,
            "wallet": customer.wallet,
            "overall_ratings": customer.overall_ratings,
            "no_of_ratings": customer.no_of_ratings
        }

        bed_bookings = admin_models.BedBooking.objects.filter(customer=customer).values('id', 'hospital', 'ward_type', 'bed_type', 'status', 'admission_date', 'discharge_date')
        bed_booking_data = list(bed_bookings)
        help_desk_queries = admin_models.HelpDeskQuery.objects.filter(customer=customer).values('id', 'name', 'email', 'message', 'created_at')
        help_desk_data = list(help_desk_queries)
        reminders = admin_models.Reminder.objects.filter(customer=customer).values('id', 'category', 'title', 'description', 'reminder_date', 'status')
        reminder_data = list(reminders)
        feedback = admin_models.Feedback.objects.filter(customer=customer).values('id', 'doctor', 'hospital', 'lab', 'rating', 'feedback', 'created_at')
        feedback_data = list(feedback)

        response_data = {
            "customer_profile": customer_data,"bed_bookings": bed_booking_data,"help_desk_queries": help_desk_data,
            "reminders": reminder_data,"feedback": feedback_data
        }

        return Response({"message": "Customer profile retrieved successfully.", "status": 1, "result": response_data}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"message": f"An error occurred: {str(e)}", "status": 0}, status=status.HTTP_400_BAD_REQUEST)

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def getBedBookings(request):
    try:
        bed_bookings = admin_models.BedBooking.objects.all()
        result = []
        for booking in bed_bookings:
            result.append({
                "id": booking.id,
                "booking_number": f"H2H{booking.id:06d}",
                "customer_id": booking.customer.id if booking.customer else None,
                "hospital_id": booking.hospital.id if booking.hospital else None,
                "ward_type": booking.ward_type,
                "bed_type": booking.bed_type,
                "booking_type": booking.booking_type,
                "booking_for": "self",
                "patient_name": booking.patient_name,
                "email": booking.email,
                "age": booking.age,
                "contact_number": booking.contact_number,
                "emergency_contact": booking.emergency_contact,
                "blood_group": booking.blood_group,
                "medical_history": booking.medical_history,
                "booking_reason": booking.booking_reason,
                "insurance_info": booking.insurance_info,
                "admission_date": str(booking.admission_date),
                "discharge_date": str(booking.discharge_date) if booking.discharge_date else None,
                "doctor_id": booking.doctor_assigned.id if booking.doctor_assigned else None,
                "booking_date": str(booking.booking_date.date()),
                "time_slot": str(booking.time_slot) if booking.time_slot else None,
                "bed_number": 10,  # Replace with actual bed details if available
                "bed_price": "800.00",  # Replace with dynamic pricing if available
                "base_rate": "800.00",  # Replace with dynamic pricing if available
                "tax": "0.00",  # Replace with dynamic tax if applicable
                "additional_charges": "0.00",
                "discount": "0.00",
                "total": "800.00",  # Replace with calculated total
                "final_total": "800.00",  # Replace with final calculated total
                "payment_mode": "online",  # Assuming payment mode is fixed
                "ambulance_required": 1,  # Replace with dynamic value if applicable
                "ambulance_type": "with_oxygen",  # Replace with dynamic type if applicable
                "notes": booking.notes,
                "status": booking.status,
                "created_at": booking.created_at.isoformat(),
                "updated_at": booking.updated_at.isoformat(),
                "customer": {
                    "id": booking.customer.id if booking.customer else None,
                    "customer_name": booking.customer.customer_name if booking.customer else None,
                    "profile_picture_url": booking.customer.profile_picture.url if booking.customer else None
                },
                "hospital": {
                    "id": booking.hospital.id if booking.hospital else None,
                    "hospital_name": booking.hospital.hospital_name if booking.hospital else None,
                    "hospital_logo_url": booking.hospital.hospital_logo.url if booking.hospital else None,
                    "images_url": []
                },
                "doctor": {
                    "id": booking.doctor_assigned.id if booking.doctor_assigned else None,
                    "name": booking.doctor_assigned.dr_name if booking.doctor_assigned else None
                } if booking.doctor_assigned else None,
                "ward": {
                    "id": 1,  # Replace with actual ward ID if applicable
                    "name": "General Ward"  # Replace with actual ward name if applicable
                },
                "bed": {
                    "id": 7,  # Replace with actual bed ID if applicable
                    "bed_type": "General Ward Beds"  # Replace with actual bed type if applicable
                }
            })

        return Response({
            "success": True,
            "message": "Bookings retrieved successfully",
            "result": result
        }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({
            "success": False,
            "message": f"An error occurred: {str(e)}"
        }, status=status.HTTP_400_BAD_REQUEST)

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def getBookingDetails(request, booking_id):
    try:
        # Retrieve the booking by ID
        booking = admin_models.BedBooking.objects.filter(id=booking_id).first()
        if not booking:
            raise NotFound(f"No booking found with ID {booking_id}")

        # Prepare the response data
        result = {
            "id": booking.id,
            "customer_id": booking.customer_id,
            "hospital_id": booking.hospital_id,
            "ward_type": booking.ward_type,
            "bed_type": booking.bed_type,
            "booking_type": booking.booking_type,
            "patient_name": booking.patient_name,
            "email": booking.email,
            "age": booking.age,
            "contact_number": booking.contact_number,
            "emergency_contact": booking.emergency_contact,
            "blood_group": booking.blood_group,
            "medical_history": booking.medical_history,
            "booking_reason": booking.booking_reason,
            "insurance_info": booking.insurance_info,
            "admission_date": booking.admission_date,
            "discharge_date": booking.discharge_date,
            "doctor_id": booking.doctor_assigned,
            "booking_date": booking.booking_date,
            "time_slot": booking.time_slot,
            # "bed_price": booking.bed_price,  # Replace with actual logic or field
            # "base_rate": booking.base_rate,  # Replace with actual logic or field
            # "tax": booking.tax,  # Replace with actual logic or field
            # "additional_charges": booking.additional_charges,  # Replace with actual logic or field
            # "discount": booking.discount,  # Replace with actual logic or field
            # "total": booking.total,  # Replace with actual logic or field
            # "final_total": booking.final_total,  # Replace with actual logic or field
            # "payment_mode": booking.payment_mode,
            # "ambulance_required": booking.ambulance_required,
            # "ambulance_type": booking.ambulance_type,
            "notes": booking.notes,
            "status": booking.status,
            "created_at": booking.created_at.isoformat(),
            "updated_at": booking.updated_at.isoformat(),
        }

        # Return the response
        return Response({"success": True, "message": "Booking retrieved successfully", "result": result},status=status.HTTP_200_OK,)

    except NotFound as e:
        return Response({"success": False, "message": str(e)},status=status.HTTP_404_NOT_FOUND,)
    except Exception as e:
        return Response({"success": False, "message": f"An error occurred: {str(e)}"},status=status.HTTP_400_BAD_REQUEST,)

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def updateBedBookings(request, booking_id):
    try:
        booking = admin_models.BedBooking.objects.filter(id=booking_id).first()
        if not booking:
            raise NotFound(f"No booking found with ID {booking_id}")
        patient_name = request.data.get('patient_name')
        email = request.data.get('email')
        time_slot = request.data.get('time_slot')
        if patient_name:
            booking.patient_name = patient_name
        if email:
            booking.email = email
        if time_slot:
            booking.time_slot = time_slot
        booking.save()
        result = API_serializers.BedBookingSerializer(booking).data
        # result = {
        #     'booking_id': booking.id,
        #     'patient_name': booking.patient_name,
        #     'email': booking.email,
        #     'time_slot': booking.time_slot,
        # }
        return Response({"success": True, "message": "Booking updated successfully", "result": result},status=status.HTTP_200_OK,)
    except NotFound as e:
        return Response({"success": False, "message": str(e)},status=status.HTTP_404_NOT_FOUND,)
    except Exception as e:
        return Response({"success": False, "message": f"An error occurred: {str(e)}"},status=status.HTTP_400_BAD_REQUEST,)


'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def addDoctorBooking(request):
    data = request.data
    user = request.user
    customer = getattr(user, 'customer_profile', None)
    if not customer:
        return Response({"message": "Customer profile is required for the logged-in user.", "status": 0}, status=status.HTTP_400_BAD_REQUEST)
    customer_id = customer.id
    try:
        doctor = account_models.DoctorDetails.objects.get(id=data.get('doctor_id'))
    except ObjectDoesNotExist:
        return JsonResponse({"success": False,"message": "Doctor not found","doctor_id": data.get('doctor_id')}, status=404)

    try:
        clinic = admin_models.DoctorClinics.objects.get(id=data.get('clinic_id'))
    except admin_models.DoctorClinics.DoesNotExist:
        return JsonResponse({"success": False, "message": "Clinic not found", "clinic_id": data.get('clinic_id')}, status=404)

    try:
        customer = account_models.Customer.objects.get(id=customer_id)
    except ObjectDoesNotExist:
        return JsonResponse({"success": False,"message": "Customer not found","customer_id": customer_id}, status=404)
    
    booking_number = f"DOC-{random.randint(100000, 999999)}"
    base_rate = float('400.00')
    tax = float('0.00')
    additional_charges = float('0.00')
    discount = float('0.00')
    total = base_rate + tax + additional_charges - discount

    # Create booking
    booking = admin_models.DoctorBooking.objects.create(
        booking_number=booking_number,doctor=doctor,
        clinic=clinic,customer=customer,
        booking_for=data.get('booking_for'),
        patient_name=data.get('patient_name'),
        email=data.get('email'),age=data.get('age'),
        contact_number=data.get('contact_number'),
        emergency_contact=data.get('emergency_contact'),
        blood_group=data.get('blood_group'),
        medical_history=data.get('medical_history'),
        current_symptoms=data.get('current_symptoms'),
        booking_date=data.get('booking_date'),
        time_slot=data.get('time_slot'),
        consultation_charge=base_rate,
        base_rate=base_rate,tax=tax,
        additional_charges=additional_charges,
        discount=discount,total=total,
        final_total=total,
        payment_mode=data.get('payment_mode'),
        notes=data.get('notes'),
        status="pending"
    )

    # Format the response
    result = {
        "id": booking.id,
        "doctor_id": booking.doctor.id,
        "clinic_id": booking.clinic.id,
        "customer_id": booking.customer.id,
        "booking_for": booking.booking_for,
        "booking_date": booking.booking_date,
        "time_slot": booking.time_slot,
        "patient_name": booking.patient_name,
        "email": booking.email,
        "age": booking.age,
        "contact_number": booking.contact_number,
        "emergency_contact": booking.emergency_contact,
        "blood_group": booking.blood_group,
        "medical_history": booking.medical_history,
        "current_symptoms": booking.current_symptoms,
        "payment_mode": booking.payment_mode,
        "notes": booking.notes,
        "consultation_charge": booking.consultation_charge,
        "base_rate": booking.base_rate,
        "tax": booking.tax,
        "additional_charges": booking.additional_charges,
        "discount": booking.discount,
        "total": booking.total,
        "final_total": booking.final_total,
        "status": booking.status,
        "booking_number": booking.booking_number,
        "created_at": booking.created_at,
        "updated_at": booking.updated_at
    }

    return Response({"success": True,"message": "Booking created successfully","result": result}, status=status.HTTP_201_CREATED)


'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def getDoctorBooking(request):
    try:
        bookings = admin_models.DoctorBooking.objects.all()
        serializer = API_serializers.DoctorBookingSerializer(bookings, many=True)

        response = {
            "success": True,
            "message": "Bookings retrieved successfully",
            "result": serializer.data,
            "total": bookings.count()
        }
        return Response(response, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"success": False, "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def getDoctorBookingsDetails(request,booking_id):
    try:
        booking = admin_models.DoctorBooking.objects.get(id=booking_id)
        serializer = API_serializers.DoctorBookingSerializer(booking)
        response = {
            "success": True,
            "message": "Booking retrieved successfully",
            "result": serializer.data,
        }
        return Response(response, status=status.HTTP_200_OK)
    except admin_models.DoctorBooking.DoesNotExist:
            return Response({"success": False,"message": "Booking not found"}, status=status.HTTP_404_NOT_FOUND)

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def cancelDoctorBooking(request):
    booking_id = request.data.get("booking_id")
    if not booking_id:
        return Response({"success": False,"message": "Booking ID is required"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        booking = admin_models.DoctorBooking.objects.get(id=booking_id)
        if booking.status == "cancelled":
            return Response({"success": False,"message": "Booking is already cancelled"}, status=status.HTTP_400_BAD_REQUEST)
        booking.status = "cancelled"
        booking.save()
        return Response({"success": True,"message": "Booking cancelled successfully"}, status=status.HTTP_200_OK)
    except admin_models.DoctorBooking.DoesNotExist:
        return Response({"success": False,"message": "Booking not found"}, status=status.HTTP_404_NOT_FOUND)


'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def allBedStatus(request):
    bed_statuses = admin_models.BedStatus.objects.all()
    serializer = API_serializers.BedStatusSerializer(bed_statuses, many=True)
    return Response({"result": serializer.data, "message": "Success", "status": 1})


'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def getNotifications(request):
    try:
        app_module = request.data.get('app_module')
        page = request.data.get('page', 1)
        per_page = request.data.get('per_page', 10)
        if not app_module:
            return Response({"success": False, "message": "app_module is required"}, status=400)
        notifications = admin_models.Notification.objects.filter(app_module_id=app_module).order_by('-created_at')
        paginator = PageNumberPagination()
        paginator.page_size = per_page
        paginated_notifications = paginator.paginate_queryset(notifications, request)

        serialized_notifications = API_serializers.NotificationSerializer(paginated_notifications, many=True)
        return paginator.get_paginated_response({
            "success": True,
            "message": "Notifications retrieved successfully",
            "result": serialized_notifications.data,
        })

    except Exception as e:
        return Response({"success": False, "message": str(e)}, status=500)

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

class PlaceLabOrder(APIView):
    permission_classes = [IsAuthenticated] 
    authentication_classes = [JWTAuthentication]
    def post(self, request):
        serializer = API_serializers.LabOrdersSerializer(data=request.data)
        if serializer.is_valid():
            lab_order = serializer.save()
            return Response({
                'message': 'Lab order placed successfully!',
                'lab_order_id': lab_order.id
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''


'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''

'''
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
'''
