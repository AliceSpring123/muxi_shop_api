from rest_framework import serializers

from apps.menu.models import MainMenu, SubMenu

class MainMenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainMenu
        fields = "__all__"



class SubMenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubMenu
        fields = "__all__"