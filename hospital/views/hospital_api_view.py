from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from hospital import serializers
from hospital import models



@api_view(['GET'])
@permission_classes([AllowAny])  # This line allows unauthenticated access
def get_hospitals_api(request):
    hospitals = models.Hospital.objects.all().prefetch_related('doctors')
    print(hospitals)
    serializer = serializers.HospitalSerializer(hospitals, many=True)
    return Response({"result": serializer.data})
    

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

@api_view(['GET'])
@permission_classes([AllowAny])
def hospital_all_facilities(request):
    hospital_facility = models.HospitalFacility.objects.all()
    serializer = serializers.HospitalBedStatusSerializer(hospital_facility, many=True)
    return Response({"result": serializer.data})

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