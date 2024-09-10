class QianChengJobSource:
    def __init__(self):
        self.id = None  # bigint unsigned, auto-increment

        self.jobName = None  # varchar(100)
        self.fullCompanyName = None  # varchar(100)
        self.jobId = None  # varchar(100)
        self.jobTags = None  # varchar(255)
        self.jobAreaString = None  # varchar(100)

        self.provideSalaryString = None  # varchar(100)
        self.workYearString = None  # varchar(255)
        self.degreeString = None  # varchar(100)
        self.companyIndustryType1Str = None  # varchar(100)
        self.companyIndustryType2Str = None  # varchar(100)

        self.lon = None  # varchar(50)
        self.lat = None  # varchar(50)
        self.jobHref = None  # varchar(255)
        self.jobDescribe = None  # varchar(5000)
        self.companyHref = None  # varchar(255)

        self.termStr = None  # varchar(100)
        self.jobWelfareCodeDataList = None  # varchar(500)
        self.jobSalaryMax = None  # varchar(100)
        self.jobSalaryMin = None  # varchar(255)
        self.source = None  # text

        self.created_time = None
        self.updated_time = None

    def __str__(self):
        return f"QianChengJobSource(id={self.id}, jobName={self.jobName}, fullCompanyName={self.fullCompanyName}, ...)"