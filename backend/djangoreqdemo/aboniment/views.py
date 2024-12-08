from rest_framework.views import APIView
import rest_framework.generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

import aboniment.models
import aboniment.serializer


class AbonimentCreateAPIView(rest_framework.generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = aboniment.models.Aboniment.objects.all()
    serializer_class = aboniment.serializer.AbonimentCreateSerializer


class AbonimentListAPIView(rest_framework.generics.ListAPIView):
    queryset = aboniment.models.Aboniment.objects.all()
    serializer_class = aboniment.serializer.AbonimentSerializer


class AbonimentDetailUpdateDeleteAPIView(rest_framework.generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = aboniment.models.Aboniment.objects.all()
    serializer_class = aboniment.serializer.AbonimentSerializer
