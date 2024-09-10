from datetime import datetime


class QianchengJob:
    def __init__(self, id=None, brand_name=None, job_name=None, salary_desc_min=None,
                 salary_desc_max=None, salary_desc=None, city_name=None, area_district=None,
                 business_district=None, location=None, brand_scale_name=None, brand_scale_min=None,
                 brand_scale_max=None, brand_industry=None, job_degree=None, job_experience=None,
                 brand_stage_name=None, exist_day=0, third_party_flag=0, source='0', welfareList=None,
                 created_time=None, updated_time=None):
        self.id = id
        self.brand_name = brand_name
        self.job_name = job_name
        self.salary_desc_min = salary_desc_min
        self.salary_desc_max = salary_desc_max
        self.salary_desc = salary_desc
        self.city_name = city_name
        self.area_district = area_district
        self.business_district = business_district
        self.location = location
        self.brand_scale_name = brand_scale_name
        self.brand_scale_min = brand_scale_min
        self.brand_scale_max = brand_scale_max
        self.brand_industry = brand_industry
        self.job_degree = job_degree
        self.job_experience = job_experience
        self.brand_stage_name = brand_stage_name
        self.exist_day = exist_day
        self.third_party_flag = third_party_flag
        self.source = source
        self.welfareList = welfareList
        self.created_time = created_time
        self.updated_time = updated_time

    def __repr__(self):
        return f"<QianchengJob(id={self.id}, brand_name='{self.brand_name}', job_name='{self.job_name}')>"

    def to_dict(self):
        """Convert the instance to a dictionary."""
        return {
            'id': self.id,
            'brand_name': self.brand_name,
            'job_name': self.job_name,
            'salary_desc_min': self.salary_desc_min,
            'salary_desc_max': self.salary_desc_max,

            'salary_desc': self.salary_desc,
            'city_name': self.city_name,
            'area_district': self.area_district,
            'business_district': self.business_district,
            'location': self.location,

            'brand_scale_name': self.brand_scale_name,
            'brand_scale_min': self.brand_scale_min,
            'brand_scale_max': self.brand_scale_max,
            'brand_industry': self.brand_industry,
            'job_degree': self.job_degree,

            'job_experience': self.job_experience,
            'brand_stage_name': self.brand_stage_name,
            'exist_day': self.exist_day,
            'third_party_flag': self.third_party_flag,
            'source': self.source,
            'welfareList': self.welfareList,
            'created_time': self.created_time.isoformat() if self.created_time else None,
            'updated_time': self.updated_time.isoformat() if self.updated_time else None
        }

    @classmethod
    def from_dict(cls, data):
        """Create an instance from a dictionary."""
        return cls(
            id=data.get('id'),
            brand_name=data.get('brand_name'),
            job_name=data.get('job_name'),
            salary_desc_min=data.get('salary_desc_min'),
            salary_desc_max=data.get('salary_desc_max'),
            salary_desc=data.get('salary_desc'),
            city_name=data.get('city_name'),
            area_district=data.get('area_district'),
            business_district=data.get('business_district'),
            location=data.get('location'),
            brand_scale_name=data.get('brand_scale_name'),
            brand_scale_min=data.get('brand_scale_min'),
            brand_scale_max=data.get('brand_scale_max'),
            brand_industry=data.get('brand_industry'),
            job_degree=data.get('job_degree'),
            job_experience=data.get('job_experience'),
            brand_stage_name=data.get('brand_stage_name'),
            exist_day=data.get('exist_day'),
            third_party_flag=data.get('third_party_flag'),
            source=data.get('source'),
            welfareList=data.get('welfareList'),
            created_time=datetime.fromisoformat(data['created_time']) if data.get('created_time') else None,
            updated_time=datetime.fromisoformat(data['updated_time']) if data.get('updated_time') else None
        )
