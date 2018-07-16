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


def get_available_jobs():
    try:
        return Job.objects.filter(status='AVAILABLE')
    except:
        return None


def get_company_jobs(company):
    try:
        return Job.objects.filter(company=company)
    except:
        return None


def get_job_by_id(id):
    try:
        return Job.objects.get(id=id)
    except:
        return None