import json
from company.models import Province, District, Subdistrict
from django.db import transaction


def run(*arg):
    try:
        province_dict = {}
        district_dict = {}
        
        with transaction.atomic():
            with open('util/province.json', 'r') as file:
                data = json.load(file)
                for province in data:
                    raw_data = Province.objects.create(
                        name_th=province["name_th"],
                        name_en=province["name_en"]
                    )
                    province_dict[province['id']] = raw_data

            with open('util/district.json', 'r') as file:
                data = json.load(file)
                for district in data:
                    raw_data = District.objects.create(
                        name_th=district["name_th"],
                        name_en=district["name_en"],
                        province=province_dict[district['province_id']]
                    )
                    district_dict[district['id']] = raw_data

            with open('util/subdistrict.json', 'r') as file:
                data = json.load(file)
                for sub_district in data:
                    district = district_dict[sub_district["district_id"]]
                    raw_data = Subdistrict.objects.create(
                        name_th=sub_district["name_th"],
                        name_en=sub_district["name_en"],
                        district=district,
                        zip_code=sub_district.get("zip_code", None)
                    )

    except Exception as e:
        print(e)
        print('Something went wrong')