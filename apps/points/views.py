# -*- coding:utf-8 -*-
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from utils.permission import IsOwnerOrReadOnly
from .models import Points
from .serializers import PointsSerializer


# Create your views here.
class GoodsPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100

class PointsViewSet(viewsets.ModelViewSet):
    """
    商品购物车
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    lookup_field = 'points_user'

    pagination_class = GoodsPagination

    def get_serializer_class(self):
        return PointsSerializer

    def get_queryset(self):
        return Points.objects.filter(user=self.request.user)
