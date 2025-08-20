from rest_framework import serializers
from .models import Contacts, Product, Network


class ContactsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Contacts
        fields = "__all__"


class ProductSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class NetworkSerializers(serializers.ModelSerializer):
    contacts = ContactsSerializers
    product = ProductSerializers

    class Meta:
        model = Network
        fields = "__all__"
        read_only_fields = ("arrears",)

    def validate(self, data):
        if data.get("type") == 0 and data.get("supplier") is not None:
            raise serializers.ValidationError(
                {"supplier": 'Для типа "Завод" нельзя указывать поставщика'}
            )
