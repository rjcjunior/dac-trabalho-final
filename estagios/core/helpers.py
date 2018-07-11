from ..core.models import Company, Job, Student


def get_company_by_user(user):
    try:
        company = Company.objects.get(user=user)
        if company:
            return company
    except:
        return False

def get_students_by_user(user):
    try:
        student = Student.objects.get(user=user)
        if student:
            return student
    except:
        return False


def get_company_jobs_avaliables():
    try:
        return Job.objects.filter(status='AVAILABLE')
    except:
        return None

def get_company_jobs(company):
    try:
        return Job.objects.filter(company=company)
    except:
        return None
        
def get_company_jobs_by_id(id):
    try:
        return Job.objects.filter(id=id)
    except:
        return None

